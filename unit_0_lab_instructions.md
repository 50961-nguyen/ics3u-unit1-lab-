## Unit 0 Lab - Movie Theater Edition ##

## Description ##
In this lab, you will create a Python program that simulates a movie theater ticket purchasing system at Father Michael Goetz through text-based input and output.

You'll use variables to store customer information and apply conditional logic to determine ticket prices and eligibility for different movies.

This lab is designed to assess your understanding of foundational programming concepts in Python.

You will choose one of three challenge tiers: Bronze, Silver, or Gold.

Each tier builds on the previous one, allowing you to demonstrate your skills at a level that matches your comfort and curiosity.

You are encouraged to challenge yourself and aim for the highest tier you feel ready for.

## Bronze Tier - Max Grade of 70%

Tasks:
- Use print() to greet the user with the message: Welcome to Goetz Cinema!
- Use input() to ask for the customer's name and age.
- Store the inputs in variables.
- Print a personalized message using the variables.
- Use an if statement to check if the customer is 13 or older:
    > If yes, print "You can watch PG-13 movies."
    > If not, print "You can only watch G and PG movies."

**Sample Output:**
Welcome to Goetz Cinema!
What is your name? Sarah
How old are you? 15
Hello Sarah, you are 15 years old.
You can watch PG-13 movies.

## Silver Tier - Max Grade of 85%

Tasks:
- Complete all Bronze tasks.
- Ask the customer how many tickets they want to purchase.
- Calculate the total cost (each ticket costs $12).
- Print the total cost in a formatted message.

Add another conditional with elif:
    > If the customer is 65 or older, print "You qualify for a senior discount!"
    > Elif the customer is 12 or younger, print "You qualify for a child discount!"
    > Else, print "Regular ticket pricing applied."

**Sample Output:**
Welcome to Goetz Cinema!
What is your name? Robert
How old are you? 70
How many tickets would you like? 2
Hello Robert, you are 70 years old.
Your total cost is: $24
You qualify for a senior discount!
You can watch PG-13 movies.

## Gold Tier - Max Grade of 100%
Note: You are ON YOUR OWN for programming the extra conditions below!

Tasks:
- Complete all Bronze and Silver tasks.
- Ask the customer if they are a rewards member (yes or no).
- Use conditionals to apply discounts based on their answer:
    > If "yes", calculate a 10% discount on the total and print the new discounted total. Hint: use :.2f in your print
    > If "no", print "Join our rewards program to save 10%!" and the total
    > For any other response, print "Invalid response. Join our reward system to save 10%!" and the total

**Modify** the movie eligibility conditional from Bronze Tier using logical operators:
    > If the customer is 17 or older **and** purchases 3 or more tickets, print "You're eligible for our group R-rated movie package!"
    > Otherwise, print "Standard ticket purchase - enjoy the show!"

**Sample Outputs:**
Welcome to Goetz Cinema!
What is your name? Marcus
How old are you? 19
How many tickets would you like? 4
Are you a rewards member? (yes/no) yes
Hello Marcus, you are 19 years old.
Your discounted total is: $43.20
Regular ticket pricing applied.
You're eligible for our group R-rated movie package!

Welcome to Goetz Cinema!
What is your name? Sarah
How old are you? 12
How many tickets would you like? 4
Are you a rewards member? (yes/no) no
Hello Sarah, you are 12 years old.
Join our rewards program to save 10%!
Your total is: $48.00
You qualify for a child discount!
Standard ticket purchase - enjoy the show!

## Reminders:
* Do not forget header comments with you and your partner's name!
* Make sure your code has IPO comments.
    * They should not be placed randomly, but in the correct places. Remember that the Input section is where we declare our variables (can be blank), the processing is where we transform variables (can be blank) and the output is where we print (can't really ever be blank, or we would not have an output of the code we wrote)
    * Use comments to explain your code
* Read through all of the lab expectations before you start. You'll note that these are not really that long.
* Start with Bronze. Then if you have time, build your way to Silver/Gold!

## Submission Instructions
- Submit your .py file as unit0_lab_tier.py (e.g., unit0_lab_gold.py) via GitHub.
