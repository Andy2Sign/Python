


#Loops

fruits = ["Apple", "Ananas", "Banana"]

for fruit in fruits:
    if fruit[0] == "A":
      print("This is one is Skipped because the condition")
    else:
       print(fruit)
       




#For Loops and range()

a = 1
b = 10 #the last is not taken in consideration

for number in range(a,b,3):
   print(number)



#functions
   

nome = "Andrea "

cognome = "Bisegna"

def my_function(a, b):
      print("Hello " + a + b)


my_function(nome, cognome)

#function example

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def my_calc(items):
    a = " è pari"
    b = " è dispari"
    for item in items:
        if item % 2 == 0:
            print(str(item) + a)
        else:
            print(str(item) + b)

my_calc(list_numbers)