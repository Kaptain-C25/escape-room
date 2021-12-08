# README

VIDEO: https://youtu.be/drd14ldrzxU

## THEME

For our project, we created an online escape room. As college students, we know how stressful reading periods and finals can be. Thus, our mission for this CS50 project is to help people have fun and relieve stress through solving different puzzles and riddles. This escape room game can be played either individually or collaboratively. We hope our project can allow everyone to take a break from work and enjoy some puzzles.

## HOW TO START

1. In terminal, enter `source flask-venv/bin/activate` to activate virtual environment. You should see `(flask_venv)` at the start of the command prompt on the next line
2. Enter `flask run` in the terminal. You should see:
    `* Environment: production`
    `  WARNING: This is a development server. Do not use it in a production deployment.`
    `  Use a production WSGI server instead.`
    `* Debug mode: off`
    `* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
3. Windows: Ctrl + click the http link to go to the game's homepage
   Mac: Cmd + click the http link to go to the game's homepage

## HOW TO PLAY

1. Click on the “Press Play” button, you should be redirected to Room 1. 
2. You will need to locate hidden buttons around the page that each load a different puzzle when clicked
3. By solving the puzzles in the room, you will collect pictures of hints that appear at the top of the page. 
4. Based on the hints, you will need to input a password in the text box at the bottom of the page to complete the room
5. Click on the "Try Password" button; if your answer is correct, you will be brought to the next room

We followed the same format of Room 1 for Room 2 and Room 3, and upon solving Room 3, you should be brought to an end screen where you can choose to play again.

### ANSWER KEY

- Room 1 password: Wasp
    - Game 1 answer: W
    - Game 2 answer: A
    - Game 3 answer: S
    - Game 4 answer: P
- Room 2 password: 7468
    - Game 1 answer: 7
    - Game 2 answer: 4
    - Game 3 answer: 6
    - Game 4 answer: 8
- Room 3 password: Game
    - Game 1 answer: G
    - Game 2 answer: A
    - Game 3 answer: M
    - Game 4 answer: E

## FAQ

- Can I go back to a previous room while playing?
    Yes you can. Just press the back button in your browser and confirm the form resubmit or change the room number in the url and load the page. You will not be able to skip rooms however.
- What if I cannot locate a button in one of the rooms?
    If you want to look at the source code, you can go to the "styles.css" file under the "static" directory, locate the css of the specific button you are looking at, in the format "#room{num}btn{num}", and delete the "background" attribute. This will reveal the button on the page.
