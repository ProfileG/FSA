import FSA
import State
import Path

class Parser():

    def __init__(self):
        self.alphabet = []
        self.states = []
        self.final_states = []
        self.initial_state = None

    #
    # General method for creating FSA*
    #
    def build_machine(self):
        machine = FSA()
        machine.states = self.states
        machine.alphabet = self.alphabet
        machine.final_states = self.final_states
        machine.initial_state = self.initial_state
        return machine

    def set_initial_state(self,initial_state):
        self.initial_state = self.get_state(initial_state)


    def set_final_states(self, set_of_final_states):
        for state in set_of_final_states.split(","):
            self.final_states.append(State(state))

    def set_state(self, set_of_states):
        for state in set_of_states.split(","):
            self.states.append(State(state))

    def set_alphabet(self, alphabet):
        for code in alphabet.split(","):
            self.alphabet.append(code)

    def get_state(self,statement):
        for element in self.states:
        #...
            if(statement == element.get_statement()):
                return element
        #...
        return None

    #Parsing a string with the definition of the routes from the states
    def parsing_expression(self, code):
        block = code.split("->")
        # @q0(a)... -> is defined as...
        code_of_initial_state_with_code_of_road = block[0]
        code_of_initial_state = code_of_initial_state_with_code_of_road.split("(")[0]
        code_of_final_state = self.get_state(block[1])
        code_of_road = code_of_initial_state_with_code_of_road.split("(")[1]
        # ... also remove the final elemenet @))
        code_of_road = code_of_road.strip(")")
        # ...
        initial_state = self.get_state(code_of_initial_state)
        initial_state.add_path(code_of_road, code_of_final_state)
        return initial_state

    def set_of_transiton(self,expression):
        for code in expression.split(","):
            #for instance, need to parse the following line @q0(a)->
            self.parsing_expression(code)
