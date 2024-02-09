# from multipledispatch import multipledispatch

class ParentClass:
    def call_me(self):
        print("I am parent class")

class ChildClass(ParentClass):
    def call_me(self):
        print("I am child class")
        super().call_me()

pobj = ParentClass()
pobj.call_me()

cobj = ChildClass()
cobj.call_me()
