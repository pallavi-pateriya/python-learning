#list comprehension
"l=[expression for item in iterable if condition]"


numbers = [2, 4, 6, 7, 8, 3, 10]

l=[i*i for i in numbers if i>5]

print(l)





#dict comprehesnion

"dict={key: value for item in iterable if condition}"

names = ["Monika", "Raj", "Priya", "Amit", "Rahul"]


dict={i:len(i) for i in names if len(i)>4}

print(dict)


#set comprehension
"{expression for item in iterable}"

s={0,1,2,3,2,2,3}
set={i for i in s}
print(set)