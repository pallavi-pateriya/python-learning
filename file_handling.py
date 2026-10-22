# # # # # file =  open("practise.txt","w")
# # # # # file.write("Hello Python")
# # # # # file.close()

# # # # file = open("practise.txt", "r")

# # # # content = file.readlines()

# # # # print(content)

# # # # # file.close()

# # # # # file = open("practise.txt","a")
# # # # # file.write("\nI am learning python")
# # # # # file.close()

# # # file = open("student.txt", "a")

# # # file.write("\nPriya")

# # # file.close()

# # file = open("student.txt","r")
# # content = file.readlines()
# # print(content)
# # file.close()

# file = open("student.txt","r")
# while True:
#     content= file.read()
#     if content == "":
#         break
#     print(content)
# file.close()


# file = open("names.txt","w")
# file.write("parul")
# file.write("\nravi")
# file.write("\npriya")

# file = open("names.txt","r")
# while True:
#     content =file.readline()
#     if content == "":
#         break
    
#     print(content,end="")
# file.close()

# file = open("practise.txt", "r")

# file.seek(2)

# print(file.read())

# file.close()


file = open("practise.txt", "a+")

file.seek(0)

file.write(" WORLD")

file.seek(0)
print(file.read())

file.close()

file = open("child.txt", "x")

file.write("Monika")

file.close()


with open("practise.txt","r+")as file:
    file.write("I am not learning python")
    file.write("\nI am learning python")


print(file.close())

file = open("student.txt", "r+")

print(file.readline(),end="")
print(file.readline())
print(file.readline())

file.close()