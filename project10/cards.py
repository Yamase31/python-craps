"""
Author: Beth Ann Townsend and James Lawson
File: cards.py
Project 10

This creates 52 regular playing cards to use in Card and Deck for later play!
""" 

import random

class Card(object): #the card object has a rank, suit, and also the card's image

    RANKS = tuple(range(1, 14)) #solely numerical here because of the tuple. We edit the numbers signifying face cards later

    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

    BACK_NAME = 'DECK/b.gif'

    def __init__(self, rank, suit): #this creates a card--rank and suit
        if not (rank in Card.RANKS):
            raise RuntimeError('Rank must be in ' + str(Card.RANKS))
        if not (suit in Card.SUITS):
            raise RuntimeError('Suit must be in ' + str(Card.SUITS))
        self.rank = rank
        self.suit = suit
        self.fileName = 'DECK/' + str(rank) + suit[0].lower() + '.gif'
        
    def __str__(self): #and this is the string representation, what we see, of the card. Here is where we specify what face cards are for the player
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit

class Deck(Card): #creates the class Deck, using Card above
    def __init__(self):
        self.deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card(rank, suit)
                self.deck.append(card)
                
    #to be used in isEmpty since we need its length
    def __len__(self):
        return len(self.deck)

    #checks to see when there are no more cards left in the deck
    def isEmpty(self):
        if len(self.deck) == 0:
            return True
        else:
            return False

    #moves them into a random order
    def shuffle(self):
        random.shuffle(self.deck)
        
    #removes and returns the top card
    def deal(self):
        return self.deck.pop(0)

    #the string representation of all of this    
    def __str__(self):
        stringRep = ""
        for x in self.deck:
            stringRep = stringRep + str(x) + '\n'
        return stringRep
