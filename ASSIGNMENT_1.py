
"""
ASSIGNMENT
1. We have the following students detials and mark, enter these detials in the keyboard
  student name= Ritah
  student number= SEP23/BCS/14
  Programming= 78
  Data Science= 89
  Computer Applications= 55
calulate the average mark and print the ans in 3 dp

2. Write a prograam that converts celsius temp to f. 
The program should ask the user to enter the temperature in c degrees and then dispaly the temperatuer converted to farhenheit.

3. A car's miles per gallaton can be calcullated with the following formula.
Write a programm that asks a user to for the number of miles driven and gallons used.
It should calculate mlies per gallon used and display the the results.
MPG = miles Driven/ gallons of gas used
"""

#.ANSWER 1
student_name= input("Enter student name: ")
student_number= input("Enter student number: ")
Programming= int(input(" Enter marks scored in Programming:  "))
Data_Science= int(input("Enter marks scored in Data Science: "))
Computer_Applications= int(input(" Enter maeks scored in Computer Applications: "))

sum=Programming + Data_Science + Computer_Applications
number_of_subjects= 3
average = sum/number_of_subjects # option 1
#average = (Programming + Data_Science + Computer_Applications)/3 #this is also an alternative option
#Average = round(average , 3) # option 3
Average = f" The average mark of all the marks is : {average:.3f}"
print (Average)

#marks = [78, 89, 55]
#average = sum(marks) / len(marks)
#Average = f"{float(average):.3f}"
#print("Average:", Average )

#ANSWER 2
def celsius_to_fahrenheit (celsius): fahrenheit = (celsius*9/5) + 32; return fahrenheit
Temp = float(input("Enter the Temperatuer: Degrees celsius"))
Temperatuer_in_fahrenheit = celsius_to_fahrenheit(Temp)
print(f"{Temperatuer_in_fahrenheit} degrees fahrenheit")

#ANSWER 3
number_of_miles_driven = float(input("Enter the number of miles driven: "))
number_of_gallons_used =float(input("Enter the number of gallons used: "))
MPG = number_of_miles_driven/ number_of_gallons_used
print(MPG)

