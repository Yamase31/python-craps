"""
Author: Beth Ann Townsend and James Lawson
File: testwar.py
Project 10

Runs a test game to see if wargame is working.
"""

from wargame import WarGame

def main(): #presents a game of war (all at once) for the test
   game = WarGame()
   game.deal()
   while not game.winner():
      game.step()
      print(game)
   print(game.winner())

if __name__ == "__main__":
   main()
