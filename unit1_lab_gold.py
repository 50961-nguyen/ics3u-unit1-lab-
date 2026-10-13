"""
author: Nguyen
date: October 13, 2026
Unit 1 Lab
"""

print("Welcome to Goetz Haunted House!")

# Input
name = input("Enter name: ")
age = int(input("Enter age: "))

# tickets for silver + gold
tickets = int(input("Enter the amount of tickets: "))

# reward for gold
reward = input("Are you a rewards member? (enter yes/no): ")

# Processing / Output
total = tickets * 12

# for bronze
print(f"Hello {name}, you are {age} years old.")
if age >= 13:
    print("You can enter the 13+ haunted attraction.")
else:
    print("You can visit the family-friendly attractions.")

# for gold
if reward == "yes":
    total = total * 0.9
    print(f"Your discounted total cost is: ${total:.2f}")

elif reward == "no":
    print("Join our rewards program to save 10%!")
    print(f"Your total cost is: ${total}")

else: 
    print("Invalid response. Join our rewards program to save 10%!")
    print(f"Your total cost is: ${total}")

# for silver + gold
if age >= 65:
    print("You qualify for a senior discount!")

elif age <= 12:
    print("You qualify for a child discount!")

else: 
    print("Regular ticket pricing applied.")

# for gold
if age >= 17 and tickets >= 3:
    print("You're eligible for our group after-dark haunted attraction package!")
else:
    print("Standard ticket purchase - enjoy the haunted house!")