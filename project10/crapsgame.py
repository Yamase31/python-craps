"""
Author: Beth Ann Townsend and James Lawson
File: crapsgame.py
Project 10

This represents craps, the game. Why gamble real money when you can do it online?
"""

from die import Die

class CrapsGame(object): #creation of the overarching class, CrapsGame which represents the game
    def __init__(self):
        self.die1 = Die() #defining the two dice
        self.die2 = Die()
        self.startUp = True
        self.gameState = "" 

    def initialRoll(self): #the initial role is important, as it determines if the game continues. It returns the tuple of the dice and then its string outcome
        self.die1.roll()
        print("Die 1 roll =", self.die1) #a visualization of what occurs in the roll
        self.die2.roll()
        print("Die 2 roll =", self.die2)
        self.rollTotal = self.die1.getValue() + self.die2.getValue() #adds the two dice values, following the rules of the game
        print("Total =", self.rollTotal)
        outcome = ""
        if self.rollTotal == 7 or self.rollTotal == 11: #provides for the outcome of a win right off the bat
            outcome = "You win!"
            self.startUp = False
        if self.rollTotal == 2 or self.rollTotal == 3 or self.rollTotal == 12: #provides for the outcome of a win at the game's start
            outcome = "You lose!"
            self.startUp = False
        return (self.die1, self.die2, outcome)
        
    def step(self): #"steps" through the game. This does all the rolls, returning the tuple of the dice and then its string outcome
        if self.startUp: #the initial roll
            self.startUp = False
            return self.initialRoll()
        else: #the subsequent rolls, if player makes it that far
            self.die1.roll()
            print("Die 1 roll =", self.die1)
            self.die2.roll()
            print("Die 1 roll =", self.die2)
            self.rollTotal2 = self.die1.getValue() + self.die2.getValue() #adds the dice for the value
            print("Total =", self.rollTotal2)
            outcome = ""
            if self.rollTotal2 == 7: #provides for the outcome of a game loss (rolling a total of 7)
                outcome = "You lose!"
                self.startUp = False
            if self.rollTotal == self.rollTotal2: #provides for a game win (if the roll equals the first one)
                outcome = "You win!"
                self.startUp = False
            return (self.die1, self.die2, outcome)
            

    def __str__(self): #returns the game state (ie what's happening at that time)
        return self.gameState
