from string import ascii_lowercase, ascii_uppercase

class Rucksacks():
    def __init__ (self):
        self.rucksackItems = self.seeItems()
        self.charCode = self.charToNum()
        self.groupsOfThree = self.seperateIntoGroups()
    
    def seeItems(self):
        rucksackItems = []
        with open('input.txt', 'r') as rucksacks:
            for items in rucksacks:
                rucksackItems.append(items.strip())

        return rucksackItems
    
    def seperateIntoGroups(self):
        groupsOfThree = []
        group = []

        for i in range(len(self.rucksackItems)):
            if len(group) == 3:
                groupsOfThree.append(group)
                group = []
            
            group.append(self.rucksackItems[i])
            
        groupsOfThree.append(group)
        return groupsOfThree 

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

    def checkBadges(self, group):
        matchedBadge = []

        for char in group[0]:
            if char in group[1] and char in group[2] and char not in matchedBadge:
                matchedBadge.append(char)
    
        return matchedBadge


    def analyzeItems(self):
        totalBadgeValue = 0
        for group in self.groupsOfThree:
            matched = self.checkBadges(group)
            totalBadgeValue += self.itemCount(matched)
        
        return totalBadgeValue

        

            
            
            
            


rucksacks = Rucksacks()
print(rucksacks.analyzeItems())