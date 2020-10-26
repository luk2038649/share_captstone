class ModelClass():
    ERROR_MSG = "Error"
    #stupid functions to prove me can use business logic on our widgets?
    #All return strings
    def timesTwo(self, x):
        returnVal = self.ERROR_MSG
        try:
            returnVal = str(x*2)
        except Exception:
            pass
        return returnVal
        
    def plusTwo(self, x):
        returnVal = self.ERROR_MSG
        try:
            returnVal = str(x+2)
        except Exception:
            pass
        return returnVal
        
    def minusTwo(self, x):
        returnVal = self.ERROR_MSG
        try:
            returnVal = str(x-2)
        except Exception:
            pass
        return returnVal
