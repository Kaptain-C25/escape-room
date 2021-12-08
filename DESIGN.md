# DESIGN

We implemented the online escape room as a web app using HTML, CSS, and Flask. 

## app.py

Here are all the routes to the html pages that does the checking of user input, either adding hint pictures to the nav bar by passing an updating list to the html pages or sending the user to the next room/page.
The routes check for correct answers by either using the re.search function or by individual checks, both case-insensitive
We also created a decorator function called "solve_required()" that takes the room number as input and checks if previous rooms are solved such that if a user tries to jump to a different room without solving an earlier one, he would be sent back.

## templates

### layout.html

In layout.html, we implemened jinja as a way to simplify formatting in room_x.html pages as well as passing dynamic information (i.e. hint pictures) to the HTML pages. We also created a navbar and linked bootstrap to create the user's inventory (the bar where letters or numbers appear at the top of the webpage).

### homepage.html

For our starting page, we created a design that is very similar to an old-fashioned video game starting screen. In HTML, we implemented a pixelated city picture as the background, the title “Escape Room” with a retro-themed font and style (that we created ourselves), and a button that says “press play” in the font Arcade Classic Regular. We used CSS as a way to make the title page look more aesthetic by centering all the text, adjusting the vertical location of the title and the button, and making the button change color when you hover a mouse over it. 
When you click on the “Press Play” button, you are redirected to Room 1 through a flask route.

### room_(1, 2, 3).html

We created transparent buttons in HTML and CSS and positioned them at specific locations on the images using absolute positioning. When clicked, they will call upon a javascript function using event listeners and open a pop up form at the location. For room 1, the puzzles were ASCII themed. Room 2 had math problems, and room 3 had a theme of binary numbers. 
The pop up form will submit a post request to the puzzle routes of the rooms in flask, and if the user inputted the right answer, the route would update the list of hint pictures and pass their names into the html and reload the page.
Similarily, the user input in the password form at the bottom of the webpage is also sent to the room's route as a post request and is checked for correctness.

### end.html

After Room 3, the users are redirected to the ending page. We used HTML and CSS to create the page, and it has a similar theme to the starting page. There is a pixelated city as the background, a title that states “you win” in a retro-themed font (that we created ourselves), and a button that states “play again” that will redirect users to the starting page.

## Others
- pycache: byte code for app.py interpretor
- .vscode: some internal setup for vscode extensions
- flask_venv: virtual environment set up for the web app to ru in
- static:
    - assets: pictures and fonts we used for our webpage
    - styles.css: we used CSS for all of our pages for aesthetic