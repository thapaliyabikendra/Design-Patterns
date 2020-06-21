class Strategy:
    def __init__(self, func=None):
        self.name = "Default Strategy"
        if func:
            self.execute = func

    def execute(self):
        print(self.name)

def strategy_one():
    print("First Strategy is used to execute method 1")

def strategy_two():
    print("Two Strategy is used to execute method 1")


s0 = Strategy()
s0.execute()

s1 = Strategy(strategy_one)
s1.name = "First Strategy"
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Two Strategy"
s2.execute()