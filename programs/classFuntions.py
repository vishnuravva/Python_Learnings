class testClass:
    def __init__(self):
        self.str = ""
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())


obj = testClass()
obj.getString()
obj.printString()