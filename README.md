# PythonLexer
A very dumb lexer the author made months ago when reading the second chapter of [a compiler book](https://www.amazon.co.uk/Engineering-Compiler-Keith-Cooper/dp/012088478X). All it knows is simple calculator expressions of the form `\d+\s*[\+-\*/]\s*\d+`. For example, the input "12  + 356" will produce the output `[(UINT_LITERAL, '12'), (OPERATION, '+'), (UINT_LITERAL, 356)]`. The code might be messy to look at (like most Python code written for the purpose of getting something nice on the screen), but it was fun to learn about finite automata :)

## Usage 
``` python3 lexer.py EXPRESSION_TO_LEX ```
