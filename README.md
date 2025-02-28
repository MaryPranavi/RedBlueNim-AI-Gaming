# RedBlueNim-AI-Gaming

##Instructions to execute the program 

###command: python RedBlueNim.py <red> <blue> <player> <depth>

###methods: 

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
