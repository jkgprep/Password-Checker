#Jonas Kennedy, 1/3/2022, program that checks the passwords length and certain requirements.

sc = "!@#$%^&*()-+?_=,<>/"


password = str(input("Please enter a password 12 characters long with 1 special character, 1 number, and 1 upper case letter.\n"))

for i in password: 
  if len(i) < 12:
    print("Your password must be 12 characters or longer")
  elif i.isnumeric() == False:
    print("Your password needs number")
  elif i.isupper() == False: 
    print("Your password needs a upper case letter")
  elif any(c in sc for c in i) == False:
    print("Your password needs a special character")
  else:
   print("Your password is compable")

