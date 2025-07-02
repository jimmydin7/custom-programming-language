# Custom Programming Language

A simple programming language built from scratch in Python.  
Includes full lexer (tokenizer), parser, and interpreter
This version supports basic features like:

- Variable declarations (with `int` and `string` types)
- Printing output using `say()`
- Comment support (`#` for single-line comments)
- Debug Mode to see tokenizing and parsing happen in real time

---

## Example Code

```plaintext
# Define a string
myname = string("Alex")

# Define an integer
mynumber = int(42)

# Output the values
say(myname)
say(mynumber)
```

---

## How to Run

1. have **Python 3.x** installed
2. clone the repository
3. add your code to a `.txt` file and specify it's path on main.py `source_code_path` variable
   ```bash
   python main.py
   ```

---

## Features

- [x] Integer & string variables
- [x] Print with `say()`
- [x] Comments (`#`)
- [x] Tokenizer and AST
- [ ] Error handling (improved)
- [ ] Expressions / math
- [ ] Control flow (`if`, `while`, etc.)

---

## Planned for Future Versions

- Arithmetic operations (`+`, `-`, etc.)
- Conditionals (`if`, `else`)
- Loops (`while`, `for`)
- Functions
- Type checking
- Custom runtime errors

---

## Why?

This is a learning project to understand how programming languages work (tokenizing, parsing, interpreting)

---