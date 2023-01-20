# Color Matching Game

This game is played on a rectangular board which consists of several rows and columns, initially filled with different colored balls. By selecting a group of adjoining balls of the same color, a player may remove them from the game board. Balls that are no longer supported will fall down, and a column without any balls will be trimmed away by other columns always sliding to the left side. In addition to the colored balls there may be a bomb on the board. If the player picks this bomb that shown by ”X” character, all the balls in the row and column will be removed regardless of their color. The goal of the game is to remove as many balls from the playing field as possible.

There can be 9 different colored balls on the board. The weight of each of these different colored balls and the weight of the bomb are different (Black (B) = 9, Gray (G) = 8, White (W) = 7, Yellow (Y) = 6, Red (R) = 5, Pink (P) = 4, Orange (O) = 3, Dark blue (D) = 2, Fuchsia (F) = 1, Bomb (X) = 0). Balls of each color and the bomb contribute to the score as much as their weight.

The game begins by asking the user to select a cell by entering the corresponding row and column (There must be a space between the entered row and column). If the chosen cell has no neighbor with the same color, no change in the board is expected. In this case, the previous status of the board will be printed and the user will be asked for new coordinates. Otherwise, the new state of the board is printed together with the updated score. If there is no cell which has no neighbor with ball of the same color and also there is no bomb (X) in a cell, it means that the game is over.

# Execution
    python3 game.py input.txt
   The input file denotes the initial configuration of the board.
