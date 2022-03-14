# Taylor Adami
# Date:
# Project: Random story generator
# story generators are where we pick random items from four different defined list.
# File: storyGenerator --> main.py
# --------------------------------------------------------------------
# import random library
import random

# Create four list to hold various parts of the story.
# In this example, we will create four variables based off of the simple 'Who', 'What', 'Where', 'When'
who = ['The Nurse', 'Batman', 'Principal Skinner', 'Bruno Mars', 'Ryan Reynolds', 'Queen Elizabeth', 'Lara Croft' 
       'Julius Caesar', 'Jules Whinfield', 'Cleopatra', 'Hillary Duff', 'Coca Melon', 'you']
what = ['to Write a long essay', 'To play Valorant', 'To go to the mall and eat chinese food', 'to sing in the shower',
        'to listen to Mrs. Adami\'s awesome music', 'to return to Gotham City', 'To steal candy from a baby']
where =['Europe', 'Sweden', 'School', 'Gotham', 'Paris', 'Piqua, Ohio', 'Mars', 'Hyrule', 'Terminis', 'Your house',
        'In a strange house', 'Camp Crystal Lake', 'A Tim Burton Film... probably']
when = ['4,000 years later', 'In a galaxy far away', 'Today', 'Yesterday', 'In 5 B.C.', 'During the great Depression',
        'In the near future', 'About a week ago', ' The night before Christmas']

# Create a print statement that will use the random library to pull from the list to generate a statement
print(random.choice(when) + ', ' + random.choice(who) + ' went to ' + random.choice(where) + ' ' + random.choice(what))


# Extra Practice:
# 1) Create options for the user to create a new category and new list items.
# Add a new category called why, then create a blank list that will let us add items to our list
# If we add this new option, at the end of the print statement, have at add 'because' + random choice of the why list
# Please note: You will not be able to save this because you have not learned how to save items to a database
# **We will do this later
# ** But at this point, just run this program at once to make sure that everything works

# 2) Give an option to allow the users to add topics to an existing list.
# When you give the option, create another menu that shows all the lists that are currently there
# Then give the users the option to choose a list and add a list item.

# 3) Advanced project:
# What if we want to save all the hilarious stories that we generated into a document on our computer?
# Would that be possible? Yes. We would import a library called Sub process
# The sub process library allows us to access the computers OS. We can do a couple different things with this library
# Such as create a new file, save files, write over files.
# All the files will be saved in the same directory as the main.py, unless you specify another folder
# I would recommend, putting this in a function to keep items organized
# Read Adami's notes about uploading files, or follow the tutorial on the capstone site.
# To do this, you will need to give an option for them to save the file to the file. Or you can just do it for them.
