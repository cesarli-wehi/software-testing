# Ide Setup

## Installing python

1. The first step is to install `python`, to do so you can visit this link [Python Official Site](https://www.python.org/downloads/) 
2. Make sure to use python version `3.12`, python version 2 has different syntax and the examples given wouldn't work.
3. to test your installation open a `terminal` on mac or `cmd` on windows and type `python` to open the interpreter and it should show you the version. 
   1. On mac sometimes python will come out as an unrecognised command so you will have to type `python3` instead


## Git

Git is a system of version control (think backup and file sharing for code) invented by the god himself mr penguin Torvald. The code for this course will be available on Github which is a free(ish) git hosting service.

Learning to use Git properly is one of the most important things you will ever do, I'll provide a quick guide in the future cause I'm nice that way

[Install Git](https://git-scm.com/)


## installing VS Code

[Install VsCode](https://code.visualstudio.com/)

After installing VsCode we should add a couple of extensions to help us with development:

* Python by Microsoft

  Language support extension for Python
  
* Pylance by Microsoft

  Useful Linter and support for static typing

* Black Formatter by Microsoft

  Useful Linter and formatter

* Material Icon Theme

  Cause it's AESTHETIC 
* Python Debugger by Microsoft

  Useful to debug code, more in the next section

### The debugger

The debugger is your best friend, TRUST ME, no need for print statements everywhere, no need to guess what your code is doing or where it's going, it's all there for you and it's there for free. Learn it, use it and you'll make learning to code a much less frustrating experience :)

Setting up the debugger is fairly simple after installing all the extensions, it should automatically prompt you to create a lunch.json file and make you choose the configuration from a predefined list.

To set breakpoints (points of interests where the debugger will stop) just place a red dot next to a line of code by clicking to the left of the line number

Use F5 to run your program, and jump from breakpoint to breakpoint

F10 to go line by line

There are also step into and step out functions which will be useful once we get into methods and loops.

### Getting started with code

- If you're here, it should hopefully mean you have downloaded the code folder for week1 in which you have found this markdown file and a main.py file alongside a python-intro.md file.
- You might be going through that python intro file and be looking at the examples and thinking: I'm not sure I trust this guy, I wish I could run these examples myself to check if he's telling the truth.
- That's smart, I make mistakes sometimes too.

- To check for yourself you can take the main.py file, copy any code, or write it yourself and run it.
- To run it you just have to have vs code open in this folder and press `F5`
- The first time a popup might appear asking you what you want to debug the file with, just select `python debugger` and then `python file` 
- Now the code should have run and you should see the output in your terminal.
- If you don't just press `ctrl/opt + ``


