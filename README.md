# RedBlueNim-AI-Gaming

## Task 1

Your task is to build an agent to play two versions (standard and misère) of  the variant of a game called nim (called red-blue nim against a human player). The game consists of two piles of marbles (red and blue). On each players turn they pick a pile and remove one or two marbles from it (if possible). If on their turn, either pile is empty then they lose in the standard version and win in the misère version. The amount they lose (or win) is dependent on the number of marbles left (2 for every red marble and 3 for every blue marble). So if on the computer player turn, it has 0 red marbles and 3 blue marbles, it loses 9 points in the standard version (or wins 9 points in the misère version).

Your program should be called red_blue_nim and the command line invocation should follow the following format:

- red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>

<num-red> and <num-blue> are required. (Number of red and blue marbles respectively)
<version> is either
- standard - Player loses if either pile empty on their turn [default option if <version> is not given]
- misere - Player wins if either pile empty on their turn

<first-player> can be
- computer - play a full game from given state with computer starting the game followed by human [default option if <first-player> is not given]
- human - play a full game from given state with human starting the game followed by computer

<depth>  only used if depth limited search (Extra Credit) is implemented.

For a full game,

On Computer turn, the program should use MinMax with Alpha Beta Pruning to determine the best move to make and perform the move.

For move ordering in standard version, use:
- Pick 2 red marble
- Pick 2 blue marble
- Pick 1 red marble
- Pick 1 blue marble

For misère version, invert that order.

On Human turn, the program should use a prompt to get the move from the human user and perform the move.

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
