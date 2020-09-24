# Selenium-COSC111-Assignment
A script to upload COSC 111 assignments directly to the canvas of UBCO.

It asks for the username and password for your canvas only on your first run and stores it in a text file in your computer thereafter.
Currently, it only works on my computer since the script only knows the location of my workspace in eclipse.

To execute it, type in the terminal: ./scipt.sh <name of your package>

It will automatically go to the workspace in eclipse, zip the file and create a new folder on your desktop called "COSC 111 Assignments".
Then it will login to your canvas and submit the project and logout, using selenium.
