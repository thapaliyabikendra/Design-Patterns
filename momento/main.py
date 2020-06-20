from editor import Editor
from history import History

e = Editor()
h = History()

e.set_content("A")
h.push(e.create_state())
e.set_content("B")
h.push(e.create_state())
e.set_content("C")
h.push(e.create_state())

e.restore_state(h.pop())
e.restore_state(h.pop())

print(e.get_content())

