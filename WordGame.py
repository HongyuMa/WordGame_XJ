#################### clean ####################
def clean(bad, phrase):
    ans = ''
    for char in phrase:
        if char in bad:
            ans += ' '
        else:
            ans += char
    return ans
                
#################### wordsByLength ####################
def wordsByLength(phrase):
    word = phrase.split()
    d = {}
    for char in word:
        d.setdefault(len(char),[]).append(char)
    return d

#################### WordGame ####################
class WordGame():
    def __init__(self, word):
        self.w = word.upper()
        self.Right = ''
        self.Wrong = ''
        self.Hint = ''
        self.n = 0
        self.m = ''
    def getSecret(self):
        return (self.w)
    def getHint(self):
        self.Hint = ''
        for char in self.w:
            if char in self.Right:
                self.Hint += char
            else:
                self.Hint += '?'
        self.m = self.Hint
        return self.Hint
    def getRight(self):
        return (self.Right)
    def getWrong(self):
        if
        return (self.Wrong)
    def guess(self,char):
        self.c = char.upper()
        if self.c in self.w:
            if self.c in self.Right:
                pass
            else:
                self.Right += self.c
        else:
            if self.c in self.Wrong:
                pass
            else:
                self.Wrong += self.c
                self.n += 1
    def getState(self):
        self.getHint();
        if "?" not in self.Hint:
            return "won"
        else:
            if self.n >= 6:
                return "lost"
            else:
                return "playing"
                
                
        
        
        
    
        
        
