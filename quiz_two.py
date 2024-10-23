#1. write a program that takes 2 numbers as input and displays there sum, differnce, product and quotient.
#2. write a programm that compares two intergers and prints whether the 1st number is greater than or less than or equal to the 2nd number.
#3. write a programm that checks if a given number is between 10 and 20 (20 is also inclusive) using logical operators.
#4. write a programm that prints the squares of all integers from 1 to 10 using a 4 loop.


# Answer 1
num_1 = int(input('Enter the 1st num: '))
num_2 = int(input('Enter the 2nd num: '))

sum =(num_1 + num_2)
print(f"the sum of {num_1} and {num_2} is :{sum}") #customizing (but can also use concatination)

difference =(num_1 - num_2)
print (f"the difference of {num_1} and {num_2} is : {difference}")

product =(num_1 * num_2)
print (f"the product of {num_1} and {num_2} is :{product}")

division =(num_1 / num_2)
print (f"the quotient of {num_1} by {num_2} is :{division}")

fdivision =(num_1 // num_2)
print (f"the floor of {num_1} by {num_2} is :{fdivision}")


modulus =(num_1 % num_2)
print (f" The modulus of {num_1} and {num_2} is :{modulus}")

# Answer 2
if num_1 > num_2 :
    print(f"{num_1} Is g2reater than {num_2}")
elif num_1 < num_2 :
    print(f"{num_1} Is less than {num_2}")
else :
    print (f"They are equal")
    
#Answer 4
for y in range (1, 11) :
    square = y**2
    print(f"square of {y} is : {square}")

#Answer 3
for y in range(10, 21) :
    

#write a simple program that asks a user for their age if it is greater or equal to 18, print adult, 
# you are an adult and u are qualified and if less than 18 then u are not qualified.
#ANSWER
    my_age = int(input('enter your age: '))
if my_age >= 18 :
    print("is an adult and qualified ")
elif my_age < 18:
    print("is not qualified")
