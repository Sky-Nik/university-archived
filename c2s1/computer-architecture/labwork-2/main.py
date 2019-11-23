# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 01:47:26 2017

@author: Nikita
"""
# global constants, built-in settings of processor
reg_size = 24
int_max = 2**reg_size
byte_size = 8
max_byte = 2**byte_size

# the Stack, our working space
Stack = []

# all our registers
Memory = {'IR' : '',
          'PS' : '+',
          'PC' : 0,
          'TC' : 0,
          'R0' : 0,
          'R1' : 0,
          'R2' : 0,
          'R3' : 0,
          #'R4' : 0,'R5' : 0,'R6' : 0,'R7' : 0,'R8' : 0,'R9' : 0
          }


def add():
    """ adds two upper elements of the Stack """
    Memory['PS'] = '+' if Stack[-1] + Stack[-2] >= 0 else '-'
    Stack[-1] = (Stack.pop() + Stack[-1]) % int_max
    Memory['TC'] += 1


def substract():
    """ substacts two upper elements of the Stack """
    Memory['PS'] = '+' if Stack[-1] - Stack[-2] >= 0 else '-'
    Stack[-1] = (Stack.pop() - Stack[-1]) % int_max
    Memory['TC'] += 1


def divide():
    """ divides two upper elements of the Stack """
    if Stack[-2] == 0:
        raise ValueError('Cannot divide by 0')
    Memory['PS'] = '+' if Stack[-1] // Stack[-2] >= 0 else '-'
    Stack[-1] = (Stack.pop() // Stack[-1]) % int_max
    Memory['TC'] += 1


def multiply():
    """ multiplies two upper elements of the Stack """
    Memory['PS'] = '+' if Stack[-1] * Stack[-2] >= 0 else '-'
    Stack[-1] = (Stack.pop() * Stack[-1]) % int_max
    Memory['TC'] += 1


def pop(reg_name):
    """ pops the top element of the Stack """
    Memory['PS'] = '+' if Stack[-1] >= 0 else '-'
    if reg_name in Memory or reg_name[0] != 'R':
        Memory[reg_name] = Stack.pop()
    else:
        raise NameError('Register with name ' + reg_name + ' does not exist.')
    Memory['TC'] += 1


def push(smth):
    """ pushes smth into the Stack """
    Stack.append(Memory[smth] if smth in Memory else smth)
    Memory['PS'] = '+' if Stack[-1] >= 0 else '-'
    Memory['TC'] += 1


def byte_add(a, b):
    """ adds two integers bytewise """
    La, Lb, Lc = [], [], []

    while len(La) < reg_size // byte_size:
        La.append(a % max_byte)
        a //= max_byte

    while len(Lb) <  reg_size // byte_size:
        Lb.append(b % max_byte)
        b //= max_byte

    for i in range(reg_size // byte_size):
        Lc.append((La[i] + Lb[i]) % max_byte)

    c = 0
    for i in range(reg_size // byte_size - 1, -1, -1):
        c = c * max_byte + Lc[i]


def op16(smth):
    """ dunno what's the purpose of this function """
    Stack[-1] = byte_add(Stack[-1], Memory[smth] if smth in Memory else smth)
    Memory['TC'] += 1


# list of all supported commands
Commands = {'add' : add,
            'sub' : substract,
            'div' : divide,
            'mul' : multiply,
            'pop' : pop,
            'push' : push,
            'op16' : op16} 


def to_bin(n):
    s = ''
    for _ in range(reg_size):
        s = str(n % 2) + s
        n //= 2
    return s


def to_byte(n):
    s = to_bin(n)
    t = s[0:byte_size]
    for i in range(1, reg_size // byte_size):
        t = t + '|' + s[i * byte_size:(i + 1) * byte_size]
    return t


def load(command):
    """ Parses a command """
    Memory['IR'] = command.strip()
    args = command.split()
    func = Commands[args[0]]
    
    val = None
    if len(args) > 1:
        if args[1].isdigit():
            val = int(args[1])
        else:
            val = args[1]
        Memory['PS'] = '+' if (Memory[val] if val in Memory else val) >= 0 else '-'
    Memory['TC'] += 1
    print_state()
    input('')
    return (func, val)

def execute(command):
    """ Executes a command """
    func, val = load(command)
    if val == None:
        func()
    else:
        func(val)
    Memory['PC'] += 1
    print_state()
    input('')

def print_state():
    print('Memory:')
    for register in Memory:
        if register[0] == 'R':
            print('\n', register, to_bin(Memory[register]), end='')
        else:
            print(register, Memory[register], end='\t' if register != 'IR' else '\n')
    print('\nStack:')
    for item in Stack:
        print(to_byte(item))


# driver program
if __name__ == '__main__':
    with open('in.txt') as In:
        for line in In:
            execute(line)
