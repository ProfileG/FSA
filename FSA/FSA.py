# Set of states
# Input alphabet
# Initial state
# Set of final state
# Set of transition in the form of @current_state(input_symbol) -> new_state;

import Parser
import Path
import State
import FSA

class FSA:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.final_states = []
        self.initial_state = None


    def check_code(self, code):
        for element in self.alphabet:
            # if the @code is contained in the alphabet, then the @code is valid
            if (code == element):
                return True
        # otherwise, this code is not contained in the alphabet
        return False

    def running(self, line):
        result = ""
        focus = self.initial_state
        # ... first step
        result += focus.get_statement()

        for element in line:
            # validation of data entry and the path exists
            if ( (not self.check_code(element)) or focus == None):
                break

            # change the status of the machine
            next = focus.change_state(element)

            # report on the state of the machine
            if (next != None):
                result += "->" + next.get_statement()
            focus = next

        # ...
        if (self.is_final_state(focus)):
            result = "true:" + result
        else:
            result = "false:" + result
        return result

    # ...
    def is_final_state (self,focus):
        for e in self.final_states:
            if e.get_statement() == focus.get_statement():
                return True
        return False


