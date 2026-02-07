# 3.4 Fill in the Missing Code 
for row in range(2): # Sets up my rows
    for column in range(7): # Tells how many @ I want per row 
        print('@', end='') # Prints the rows 
    print() # Prints the next coloum  

# 3.9 Separating the Digits in an Interger 
number = int(input("Enter a number 7 to 10 digits: ")) # Gets input and makes int 
num_length = len(str(number)) # Gets me the length of the number 
divisor = 10 ** (num_length - 1) # Gives me the starting power 

while divisor >= 1: # Loop for digit 
    digit = number // divisor # Gives First Digit
    print(digit)  # Prints said digit               
    number %= divisor  # Keeps what is left 
    divisor //= 10  # Moves the divisor 

# 3.11 Miles Per Gallon 
Total_Miles = 0 # Total Miles Variable
Total_Gallons = 0 #Total Gallons Variable 
miles = int(input("How many miles did you drive (Enter -1 to Quit): ")) # Loop Variable & Miles Input 
while miles != -1:  # Loop for Mpg
    gallons = int(input("How many gallons of gas did you use: ")) # Gallons Input 
    mpg = miles/gallons # MPG Calc 
    print("Your miles per gallon was", mpg) # Prints MPG for Trip
    Total_Miles += miles # Line 26 & 27 adds to the totals 
    Total_Gallons += gallons 
    miles = int(input("How many miles did you drive (Enter -1 to Quit): ")) # Repeats or closes loop 
if Total_Miles != 0: # Checks to make sure trip was entered 
    overall_mpg = Total_Miles/Total_Gallons # Overall mpg calc
    print("For these trips, your averge mpg was", overall_mpg) # Prints overall mpg 

# 3.12 Palindromes 
num = int(input("Enter a five digit number: ")) # Asks for the five digit number and makes it an int 

first_num = num // 10000 # Gives me the first digit 
fifth_num = num % 10 # Gives me the fifth digit 
second_num = (num // 1000) % 10 # Gives me the Second Digit
fourth_num = (num // 10) % 10 # Gives me the Fourth Digit 

is_palindrome = first_num == fifth_num and second_num == fourth_num # Checks for first = Fifth and Second = Fourth 
if is_palindrome == True: # Checks to see if the palindrone variable is T/F and prints the appropriate function 
    print(" The number is a palindrome :)")
else:
    print("The number is not a palindrome :(")

# 3.14 Challenge: Approximation the Mathmatical Constant (Pi)
# Answers:
# 3.14 reached twice in a row at iteration: 628
# 3.141 reached twice in a row at iteration: 2455
pi = 0 # Running Total of pi  
denom = 1 # Denominator 
prev_pi = 0 # Stores the previous PI 
print(f"{'Term':<10} | {'Pi Value'}") # Table Header Creation 
for i in range(1, 3001): # For Loop going from 1 to 3000 
    if i % 2 == 0: 
        pi -= 4 / denom
    else:
        pi += 4 / denom
    print(f"{i:<10} | {pi:.6f}") # Prints Term Number and pi rounded 
    if f"{pi:.2f}" == "3.14" and f"{prev_pi:.2f}" == "3.14": # Checks for 3.14 repeat 
        pass 
    if f"{pi:.3f}" == "3.141" and f"{prev_pi:.3f}" == "3.141": # Checks for 3.141 repeat
        pass
    denom += 2 # Increase Denominator 
    prev_pi = pi # Saves the pi value for repeat check 