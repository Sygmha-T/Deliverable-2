import json
import os
import re

FILENAME = "profile.json"

name = input("What is your Full name? ")
print("Your name is", name)
print("------Welcome", name, "------")

while True:
    age = (input("How old are you? "))
    if age.isdigit():
        break
    else:
        print("Your age is invalid")
        
height = input("How tall are you? ")
weight = input("What is your weight? ")
no_of_family = input("How many are you in your family? ")
siblings = input("Do you have siblings? Yes/No ")
nationality = input("What Nationality do you hold? ")
language = input("What language do you speak? ")
social = input("What social medium do you use mostly? ")

profile_data = {
    "name": name,
    "age": int(age),
    "height": height,
    "weight": weight,
    "no_of_family": no_of_family,
    "siblings": siblings,
    "nationality": nationality,
    "language": language,
    "social": social
}

print("Your name is ", name)
print(f"You are {age} years old")
print(f"You are {height} tall")
print(f"Your weight is {weight}")
print(f"You are {no_of_family} in your family")
print(f"Siblings? {siblings}")
print(f"You are {nationality}")
print(f"You speak {language} language")
print(f"Your most used social medium is {social}")

with open(FILENAME, "w") as fp:
    json.dump(profile_data, fp, indent=4)

print(f"Profile successfully saved to {FILENAME}")