# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jonathan Samuel
# Section:		510
# Assignment:	Lab7b
# Date:         10/11/18
def wordChanger(word):
    vowels = ["a", "e", "i", "o", "u", "y"]
    for i, c in enumerate(vowels):
        if word[0] == c:
            return word + "yay"
        else:
            return word[1:] + word[0] + "ay"


def convertWord():
    word = "go"
    while word != "stop":
        word = input("Enter in word")
        print(wordChanger(word))


def convertSentence():
    sentence = "go"
    while sentence != "stop":
        sentence = input("Enter in sentence")
        sentenceList = sentence.split(" ")
        sentence = ""
        for i, c in enumerate(sentenceList):
            sentence = sentence + wordChanger(c) + " "

        print(sentence[:len(sentence) - 1])


choose = input("If you want to do words type \"word\" and if you want to do sentence type \"sentence\"")
if choose == "word":
    convertWord()
else:
    convertSentence()
