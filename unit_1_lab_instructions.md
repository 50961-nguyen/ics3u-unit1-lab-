# Unit 0 Lab - Haunted House Edition

## Description

In this lab, you will create a Python program that simulates a haunted-house ticket booth at Father Michael Goetz using text-based input and output.

You will use variables to store visitor information, calculate ticket costs, and apply conditional logic to determine which attractions visitors can enter and whether they qualify for a ticket discount.

This lab assesses your understanding of foundational programming concepts in Python. Choose one of three challenge tiers: Bronze, Silver, or Gold. Each tier builds on the previous one, allowing you to demonstrate your skills at a level that matches your comfort and curiosity. You are encouraged to challenge yourself and aim for the highest tier you feel ready for.

## Submission Instructions

Submit your `.py` file via GitHub as `unit1_lab_tier.py` (for example, `unit1_lab_bronze.py`, `unit1_lab_silver.py`, or `unit1_lab_gold.py`).

## Bronze Tier - Max Grade of 70%

### Tasks

- Greet the visitor with the message: `Welcome to Goetz Haunted House!`
- Ask for the visitor's name and age.
- Print a personalized message using the variables.
- Use a conditional to check whether the visitor is 13 or older:
  - If user is 13 or older, print `You can enter the 13+ haunted attraction.`
  - If not, print `You can visit the family-friendly attractions.`

### Sample Output

```text
Welcome to Goetz Haunted House!
Enter name: Sarah
Enter age: 15
Hello Sarah, you are 15 years old.
You can enter the 13+ haunted attraction.
```

## Silver Tier - Max Grade of 85%

### Tasks

- Complete all Bronze tasks.
- Ask the visitor how many tickets they want to purchase.
- Calculate the total cost and store it in a variable. Each ticket costs $12.
- Print the total cost in a formatted message.
- Add another conditional:
  - If the visitor is 65 or older, print `You qualify for a senior discount!`
  - If the visitor is 12 or younger, print `You qualify for a child discount!`
  - Otherwise, print `Regular ticket pricing applied.`

For this tier, print the discount qualification message; you do not need to change the ticket price.

### Sample Output

```text
Welcome to Goetz Haunted House!
Enter name: Robert
Enter age: 70
Enter the amount of tickets: 2
Hello Robert, you are 70 years old.
You can enter the 13+ haunted attraction.
Your total cost is: $24
You qualify for a senior discount!
```

## Gold Tier - Max Grade of 100%

**Note:** You are on your own for programming the extra conditions below!

### Tasks

- Complete all Bronze and Silver tasks.
- Ask the visitor if they are a rewards member (`yes` or `no`).
- Use conditionals to apply a discount based on their answer:
  - If the answer is `yes`, calculate a 10% discount on the total and print the discounted total. Hint: use `:.2f` somewhere in your print statement.
  - If the answer is `no`, print `Join our rewards program to save 10%!` and print the total.
  - For any other response, print `Invalid response. Join our rewards program to save 10%!` and print the total.
- **Modify** the age conditional from Bronze Tier using a logical operator and move the print statement to the end:
  - If the visitor is 17 or older **and** purchases 3 or more tickets, print `You're eligible for our group after-dark haunted attraction package!`
  - Otherwise, print `Standard ticket purchase - enjoy the haunted house!`

### Sample Outputs

```text
Welcome to Goetz Haunted House!
Enter name: Marcus
Enter age: 19
Enter the amount of tickets: 4
Are you a rewards member? (enter yes/no): yes
Hello Marcus, you are 19 years old.
Your discounted total is: $43.20
Regular ticket pricing applied.
You're eligible for our group after-dark haunted attraction package!
```

```text
Welcome to Goetz Haunted House!
Enter name: Sarah
Enter age: 12
Enter the amount of tickets: 4
Are you a rewards member? (enter yes/no): no
Hello Sarah, you are 12 years old.
Join our rewards program to save 10%!
Your total cost is: $48.00
You qualify for a child discount!
Standard ticket purchase - enjoy the haunted house!
```

## Reminders

- Do not forget header comments with your name!
- Make sure your code has IPO comments.
- Use comments to explain your code.
- Read through all of the lab expectations before you start.
- Start with Bronze. Then, if you have time, build your way to Silver and Gold!
