import Path
import FSA

class State:

    def __init__(self,statement):
        self.targets = []
        self.statement = statement

    def add_path (self, code, state):
        self.targets.append(Path(code,state))

    def change_state (self, code):
        for i in self.targets:
            if (i.code == code):
                return i.get_target()
        return None;

    def get_statement(self):
        return self.statement