from threading import Thread, current_thread

def display(**kwargs):
  print("details of current thread", current_thread().name)
  print("details of current thread", current_thread().ident)

  for key, value in kwargs.items():
    if key =='n':
      for i in range(value):
        for key, value in kwargs.items():
          if key =='msg':
            print(value)
  # for key,value in kwargs.items():
  #   print(f"{key}:{value}")


t1=Thread(target=display,kwargs={'n':2,'msg':'monika'})

t1.start()

print("details of current thread", current_thread().name)
print("details of current thread", current_thread().ident)



for i in range(5):
  print("hello")

# from threading import Thread
# #through static method 
# class example:
#   @staticmethod
#   def display(n):
#     for i in range(n):
#       print("hello")

# # c1=example()
# t1=Thread(target=example.display,args=(4,))

# t1.start()


# from threading import Thread
# #as classmethod
# class example:
#   @classmethod
#   def display(self,n):
#     for i in range(n):
#       print("hello")

# # c1=example()
# t1=Thread(target=example.display,args=(4,))

# t1.start()

# #creating object of class then acesing the method through object of class

# class example:
#   def display(self,n):
#     for i in range(n):
#       print("hello")

# c1=example()
# t1=Thread(target=c1.display,args=(4,))

# t1.start()



#creating thread by extending thread class
from threading import Thread
from time import sleep 

videos = ["oops","dance","tutorial"]
class myclass(Thread):
  def run(self):
    for video in videos:
      print("uploading videos")
      sleep(3)
      print("video uploaded")
t1=myclass()
t1.start()

for i in range(4):
  sleep(0.5)
  print("checking copyright")