# RedBlueNim-AI-Gaming

## Task 1

Your task is to build an agent to play two versions (standard and misère) of  the variant of a game called nim (called red-blue nim against a human player). The game consists of two piles of marbles (red and blue). On each players turn they pick a pile and remove one or two marbles from it (if possible). If on their turn, either pile is empty then they lose in the standard version and win in the misère version. The amount they lose (or win) is dependent on the number of marbles left (2 for every red marble and 3 for every blue marble). So if on the computer player turn, it has 0 red marbles and 3 blue marbles, it loses 9 points in the standard version (or wins 9 points in the misère version).

![Screenshot 2025-02-28 123313](https://github.com/user-attachments/assets/d9b9335a-3ae1-4c7a-bd09-43ddea5da409)

The program should alternate between these turns till the game ends (when the players run out of either red or blue marbles). Once the game ends, calculate who won and their final score and display it to the user.

## Task 2
If your program determines computer move by using depth limited MinMax search with alpha beta pruning then you will be given 20 points extra credit. You will need to come up with a eval function to use with the program also.


## Instructions to execute the program 

### command: python RedBlueNim.py <red> <blue> <player> <depth>

### methods: 

findminmaxAlgo(): It is used to select the player's turns and find the winning score
find_alpha_beta(): it implements minmax algorithm

eval function in the RedBlueNim code use to evaluate the score of the game.
It multiplies the red score which is 2 and the blue's scores and returns the overall score of the 
left out marbles. The marbles score which is returned used to caluculate the alpha and beta values.
and finds the min and max values.

The eval function is used in two places in the program:

- In the find_alpha_beta function, where it is called when the depth of the search tree reaches zero or 
the game ends (i.e., one of the players has no stones left).

- In the findminmaxAlgo function, where it is called as the base case when the depth of the search tree 
reaches zero or the game ends.
