import sys

transition = {'state_0': {'digit': 'state_1', 'operation': 'state_2', 'whitespace': 'state_3', 'other': 'state_e'}, 
              'state_1': {'digit': 'state_1', 'operation': 'state_e', 'whitespace': 'state_e', 'other': 'state_e'},
              'state_2': {'digit': 'state_e', 'operation': 'state_e', 'whitespace': 'state_e', 'other': 'state_e'},
              'state_3': {'digit': 'state_e', 'operation': 'state_e', 'whitespace': 'state_3', 'other': 'state_e'}}

word_type = {'state_0': 'invalid', 'state_1': 'UINT_LITERAL', 'state_2': 'OPERATION', 'state_3': 'WHITESPACE', 'state_e': 'invalid'}

char_type = {'0': 'digit', '1': 'digit', '2': 'digit', '3': 'digit', '4': 'digit', '5': 'digit', '6': 'digit', '7': 'digit', '8': 'digit', '9': 'digit',
             '+': 'operation', '-': 'operation', '*': 'operation',
             ' ': 'whitespace',
             '\0': 'other'}

class Lexeme:
    def __init__(self, word_type, word):
        self.type = word_type
        self.word = word

    def __str__(self):
        return "(" + self.type + ", " + self.word + ")"

class Scanner:
    def __init__(self, in_string, transition, word_type, char_type):
        self.i = 0
        self.transition = transition
        self.word_type = word_type
        self.s = in_string
        self.char_type = char_type

    def next_char(self):
        try:
            c = (self.s)[self.i]
        except IndexError:
            return '\0'
        finally:
            self.i += 1
        return c

    def next_lexeme(self):
        print('initializing...')
        lexeme = ''
        stack = []
        c = self.next_char()
        if c == '\0':
            print('reached end of input string, ending lexeme hunt')
            raise IndexError('Reached end of input string')
        lexeme += c
        c_type = char_type[c]
        state = transition['state_0'][c_type]
        print('s:', self.s, ', lexeme:', lexeme, ', c:', c, ', state:', state)

        print('constructing lexeme...')
        while state != 'state_e' and c != '\0':
            if word_type[state] == 'invalid':
                stack.append(state)
            else:
                stack = [state]
            c = self.next_char()
            lexeme += c
            c_type = char_type[c]
            state = transition[state][c_type]
            print('lexeme:', lexeme, ', c:', c, ', state:', state)
        
        print('rolling back...')
        lexeme_list = list(lexeme)
        while word_type[state] == 'invalid':
            self.i -= 1
            _ = lexeme_list.pop()
            state = stack.pop()
            print('i:', self.i, 'state:', state)

        return Lexeme(word_type[state], ''.join(lexeme_list))

try:
    s = sys.argv[1]
    scanner = Scanner(s, transition, word_type, char_type)
    lexemes = []
    while True:
        try:
            lexemes.append(scanner.next_lexeme())
        except IndexError:
           break
        for lexeme in lexemes:
            print(lexeme)
except IndexError:
    print("Error: no input string")
