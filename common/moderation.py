#Copyright Devin B (Azura4k) 2022, ALL RIGHTS RESERVED
#Use this for moderation actions
from difflib import SequenceMatcher
from email.message import Message
from re import L
from typing import List
from common.tools import Tools as tools


class Moderation():
    def __init__(self, WordMatchThreshold):
        self.ListOfBannedWords = ["nigger", "coon", "faggot", "kys","fag", "c00n"]
        self.ListOfBannedPhrases = ["kill your self"]
        self.ListOfExceptionWords = ["raccoon", "cocoon"]
        self.Threshold = float(WordMatchThreshold)

    #Returns true if word is safe, returns false if word is banned.
    def SafeMsgWordScanner(self, message):
        message = str(message).lower()
        #WORD SCANNER
        for word in message.split():
            for bannedword in self.ListOfBannedWords:
                if SequenceMatcher(None, word, bannedword).ratio() >= self.Threshold:
                    #If exception is found, returns true, else, returns false
                    if self.WordExceptionChecker(word) == False:
                        return False
                else:
                    pass
        #Return True if there is no banned word found
        return True

    #Returns True if Bad Word Found, Returns False if no bad word is found
    def SafeMsgSequenceScanner(self, message):
        
        message = str(message).lower()
        
        #Removes excempted words for processing
        message = self.MessageExemptionScissors(message)
        #Check for every banned word
        for word in self.ListOfBannedWords:
            #Used for sequence counter counter
            i = int(0)
            CompiledWord = str()
            for letter in message:
                try:
                    if letter == word[i]:
                        i += 1
                        CompiledWord = CompiledWord + letter
                except IndexError:
                    pass
            #Assuming that a bad word is already found, call Msg scanner to match word and return false. Puts word to threshold
            if self.SafeMsgWordScanner(CompiledWord) == False:
                return False
        #If no sequences match, return true 
        return True
            
    #Check for Word Exceptions, automatically assume false                
    def WordExceptionChecker(self, Word):
        Word = str(Word).lower()
        for exceptionword in self.ListOfExceptionWords:
        #If word does not equal a single exception, banish it
            if Word == exceptionword:
                return True
        #Using not for compatability, so Exception can be readable
        return False

    def MessageExemptionScissors(self, message):
        message = str(message).lower()
        for ExemptWord in self.ListOfExceptionWords:
            #Used for sequence counter counter
            i = int(0)
            CompiledWord = str()
            for letter in message:
                try:
                    if letter == "": 
                        pass
                    elif letter == ExemptWord[i]:
                        i += 1
                        CompiledWord += letter
                except IndexError:
                    pass
            if CompiledWord == ExemptWord:
                tempmessage = message
                #Removes All Spaces
                for i in range(0, len(message)):
                    try:
                        if message[i] == " ":
                            message = message.replace(" ","", i)
                    except IndexError:
                        pass
                message = message.replace(CompiledWord, '')
        return message