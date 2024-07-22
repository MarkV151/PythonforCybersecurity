#!/usr/bin/env python3
# Sample script that writes to a file
test = open("hackme.txt", "w")

name = input("What is your name: ")
color = input("What is your favorite color: ")
pet = input("What was your first pet's name: ")
mom = input("What is your mother's maiden name: ")
school = input("What elementary school did you attend: ")

test.write(name)
test.write(color)
test.write(pet)
test.write(mom)
test.write(school)