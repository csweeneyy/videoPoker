"""
Author: Evan and Connor
File: poker_gui.py
Project 11
GUI for the 5 Card Draw Poker Game
"""

from tkinter import PhotoImage, font
from breezypythongui import EasyFrame
from cards import Card, Deck
from poker_calc import *
import json
import os

class PokerGui(EasyFrame):    
    def __init__(self):
        EasyFrame.__init__(self, width=1500, height=500)
        c_font = font.Font(family="courier", size=20)
        self.moneyLabel = self.addLabel("Cash: $" + str(0), 0 , 0)
        self.totalHandsLabel = self.addLabel("Total Hands: " + str(0), 0, 1)
        
        self.startGameButton = self.addButton("Start Game", 1, 0, command = self.startGame)
        self.newHandButton = self.addButton("New Hand", 1, 1, command = self.newHand)
        self.exchangeCardsButton = self.addButton("Exchange Cards", 1, 2, command = self.turn)
        self.endGameButton = self.addButton("End Game", 1, 3, command = self.endGame)
        self.highScoreButton = self.addButton("High Scores", 1, 4, command = self.highScore)
        
        self.blueBackCard = PhotoImage(file = "card_images/blue_back.gif", )
        self.card1Label = self.addLabel("", 2, 0)
        self.card1Label['image'] = self.blueBackCard
        self.card2Label = self.addLabel("", 2, 1)
        self.card2Label['image'] = self.blueBackCard
        self.card3Label = self.addLabel("", 2, 2)
        self.card3Label['image'] = self.blueBackCard
        self.card4Label = self.addLabel("", 2, 3)
        self.card4Label['image'] = self.blueBackCard
        self.card5Label = self.addLabel("", 2, 4)
        self.card5Label['image'] = self.blueBackCard
        self.card1Label.bind("<Button-1>", self.card1Click)
        self.card2Label.bind("<Button-1>", self.card2Click)
        self.card3Label.bind("<Button-1>", self.card3Click)
        self.card4Label.bind("<Button-1>", self.card4Click)
        self.card5Label.bind("<Button-1>", self.card5Click)

        self.exchangeCardsButton.config(state="disabled")
        self.newHandButton.config(state="disabled")
        self.endGameButton.config(state="disabled")
        

        self.highScores = {}
        self.newDict = {}   

        
    def card1Click(self, e):
        if self.click1 == 1:
            self.cardImage1 = PhotoImage(file = self.cardString(self.card1.suit, self.card1.rank))
            self.card1Label['image'] = self.cardImage1
            self.click1 = -1
        elif self.click1 == 0:
            return None
        else:
            self.cardImage1 = PhotoImage(file = self.invertedCardString(self.card1.suit, self.card1.rank))
            self.card1Label['image'] = self.cardImage1
            self.click1 = 1 
       
    def card2Click(self, e):
        if self.click2 == 1:
            self.cardImage2 = PhotoImage(file = self.cardString(self.card2.suit, self.card2.rank))
            self.card2Label['image'] = self.cardImage2
            self.click2 = -1
        elif self.click2 == 0:
            return None
        else:
            self.cardImage2 = PhotoImage(file = self.invertedCardString(self.card2.suit, self.card2.rank))
            self.card2Label['image'] = self.cardImage2
            self.click2 = 1

    def card3Click(self, e):
        if self.click3 == 1:
            self.cardImage3 = PhotoImage(file = self.cardString(self.card3.suit, self.card3.rank))
            self.card3Label['image'] = self.cardImage3
            self.click3 = -1
        elif self.click3 == 0:
            return None
        else:
            self.cardImage3 = PhotoImage(file = self.invertedCardString(self.card3.suit, self.card3.rank))
            self.card3Label['image'] = self.cardImage3
            self.click3 = 1

    def card4Click(self, e):
        if self.click4 == 1:
            self.cardImage4 = PhotoImage(file = self.cardString(self.card4.suit, self.card4.rank))
            self.card4Label['image'] = self.cardImage4
            self.click4 = -1
        elif self.click4 == 0:
            return None
        else:
            self.cardImage4 = PhotoImage(file = self.invertedCardString(self.card4.suit, self.card4.rank))
            self.card4Label['image'] = self.cardImage4
            self.click4 = 1

    def card5Click(self, e):
        if self.click5 == 1:
            self.cardImage5 = PhotoImage(file = self.cardString(self.card5.suit, self.card5.rank))
            self.card5Label['image'] = self.cardImage5
            self.click5 = -1
        elif self.click5 == 0:
            return None
        else:
            self.cardImage5 = PhotoImage(file = self.invertedCardString(self.card5.suit, self.card5.rank))
            self.card5Label['image'] = self.cardImage5
            self.click5 = 1
            
    def startGame(self):
        self.cash = 100
        self.totalHands = 0
        self.moneyLabel.config(text = "Cash: $" + str(self.cash))
        self.totalHandsLabel.config(text = "Total Hands: " + str(self.totalHands))
        self.blueBackCard = PhotoImage(file = "card_images/blue_back.gif", )
      
        self.card1Label['image'] = self.blueBackCard
       
        self.card2Label['image'] = self.blueBackCard
       
        self.card3Label['image'] = self.blueBackCard
       
        self.card4Label['image'] = self.blueBackCard
     
        self.card5Label['image'] = self.blueBackCard

        
        self.newHandButton.config(state="normal")
        self.endGameButton.config(state="disabled")
        self.exchangeCardsButton.config(state="disabled")
        self.startGameButton.config(state="disabled")

        #self.click1 = False
        

    def newHand(self):
        self.cash -= 10
        self.moneyLabel.config(text = "Cash: $" + str(self.cash))
        self.totalHands += 1
        self.totalHandsLabel.config(text = "Total Hands: " + str(self.totalHands))
        self.exchangeCardsButton.config(state="normal")
        
        
        self.d = Deck()
        self.d.shuffle()
        self.card1 = self.d.deal()
        self.cardImage1 = PhotoImage(file = self.cardString(self.card1.suit, self.card1.rank))
        self.card1Label['image'] = self.cardImage1

        self.card2 = self.d.deal()
        self.cardImage2 = PhotoImage(file = self.cardString(self.card2.suit, self.card2.rank))
        self.card2Label['image'] = self.cardImage2

        self.card3 = self.d.deal()
        self.cardImage3 = PhotoImage(file = self.cardString(self.card3.suit, self.card3.rank))
        self.card3Label['image'] = self.cardImage3


        self.card4 = self.d.deal()
        self.cardImage4 = PhotoImage(file = self.cardString(self.card4.suit, self.card4.rank))
        self.card4Label['image'] = self.cardImage4

        self.card5 = self.d.deal()
        self.cardImage5 = PhotoImage(file = self.cardString(self.card5.suit, self.card5.rank))
        self.card5Label['image'] = self.cardImage5

        self.Hand = [self.card1, self.card2, self.card3, self.card4, self.card5]
        self.exchangeCardsButton.config(state="normal")
        self.endGameButton.config(state="normal")

        self.click1 = -1
        self.click2 = -1
        self.click3 = -1
        self.click4 = -1
        self.click5 = -2

        if self.cash <= 0:
            self.newHandButton.config(state="disabled")
        
    def turn(self):
        if self.click1 == 1:
            self.Hand.pop(0)
            self.card1 = self.d.deal()
            self.Hand.insert(0, self.card1)
            self.cardImage1 = PhotoImage(file = self.cardString(self.card1.suit, self.card1.rank))
            self.card1Label['image'] = self.cardImage1
            self.click1 = -1
        else:
            pass
            
        if self.click2 == 1:
            self.Hand.pop(1)
            self.card2 = self.d.deal()
            self.Hand.insert(1, self.card2)
            self.cardImage2 = PhotoImage(file = self.cardString(self.card2.suit, self.card2.rank))
            self.card2Label['image'] = self.cardImage2
            self.click2 = -1
        else:
            pass

        if self.click3 == 1:
            self.Hand.pop(2)
            self.card3 = self.d.deal()
            self.Hand.insert(2, self.card3)
            self.cardImage3 = PhotoImage(file = self.cardString(self.card3.suit, self.card3.rank))
            self.card3Label['image'] = self.cardImage3
            self.click3 = -1
        else:
            pass

        if self.click4 == 1:
            self.Hand.pop(3)
            self.card4 = self.d.deal()
            self.Hand.insert(3, self.card4)
            self.cardImage4 = PhotoImage(file = self.cardString(self.card4.suit, self.card4.rank))
            self.card4Label['image'] = self.cardImage4
            self.click4 = -1
        else:
            pass

        if self.click5 == 1:
            self.Hand.pop(4)
            self.card5 = self.d.deal()
            self.Hand.insert(4, self.card5)
            self.cardImage5 = PhotoImage(file = self.cardString(self.card5.suit, self.card5.rank))
            self.card5Label['image'] = self.cardImage5
            self.click5 = -1
        else:
            pass

        self.handValue = hand_ranker(self.Hand)
        if self.handValue == 0:
            self.messageBox(title = "Lost!", message = "You didn't earn any money on this hand.")
        elif self.handValue == 1 :
            self.messageBox(title = "Earned!", message = "You earned $10 on this hand with a pair!")
        elif self.handValue == 2:
            self.messageBox(title = "Earned!", message = "You earned $20 on this hand with a Two pair!")
        elif self.handValue == 3:
            self.messageBox(title = "Earned!", message = "You earned $30 on this hand with a Three of a kind!")
        elif self.handValue == 4:
            self.messageBox(title = "Earned!", message = "You earned $40 on this hand with a Straight!")
        elif self.handValue == 6:
            self.messageBox(title = "Earned!", message = "You earned $60 on this hand with a Flush!")
        elif self.handValue == 9:
            self.messageBox(title = "Earned!", message = "You earned $90 on this hand with a Full House!")
        elif self.handValue == 25:
            self.messageBox(title = "Earned!", message = "You earned $250 on this hand with a Four of a kind!")
    
        
        self.cash = self.cash + 10 * self.handValue
        self.moneyLabel.config(text = "Cash: $" + str(self.cash))
        self.exchangeCardsButton.config(state="disabled")
        
        if self.cash <= 0:
            self.exchangeCardsButton.config(state="disabled")
            self.messageBox(title = "Out of Money!", message = "You are out of money!")
        else:
            self.newHandButton.config(state="normal")
        
    
    def endGame(self):
        self.messageBox(title = "Game Over", message = f"Your ending money amount was {self.cash}.")
        self.scoreName = self.prompterBox(title = "Name", promptString = "Please input your name.", inputText = "")
        
        self.score = self.cash
        
        
        
        if os.path.isfile("highScores"):
            fileObj = open('highScores', 'r')
            self.newDict = json.load(fileObj)
        else:
            pass

       
        fileObj = open('highScores', 'w')
    
        if len(self.newDict) == 0:
            self.highScores[self.scoreName] = self.score
            json.dump(self.highScores, fileObj)
        else:
            
            self.highScores = self.newDict
            b = self.highScores.get(self.scoreName, None)
            #print(b)
            if b != None:                                   #if the player name is the same, takes the highest score
                if self.score > int(b):
                    self.highScores.update({self.scoreName : self.score})
            else:
                self.highScores.update({self.scoreName : self.score})
            json.dump(self.highScores, fileObj)
      
    
        
        fileObj.close()
        




    
        self.exchangeCardsButton.config(state="disabled")
        self.newHandButton.config(state="disabled")
        self.endGameButton.config(state="disabled")
        self.startGameButton.config(state="normal")

        self.click1 = 0
        self.click2 = 0
        self.click3 = 0
        self.click4 = 0
        self.click5 = 0
        

    def cardString(self, suit, rank):
        if rank == 11:
            rank = 'jack'
        elif rank == 12:
            rank = 'queen'
        elif rank == 13:
            rank = 'king'
        elif rank == 1:
            rank = 'ace'
        return f"card_images/{suit.lower()}_{rank}.gif"
    
    def invertedCardString(self, suit, rank):
        if rank == 11:
            rank = 'jack'
        elif rank == 12:
            rank = 'queen'
        elif rank == 13:
            rank = 'king'
        elif rank == 1:
            rank = 'ace'
        return f"inverted_card_images/{suit.lower()}_{rank}.gif"



    def highScore(self):

        if os.path.isfile("highScores"):
            fileObj = open('highScores', 'r')
            self.newDict = json.load(fileObj)
        else:
            pass

        self.Lyst = sorted(self.newDict.items(), key=lambda x:x[1], reverse = True)

        if len(self.Lyst) > 5:
            y = len(self.Lyst) - 5
            for x in range(y):
                self.Lyst.pop()
        else:
            pass
                    
        printedString = ""
        for name, score in self.Lyst:
            printedString += name + ": $" + str(score) + "\n"
    
 
        self.messageBox(title = "High Scores", message = printedString)


    
if __name__ == "__main__":
    PokerGui().mainloop()
