'''
Created on Oct 18, 2018

@author: ekinkade20
'''
inputedString=input("Please enter a string:")
startIndex=int(input("Enter the index where you would like to start slicing:"))
endIndex=int(input("Enter the index where you would like to stop slicing:"))
characterIndex=int(input("Enter the index of the character you would like to access:"))
slicedString=inputedString[startIndex:endIndex]
singleCharacter=inputedString[characterIndex]
print("Original String:",inputedString)
print("Length of Original String:",len(inputedString))
print("Substring from index",startIndex,"to index",endIndex,":",slicedString)
print("Character at index",characterIndex,":",singleCharacter)