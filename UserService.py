# encoding=utf-8

from User import User
from random import sample


class UserSerice:

    def __init__(self):
        self.path="data/user.txt"

    def load_user(self, id):
        user=file=None
        try:
            file = open(self.path, "r")
            for line in file:
                list = line.split(",")
                if str(list[0]) == str(id):
                    user = User()
                    user.setId(int(id))
                    user.setName(list[1])
                    user.setPassword(list[2])
                    user.setTel(list[3])
                    break
        except Exception,e:
            print e.message
        finally:
            file.close()
        return user

    def getUserByName(self,name):
        user=file=None
        try:
            file=open(self.path,"r")
            for line in file:
                list=line.split(",")
                if str(list[1])==name:
                    user=User()
                    user.setId(int(list[0]))
                    user.setName(name)
                    user.setPassword(list[2])
                    user.setTel(list[3][:-1])
                    break
        except Exception,e:
            print e.message
            return
        finally:
            file.close()
        return user

    def list_allUsers(self):
        file=None
        list = []
        try:
            file = open(self.path, "r")
            for line in file:
                list_user = line.split(",")
                user = User()
                user.id = list_user[0]
                user.name = list_user[1]
                user.password = list_user[2]
                user.tel = list_user[3][:-1]
                list.append(user)
        except Exception,e:
            print e.message
            return
        finally:
            file.close()
        return list

    def save_user(self, user):
        errorMsg=""
        status=False
        if isinstance(user, User):
            file = None
            try:
                file = open("data/user.txt", "a+")
                file.write("%s\n" % user.toString())
                status=True
            except Exception, e:
                errorMsg=e.message
            finally:
                file.close()
        else:
            errorMsg="Params must be object User."
        return status,errorMsg

    def updateTel(self,name,tel):
        errorMsg=""
        status=False
        file=None
        try:
            file=open(self.path,"r")
            for line in file:
                list_line=line.split(",")
                if list_line[1]==name:
                    list_line[3]=tel
                    user=User()
                    user.newUser(list_line[0],list_line[1],list_line[2],list_line[3])
                    status,errorMsg=self.save_user(user)
                    break
        except Exception,e:
            errorMsg=e.message
        finally:
            file.close()
        return status,errorMsg

    def createId(self):
        users = self.list_allUsers()
        list_id = []
        for user in users:
            list_id.append(user.id)
        id = int(max(list_id)) + 1
        return id

    def createPassword(self):
        num = "012345678901234567890123456789"
        return "".join(sample(num, 4))

    def createTel(self):
        num = "012345678901234567890123456789"
        return "%d%s" % (13, "".join(sample(num, 9)))

    def createUser(self):
        user = User()
        id = self.createId()
        name = "cool%s" % id
        user.newUser(id, name, self.createPassword(), self.createTel())
        return user


if __name__ == "__main__":
    test = UserSerice()
    user = test.createUser()
    test.save_user(user)
