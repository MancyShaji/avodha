class student:
    def __init__(self ,name,std):
        self.name=name
        self.std=std
    def putdata(self):
        self.name = input("enter your name ")
        self.std = input("enter your class ")    

class hod(student):
    def __init__(self ,hodname):
        self.hodname = hodname
    def givedata(self):
        self.hodname = input("enter hod name ")
    def display(self):
        print("student name is ",self.name)
        print("student class is ",self.std)
        print("hod name is ",self.hodname)
obj = hod("") 
obj.putdata() 
obj.givedata()
obj.display() 

# class student:
#     def __init__(self ,name,std):
#         self.name=name
#         self.std=std
#     def putdata(self):
#         self.name = input("enter your name ")
#         self.std = input("enter your class ")    

# class hod(student):
#     def __init__(self ,hodname):
#         self.hodname = hodname
#     def givedata(self):
#         self.hodname = input("enter hod name ")

# class principal(hod):
#     def __init__(self ,pname):
#         self.pname = pname
#     def getdata(self):
#         self.pname = input("enter principal's name ")
#     def display(self):
#         print("student name is ",self.name)
#         print("student class is ",self.std)
#         print("hod name is ",self.hodname)
#         print("principal name is ",self.pname)   

# obj = principal("")
# obj.putdata()
# obj.givedata()
# obj.getdata()
# obj.display()

# class A:
#     def get1(self):
#         print("am A class")
# class B:
#     def get2(self):
#         print("am B class")

# class C(A,B):
#     def put(self):
#         print("yes am inherited A & B")

# obj = C()
# obj.get1()
# obj.get2()
# obj.put()
       


