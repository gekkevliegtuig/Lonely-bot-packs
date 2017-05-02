# This Python file uses the following encoding: utf-8
import os, sys

#This document is just for entertaiment purposes
#Avaible under MIT-License. © Joeri Jungschlager

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

hobby = raw_input("What is your Hobby?")
relationship = raw_input("What is your Relationship status?")
dream = raw_input("What is your dream?")

print "Ah, so your hobby is %s, your relationship status is %s, " \
"and your dream is %s." % (hobby, relationship, dream) 

from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

from datetime import datetime
now = datetime.now()

print '%s-%s-%s' % (now.year, now.month, now.day) 
print '%s:%s:%s' % (now.hour, now.minute, now.second) 	
print "It's time to head to the clinic!" 


def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

