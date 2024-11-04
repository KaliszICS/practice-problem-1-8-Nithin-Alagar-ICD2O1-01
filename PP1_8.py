
def q1():
  #Write Assignment code here
  bool1 = True
  bool2 = False
  print(bool1 and bool2)
  print(bool1 or bool2)
def q2():
  #Write Assignment code here
  num = input("Enter an integer: ")
  num = int(num)
  bool = not 0 == num
  print(bool)
def q3():
  #Write Assignment code here
  num3 = input("Enter a number: ")
  num3 = int(num3)
  value2 = num3 >= 0 and num3 <= 10
  print(value2)
def q4():
  #Write Assignment code here
  food = input("Input food: ")
  drink = input("Input drink: ")
  result = not food == "pizza" and not drink == "pop"
  print(result)
def q5():
  #Write Assignment code here
  numb = input("Enter an integer: ")
  numb = int(numb)
  if  numb%2 == 0:
    print(f"The integer {numb} is True.")
  else:
      print(f"The integer {numb} is False.")
#Do not edit code after this
#Comment out the followwing code when running tests

#q1()
#q2()
#q3()
#q4()
#q5()
