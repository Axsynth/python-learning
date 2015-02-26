# Exercise 35 - Branches and Functions

"""
My Notes:
After going through the "game", it's know that there's very limited logic.
I understand that this isn't suppose to be complete and it's an exercise,
but come on, even the logic doesn't make sense in some cases.

Example:
gold_room() raw input for gold doesn't include "0" or "1", it's not a number.
If I type 22, that is a number, but not by this logic. Mayhaps I'll come across
this one day in the future and find out how to do a range of "or"s without 
writing too many or statements.
"""

from sys import exit

# defining function gold_room()
def gold_room():
    print "This room is full of gold. How much do you take?"
    
    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice) # This makes the choice an integer and assign it to how_much
    else:
        dead("Man, learn to type a number.")
    
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0) # exit the program.
    else:
        dead("You greedy bastard!")

# defining function bear_room()
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    while True:
        choice = raw_input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        # adding this for help text sake
        elif choice == "open door" and not bear_moved:
            print "You can't open the door. The bear is in front of it."
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now"
            
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "help":
            # adding a helper for what words can be used.
            print "Your choices are:"
            print "take honey"
            print "taunt bear"
            print "open door"
        # adding a hidden action
        elif choice == "ninja":
            print "The bear turned into a cardboard cutout of a bear."
            print "You walk through the door with ease."
            gold_room()
        else:
            print "I got no idea what that means."

# defining function cthulhu_room()
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you \"flee\" for your life or eat your \"head\"?"
    
    choice = raw_input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

# defining function dead()
# "why" inside dead() is the return value when the function used.
def dead(why):
    print why, "Good job!"
    exit(0)

# defining function start()
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    choice = raw_input("> ")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You hear a quote: 'You are already dead. You just haven't caught up yet.")

# start the adventure
start()