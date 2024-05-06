print ("Welcome Back !!")

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "admin":
  print ("Hi admin")
elif username == "user" and password == "user":
  print ("Hi user")
elif username == "   " and password == "   ":
  print ("Hi guest")
else :
  print ("Well, you not have access")
