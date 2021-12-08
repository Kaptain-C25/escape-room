# DESIGN

We implemented the online escape room as a web app using HTML, CSS, and Flask. 

## app.py


## templates

### layout.html

### homepage.html

For our starting page, we created a design that is very similar to an old-fashioned video game starting screen. In HTML, we implemented a pixelated city picture as the background, the title “Escape Room” with a retro-themed font and style, and a button that says “press play” in the font Arcade Classic Regular. We used CSS as a way to make the title page look more aesthetic by centering all the text, adjusting the vertical location of the title and the button, and making the button change color when you hover a mouse over it. When you click on the “Press Play” button, you are redirected to Room 1 through a flask route.

### room_(1, 2, 3).html

What a user will see in this page is a picture of an old-fashioned room. The user will need to click around to find different clues that are hidden. In code, we created transparent buttons in HTML and CSS that when clicked, call upon a javascrpt function using event listeners to open a pop up form at the location. For room 1, the puzzles were ASCII themed. Room 2 had math problems, and room 3 had a theme of binary numbers. This form used flask: we implemented code that when the user inputted the right answer, a picture would appear in the bar on the top of the website. This picture would be a hint to the password that will allow them to escape the room. Thus, the user would then have to input a password in the form created by HTML, CSS, and Flask that is found at the bottom of the webpage. We followed the same format of Room 1 for Room 2 and Room 3. 

### end.html

After Room 3, the users are redirected to the ending page. We used HTML and CSS to create the page, and it has a similar theme to the starting page. There is a pixelated city as the background, a title that states “you win” in a retro-themed font, and a button that states “play again” that will redirect users to the starting page.

## static

### styles.css

### assets

Here are the images and font files we used in the web app

## others
- __pycache