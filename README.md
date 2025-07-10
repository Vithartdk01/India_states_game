## Finding India States Game
This Python program is designed to help users learn and memorize the states of India through an interactive map and a user-friendly interface.
## How it works?
- Launch the Program:
   The program opens a window displaying the map of India.
- Enter State Names:
Users enter the name of a state in the dialogue box. If the entry is correct and not previously entered, it is marked on the map, and the counter increases.
- View Progress:
The number of correctly entered states is always visible at the top of the interface.
- CSV File Integration:
The list of all Indian states is read from a CSV file. This file can be opened separately to review or update the list of states to learn.
## Code Description
- Setup and Initialization
    - turtle: Used for graphical display and drawing on the screen.
    - pandas: Used for reading and handling tabular data from a CSV file.
- Screen Setup:
    - A Turtle screen is created and titled "INDIA States Game".
    - An image file (blank_india_map.gif) of the Indian map is set as the shape of the turtle window, serving as the background for the game.
- Data Preparation:
    - The program reads a CSV file (states.csv) containing state names and their corresponding x, y coordinates on the map.
    - A list of all state names is extracted for easy lookup.
- Game Loop:
    - Prompts user to enter state names in a dialog box.Ends if user types "Exit".Saves unguessed states to states_to_learn.csv
- Processing Correct Guesses:
     - If input matches a state and isn't already guessed.Adds state to guessed list.Writes state name on the map at correct coordinates.
- Key Features:
    - Progress is always visible in the dialog box.Missed states are saved for future learning.Correct guesses are labeled on the map for visual feedback
- CSV File Structure:
    - state: State name and x, y: Coordinates for map placement.
## [Video](https://drive.google.com/file/d/1L8EeW7lUYE7BnNtNl6u5UxvPlQrauqIU/view?usp=sharing)




       
