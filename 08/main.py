class Instruction:
    command = ''
    number = ''
    fresh = True
    tried = False
    corrupted = False
    
    
    def __init__(self, command, number):
        self.command = command
        self.number = int(number)


def runProgram(program):
    actualInstruction = 0
    accumulator = 0
    programLastInstructionIndex = len(program)
    
    while True:
        if actualInstruction == programLastInstructionIndex:
            return accumulator
        
        instruction = program[actualInstruction]
        if instruction.fresh is not True:
            # return accumulator # first part of answer
            return None
        
        else:
            instruction.fresh = False
        
        if instruction.command == 'nop':
            if instruction.corrupted is False:
                actualInstruction += 1
            else:
                actualInstruction += instruction.number
        
        
        elif instruction.command == 'jmp':
            if instruction.corrupted is False:
                actualInstruction += instruction.number
            else:
                actualInstruction += 1
        
        elif instruction.command == 'acc':
            accumulator += instruction.number
            actualInstruction += 1
        
        else:
            raise Exception('unknown command')

def runProgramRepairingCommands(program):
    lastCorruptedInstructionIndex = None
    while True:
        # change first possible command to corrupted one
        for i in program:
            if program[i].tried is False:
                program[i].tried = True
                program[i].corrupted = True
                lastCorruptedInstructionIndex = i
                break
        
        result = runProgram(program)
        if result is not None:
            return result
        
        # cleanup from last attempt
        program[lastCorruptedInstructionIndex].corrupted = False
        for i in program:
            program[i].fresh = True


content = open('input.txt', 'r').read()

program = {}
for i, line in enumerate(content.split('\n')):
    command, number = line.split(' ')
    program[i] = Instruction(command, number)

# print(runProgram(program)) # first part of answer
print(runProgramRepairingCommands(program))

# bruteforce was first and obvious solution
# to be faster there will be better to try something like depth-search - try to change every command we hit in run