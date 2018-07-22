__author__ = "Linux Yaz Kampı Django Sınıfı"
__license__ = ""
"""
Try Our Luck With 3 Option!

Description: 
This module functions returns a lot of lucky games

Options:
Dice Roll
Head&Tail
Rock&Paper&scissors

Simple Usage:

o = olasilik()
o.dice_roll() # For Dice Roll
o.head_tail() # For Head Tail
o.rock_paper_scissors # for Rock&Paper&Scissors
"""
from random import choice
class olasilik:
    def dice_roll(self):
        return choice(range(6))

    def head_tail(self):
        return choice("Head","Tail")

    def rock_paper_scissors(self):
        return choice(["Rock","Paper","Scissors"])

    def roller(self):
        return self.dice_roll()