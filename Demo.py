# encoding=utf-8

import sys
from User import User
from UserService import UserSerice
from flask import Flask, make_response, redirect, abort, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<string:name>")
def welcome(name):
    return render_template("index.html", name=name)


@app.route("/newpath")
def new_path():
    return redirect("http://www.example.com")


# ========================== 下面是接口 =====================

@app.route("/user/#<int:id>")
def getUser(id):
    userService = UserSerice()
    user = userService.load_user(id)
    if not user:
        abort(404)
    return jsonify({"id": user.id, "name": user.name, "tel": user.tel})


@app.route("/register", methods=["POST"])
def register():
    if ("username" not in request.values) or ("userpwd" not in request.values) or ("tel" not in request.values):
        return "缺少参数 !"
    username = request.values.get("username")
    userPwd = request.values.get("userpwd")
    tel = request.values.get("tel")
    userService = UserSerice()
    id = userService.createId()
    user = User()
    user.newUser(id, username, userPwd, tel)
    status, errorMsg = userService.save_user(user)
    return jsonify({"status": status, "id": "id", "errorMsg": errorMsg})


@app.route("/login", methods=["GET"])
def login():
    if ("username" not in request.values) or ("userpwd" not in request.values):
        return "缺少参数 !"
    username = request.values.get("username")
    userPwd = request.values.get("userpwd")
    userService = UserSerice()
    user = userService.getUserByName(username)
    errorMsg = ""
    status = True
    if user.getPassword() != userPwd:
        status = False
        errorMsg = "Password error!"
    # 将返回的内容放入response中
    response = make_response(jsonify({"status": status, "errorMsg": errorMsg}))
    # 添加cookie cookie
    if status: response.set_cookie("username", username)
    return response


@app.route("/updateTel", methods=["GET"])
def updateTel():
    if ("username" not in request.values) or ("tel" not in request.values):
        return "缺少参数 !"
    username = request.values.get("username")
    tel = request.values.get("tel")
    userService = UserSerice()
    status, errorMsg = userService.updateTel(username, tel)
    return jsonify({"status": status, "errorMsg": errorMsg})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=sys.argv[1] if len(sys.argv) > 1 else 5000)
