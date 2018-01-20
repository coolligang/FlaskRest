# encoding=utf-8

class User:
    id = ""
    name = ""
    password=""
    tel = ""

    def __init__(self):
        pass

    def newUser(self,id,name,pwd,tel):
        self.id=id
        self.name=name
        self.password=pwd
        self.tel=tel

    def setId(self,id):
        self.id=id

    def setName(self, name):
        self.name = name

    def setTel(self, tel):
        self.tel = tel

    def setPassword(self,password):
        self.password=password

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getPassword(self):
        return self.password

    def getTel(self):
        return self.tel

    def toString(self):
        return "%s,%s,%s,%s" %(self.id,self.name,self.password,self.tel)


