class string:
    def __init__(self):
        self.word=""
    def uppercase(self):
        self.word=input("Enter the word")
        print(self.word.upper())

obj=string()
obj.uppercase()

