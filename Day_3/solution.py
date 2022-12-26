from string import ascii_lowercase, ascii_uppercase

class Rucksacks():
    def __init__ (self):
        self.rucksackItems = self.seeItems()
        self.charCode = self.charToNum()
    
    def seeItems(self):
        rucksackItems = []
        with open('input.txt', 'r') as rucksacks:
            for items in rucksacks:
                rucksackItems.append(items.strip())

        return rucksackItems
    
    def checkFirstInSecond(self, first, second):
        itemsMatched = []
        for item in first:
            if item in second and item not in itemsMatched:
                itemsMatched.append(item)
        
        return itemsMatched


    def charToNum(self):
        charCodes = {}
        upperCaseCode = 27

        for char in range(len(ascii_lowercase)):
            charCodes[ascii_lowercase[char]] = char + 1
            charCodes[ascii_uppercase[char]] = upperCaseCode

            upperCaseCode += 1

        return charCodes
    

    def itemCount(self, chars):
        itemValue = 0
        for char in chars:
            if char in self.charCode.keys():
                itemValue += self.charCode[char]

        return itemValue





    def analyzeItems(self):
        itemsTotal = 0
        for items in self.rucksackItems:
            firstHalf = items[:len(items)//2]
            secondHalf = items[len(items)//2:]

            itemsMatched = self.checkFirstInSecond(firstHalf, secondHalf);
            itemsTotal += self.itemCount(itemsMatched)
        
        return itemsTotal

            
            
            
            


rucksacks = Rucksacks()
print(rucksacks.analyzeItems())