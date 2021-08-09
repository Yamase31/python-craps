"""
Author: Beth Ann Townsend and James Lawson
File name: testcard.py
Project 10

This runs a test to see if the cards are working properly by presenting the rank and suit.
"""

from cards import Card

def main(): #prints the cards for us to see
   for suit in Card.SUITS:
      for rank in Card.RANKS:
         card = Card(rank, suit)
         print(card)

if __name__ == "__main__":
   main()
