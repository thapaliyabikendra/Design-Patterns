from editorstate import EditorState

class Editor:
    def set_content(self, content: str):
        self.content = content

    def get_content(self) -> str:
        return self.content

    def create_state(self):
        return EditorState(self.content)
    
    def restore_state(self, state):
        self.content = state.get_content()
        