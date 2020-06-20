from tool import Tool

class SelectionTool(Tool):

    def mouse_down(self):
        print("Selection icon")

    def mouse_up(self):
        print("Draw a dash rectangle")