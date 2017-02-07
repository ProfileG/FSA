import State
import FSA

class Path:

    def __init__(self,code,target):
        self.code = code
        self.target = target

    # Method the method of determining the nearest opposite @State
    def get_target(self):
        return self.target
