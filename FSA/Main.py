import Parser
import Path
import State
import FSA


def validation_of_the_file(text):

    # ... remove not needed elements
    remove_code = "{}"

    for i in remove_code:
        text = text.replace(i, "")

    return text

def parse_of_file(input,output):

    the_number_of_the_processed = 1


    #Open the file for parsing input data
    input = open(input)
    text = input.read()
    text = validation_of_the_file(text)

    #Divide the text lines for subsequent analysis
    lines = text.split("\n");

    #Create a file to write the results
    output = open(output, "w")
    output.write("VadimGilemzyanov\n")

    #Define how many machines you need to create
    count_of_machines = int(lines[0])
    i = 0;

    while(i<count_of_machines):
        i += 1
        output.write(str(i)+"\n");

        # Create a FSA and recording the results
        machine = parse_machine(lines,the_number_of_the_processed)
        writing_results(lines,the_number_of_the_processed +5 ,machine,output)

def parse_machine(lines,n):
    parser = Parser()
    parser.set_state(lines[n])
    parser.set_alphabet(lines[n+1])
    parser.set_initial_state(lines[n+2])
    parser.set_final_states(lines[n+3])
    parser.set_of_transiton(lines[n+4])
    return parser.build_machine()

def writing_results(lines,n,machine,output):

    #Determine the number of tests for this machine
    count_of_words = int(lines[n])

    for i in range(n,n+count_of_words):

        #Recorded the result
        output.write(machine.running(lines[i+1])+"\n")
        n += n+count_of_words;

parse_of_file("input.txt", "output.txt")