class getStringUpper:
    def _init_(self):
        self.text = ""
    def getString(self):
        self.text = input("Text:")
    def PrintUpper(self):
        print(self.text.upper())

obj = getStringUpper()
obj.getString()
obj.PrintUpper() 
    