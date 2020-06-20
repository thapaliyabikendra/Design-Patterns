class Canvas:

    def mouse_down(self):
        self.current_tool.mouse_down()

    def mouse_up(self):
        self.current_tool.mouse_up()


    def get_current_tool(self):
        return self.current_tool
    
    def set_current_tool(self, current_tool):
        self.current_tool = current_tool
