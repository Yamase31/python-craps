"""
Author: Beth Ann Townsend and James Lawson
File: wargame.py
Project 10

Simulates a game of the card game War.
"""

from cards import Deck

class WarGame(object): #this what makes the game
    def __init__(self): #initializes with the necessary components: two players, the war pile, the game's state, and the deck of cards
        self.player1 = Player()
        self.player2 = Player()
        self.warPile = []
        self.gameState = ""
        self.deck = Deck()
        self.deck.shuffle()

    def __str__(self): #returns the string of the game state
        return self.gameState

    def deal(self): #splits the deck in half, dealing out 26 cards to each player
        while not self.deck.isEmpty(): #checks if game is over
            self.player1.addToUnplayedPile(self.deck.deal())
            self.player2.addToUnplayedPile(self.deck.deal())

    def step(self): #"steps" through the game, returning the two cards that were played each time
        card1 = self.player1.getCard()
        card2 = self.player2.getCard()
        self.warPile.append(card1)
        self.warPile.append(card2)
        self.gameState = "Player 1: " + str(card1) + "\n" +\
                         "Player 2: " + str(card2)
        #runs through each possibility
        if card1.rank == card2.rank:
            self.gameState += "\nCards added to War pile\n"
        elif card1.rank > card2.rank:
            self.transferCards(self.player1)
            self.gameState += "\nCards go to Player 1"
        else:
            self.transferCards(self.player2)
            self.gameState += "\nCards go to Player 2"
        return (card1, card2)

    def transferCards(self, player): #moves war pile to the winning player's winning pile
        while len(self.warPile) > 0:
            player.addToWinningsPile(self.warPile.pop())

    def winner(self):
        #once there is a winner, as defined below, a string is returned to say who won and how
        if self.player1.isDone() or self.player2.isDone():
            count1 = self.player1.winningsCount()
            count2 = self.player2.winningsCount()
            if count1 > count2:
                return "Player 1 wins, " + str(count1) + " to " +\
                       str(count2) +"!"
            elif count2 > count1:
                return "Player 2 wins, " + str(count2) + " to " +\
                       str(count1) +"!"
            #accounts for a tie
            else:
                return "The game ends in a tie!\n"
        #doesn't do anything when there isn't a winner
        else:
            return None

class Player(object): #this class represents a player
    def __init__(self): #initializes the card piles, the unplayed cards and the won cards
        self.playerUnplayed = []
        self.winningsPile = []

    def __str__(self): #returns a string announcing the winning pile of the player
        return str(self.winningsPile)

    def addToUnplayedPile(self, card): #moves card to the unplayed pile for the player
        self.playerUnplayed.append(card)

    def addToWinningsPile(self, card): #moves card to the winnings pile for the player
        self.winningsPile.append(card)
    
    def getCard(self): #essentially pulls a card from the player's unplayed pile to play
        return self.playerUnplayed.pop(0)

    def isDone(self): #turns True if an unplayed pile is empty, but False when not
        if len(self.playerUnplayed) == 0:
            return True
        else:
            return False

    def winningsCount(self): #returns the number in the winnings pile
        return len(self.winningsPile)
