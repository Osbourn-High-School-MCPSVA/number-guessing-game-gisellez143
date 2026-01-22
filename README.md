# Number Guessing Game
## Description:
You are going to create a number-guessing game. The game will ask the user to guess a number between 1 and 100. 
1. Generate a random number between 1 and 100.
2. Ask the user to guess the number.
3. Check the user’s input.
  - If they guessed a number larger than the answer, tell them their guess was too high.
    - Ask them to guess again.
  - If they guessed a number smaller than the answer, tell them their guess was too low.
    - Ask them to guess again
  - If they guessed the answer correctly
    - Congratulate them.
    - Ask them if they would like to play again.

In order for this game to be interesting, we will have to generate a new random number each game. 
There already exists a module in the Python standard library for generating random numbers, the random library. 
We can use the pre-existing functions from this module by importing them. The random library has a lot of 
functions in it, and because we only need one of them, we will only import that one function. We do that like this:

```
from random import randint
```

## Getting Started:
1. Add your name to the “author” field of the docstring
2. Add today’s date in the “Created” field of the docstring.

## Submission Instructions
1. GitHub Codespaces
  - In the menu bar on the left side of the screen, left-click on the “Source Control” button 
  - In the “SOURCE CONTROL” panel, Write a comment for your changes. (For longer projects it is a good idea to write about the areas your worked on or bugs you fixed.)
  - Left-click on the dropdown arrow on the right side of the blue “Commit” button.
  - Left-click on the option “Commit & Push”
  - You may get a warning box saying “There are no staged changes to commit.”
    - Left-click the blue “Yes” button.
2. Go back to GitHub
  - Open the assignment repository
  - Left-click on the python file you want to submit.
  - On the right side of the screen left-click on the download button
3. On your computer
  - Open windows explorer
  - Left-click on “Downloads”  
  - Highlight the files to submit
  - Right-click on your files
    - Zip selection
  - Name the file with the following format:
    - lastname_firstname_assignmentname.zip
4. On Schoology
  - go to the assignment
  - Left-click “Submit Assignment”
  - Ensure that you are looking at the “Upload” tab
  - Drag and drop the lastname_firstname_assignmentname.zip file into Schoology
  - Left-click “Submit”

## Example Output:
```
Guess a number between 1 and 100.
50
Your guess was too high!
Guess a number between 1 and 100.
25
Your guess was too low!
Guess a number between 1 and 100.
37
Your guess was too high!
Guess a number between 1 and 100.
31
Your guess was too high!
Guess a number between 1 and 100.
28
Your guess was too low!
Guess a number between 1 and 100.
29
Your guess was too low!
Guess a number between 1 and 100.
30
Correct! The number was 30.
Would you like to play again? (y/n)
y
Guess a number between 1 and 100.
```
