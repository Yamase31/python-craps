"""
Author: Beth Ann Townsend and James Lawson
File: testdeck.py
Project 10

This tests the deck to easily show if it's functioning properly.
"""

from cards import Card, Deck

def main(): #creates deck, deals them, prints them, then shuffles and repeats
   deck = Deck()
   print("NUMBER OF CARDS:", len(deck))
   print("THE CARDS IN A NEW DECK:")
   while not deck.isEmpty():
      print(deck.deal())
   

   deck = Deck()
   deck.shuffle()
   print("\nTHE CARDS IN A SHUFFLED DECK:")   
   while not deck.isEmpty():
      print(deck.deal())

if __name__ == "__main__":
   main()
