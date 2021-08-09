"""
Author: Beth Ann Townsend and James Lawson
File: testcraps.py
Project 10

When run, this program tests the crapsgame to ensure it's working properly.
"""

from crapsgame import CrapsGame

def main(): #simulates a game, displaying all the rolls at once for testing purposes
   game = CrapsGame()
   (die1, die2, outcome) = game.step()
   print(game)
   while not outcome:
      (die1, die2, outcome) = game.step()
      print(game)
   print(outcome)

if __name__ == "__main__":
   main()
