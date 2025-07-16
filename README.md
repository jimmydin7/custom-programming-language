![GitHub Clones](https://img.shields.io/badge/GitHub%20Clones-84-blue?logo=github&style=for-the-badge)
![GitHub Visitors](https://img.shields.io/badge/GitHub%20Visitors-341-brightgreen?logo=github&style=for-the-badge)
# Custom Programming Language
**View demo & docs [here](https://jimmydin7.github.io/custom-programming-language/docs)**

A simple programming language built from scratch in Python.  
Includes full lexer (tokenizer), parser, and interpreter (no real-world senario, just educational)
This version supports basic features like:


- Variable declarations (with `int` and `string` types)
- Printing output using `say()`
- Comment support (`#` for single-line comments)
- Debug Mode to see tokenizing and parsing happen in real time
- Repeat blocks for simple loops (`repeat x { ... }`)
- Arithmetic operators in expressions (`+`, `-`, `*`, `/`)
- If statements for conditional execution (`if ... { ... }`)

---

## Example Code

```plaintext
# Print
say("Hello, world!")

# Define a string
myname = string("Alex")

# Define an integer
mynumber = int(42)

# Output the values
say(myname)
say(mynumber)

# Repeat block demo
repeat 3 {
    say("hi!")
}

# Arithmetic operators demo
minutes_in_a_day = int(60 * 24)
say(minutes_in_a_day)

sum = int(5 + 3)
say(sum)

complex = int((2 + 3) * 4 - 6 / 2)
say(complex)

# If statement demo
minutes = int(60 * 24)
if minutes > 100 {
    say("there are more than 100 minutes in a day!")
}

# If with equality
x = int(5)
if x == 5 {
    say("x is five!")
}
```

---

## How to Run

1. have **Python 3.x** installed
2. clone the repository
3. add your code to a `.txt` file
4. run the python file and add your source code's path as an argument
   ```bash
   python run.py sourcecode.txt
   ```

---

## Features

- [x] Integer & string variables
- [x] Print with `say()`
- [x] Comments (`#`)
- [x] Tokenizer and AST
- [x] Repeat blocks (`repeat x { ... }`)
- [x] Arithmetic operators in expressions
- [x] If statements for conditional execution
- [x] Expressions / math
- [ ] Error handling (improved)
- [ ] Functions
- [ ] Arguments on functions
