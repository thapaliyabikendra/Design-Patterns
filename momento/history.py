class History:
    def __init__(self):
        self.states = []
    def push(self, editor_state):
        self.states.append(editor_state)

    def pop(self):
        self.states.pop()
        return self.states[-1]

