
#deco for multiplication of result of function with args
from functools import wraps
def deco(func):
  @wraps(func)
  def wrapper(*args):
    result=func(*args)
    for i in args:
      result=result*i
    return result
  return wrapper

@deco
def sum(*args):
  add =0

  for i in args:
    add+=i
  return add
print(sum(1,2,3))






#deco for  login required
from functools import wraps
def authenticate(func):
  @wraps(func)
  def wrapper(**kwargs):
    for key,value in kwargs.items():
      print(f"{key}:{value}")

      if key == "name" and value == "monika":
         
         return func(**kwargs)
      
    print("login required")
      
    #return render login.html
  return wrapper

@authenticate
def dashboard(**kwargs):
  print("this is the home page")
  

print(dashboard(age = 22,name="monika"))


#drco to swap the value if divisor is greater than dividend
from functools import wraps
def outer(func):
  @wraps(func)
  def inner(a,b):
    if a<b:
      a,b=b,a
      print(a)
      print(b)
    
    return func(a,b)
  return inner
  
@outer
def div(a,b):
  return a/b

print(div(7,11))
    
    