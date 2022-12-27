class SectionPairs():
    def __init__(self):
        self.sectionPairs = self.getSectionPairs()
    
    def getSectionPairs(self):
        sectionPairs = []
        with open('input.txt') as Pairs:
            for pair in Pairs:
                sectionPairs.append(pair.strip())
        
        return sectionPairs
    
    def rangeToList(self, sectionRange):
        start, end = sectionRange.split('-')
        start, end = int(start), int(end)
        
        rangeList = []
        for section in range(start, end + 1):
            rangeList.append(section)

        return rangeList

    def checkFaultyPairs(self, a, b):
        if len(a) < len(b):
            a, b = b, a
        
        for section in b:
            if section in a:
                return True
        return False

    def countFaultyPairs(self):
        faultyCount = 0
        for pair in self.sectionPairs:
            pair_a, pair_b = pair.split(',')
            pair_a, pair_b = self.rangeToList(pair_a), self.rangeToList(pair_b)
            
            if self.checkFaultyPairs(pair_a, pair_b):
                faultyCount += 1
        
        return faultyCount

            



solution = SectionPairs()
print(solution.countFaultyPairs())