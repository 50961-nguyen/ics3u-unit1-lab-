## Unit 0 Lab ##

## Description ##
In this lab, you will create a Python program that interacts with the user through text-based input and output. 

You’ll use variables to store information and apply conditional logic to make decisions based on user responses. 

This lab is designed to assess your understanding of foundational programming concepts in Python.

You will choose one of three challenge tiers: Bronze, Silver, or Gold. 

Each tier builds on the previous one, allowing you to demonstrate your skills at a level that matches your comfort and curiosity. 

You are encouraged to challenge yourself and aim for the highest tier you feel ready for.

## Bronze Tier - Max Grade of 70%

Tasks:
- Use print() to greet the user with the message: Welcome to the Python Basics Lab!
- Use input() to ask for the user's name and age.
- Store the inputs in variables.
- Print a personalized message using the variables.
- Use an if statement to check if the user is 18 or older:
    > If yes, print "You are eligible to vote."
    > If not, print "You are not eligible to vote yet."

**Sample Output:**
Welcome to the Python Basics Lab!
What is your name? Nguyen
How old are you? 17
Hello Nguyen, you are 17 years old.
You are not eligible to vote yet.

## Silver Tier - Max Grade of 85%
Tasks:
- Complete all Bronze tasks.
- Ask the user for their country.
- Use a conditional to check if the country is "Canada":
    > If yes, print "You live in Canada!"
    > If not, print "You live outside Canada."

Add another conditional:
    > If the user is under 13, print "You're quite young to be coding!"

**Sample Output:**
Welcome to the Python Basics Lab!
What is your name? Nguyen
How old are you? 12
What country do you live in? Canada
Hello Nguyen, you are 12 years old.
You live in Canada!
You're quite young to be coding!
You are not eligible to vote yet.

## Gold Tier - Max Grade of 100% 
Note: You are ON YOUR OWN for programming the extra conditions below! 

Tasks:
- Complete all Bronze and Silver tasks.
- Ask the user for their favorite programming language.
- Use conditionals to respond differently based on their answer:
    > If "Python", print "Great choice! Python is beginner-friendly."
    > If "JavaScript", print "JavaScript is awesome for web development!"
    > Else, print "That's a cool language too!"

**Modify** the voting eligibility conditional from Bronze Tier using logical operators:
    > If the user is 18 or older **and** lives in Canada, print "You can vote in Canadian federal elections!"
    > If the user is under 18 or does not live in Canada, print "You may not be eligible to vote in Canada yet."

**Sample Output:**
Welcome to the Python Basics Lab!
What is your name? Nguyen
How old are you? 18
What country do you live in? Canada
What is your favorite programming language? Python
Hello Nguyen, you are 18 years old.
You live in Canada!
Great choice! Python is beginner-friendly.
You can vote in Canadian federal elections!

## Reminders:
* Do not forget header comments with you and your partner's name!
* Make sure your code has IPO comments.
    * They should not be placed randomly, but in the correct places. Remember that the Input section is where we declare our variables (can be blank), the processing is where we transform variables (can be blank) and the output is where we print (can't really ever be blank, or we would not have an output of the code we wrote)
    * Use comments to explain your code
* Read through all of the lab expectations before you start. You'll note that these are not really that long.
* Start with Bronze. Then if you have time, build your way to Silver/Gold!

## Submission Instructions
- Submit your .py file as unit0_lab_tier.py (e.g., unit0_lab_gold.py) via GitHub.
