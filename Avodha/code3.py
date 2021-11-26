# def divide(a, b):
#     try:
#         print(a/b)
#     except Exception as e:
#         print(e)


# a = int(input("enter 1st no:"))
# b=int(input("enter 2nd no:"))

# divide(a,b)
 

   
# try:
#     a = int(input("enter 1st no:"))
#     b=int(input("enter 2nd no:"))
#     c=a/b
#     print(int(c))
# except:
#     print("I'm sorry")     


# file=open("eg.txt","w")
# content=file.write("Hai hellow world ")
# print(content)
# file.close() 

# file=open("eg.txt","r")
# content=file.read()
# print(content)
# file.close  

file=open("eg.txt","a")
content=file.write("nice to meet you")
print(content)
file.close
