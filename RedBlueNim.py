import datetime,sys
now = datetime.datetime.now()

def eval(red,blue,player):
    if player=="human":
        return red*2+blue*3
    else:
        return -(red*2+blue*3)
    
def find_alpha_beta(res,red,blue,alpha,beta,depth,player):
    score,move  =0,-1
    if red==0 or blue==0 :
        # we need to call the eval function
        rests = eval(red,blue,player)
        # print(rests)
        return [rests,-1]
    if depth ==0:
        rests =eval(red,blue,player)
        return [rests,-1]
    move = -1
    if player=="human":
        res = -1000000
    else:
        res = 1000000
    for i in range(0,2):
        if red==0 and i==0:
            continue
        if blue==0 and i==1:
            continue
        # if i==0:
        #     cur = red
        # else:
        #     cur = blue
        re =red
        bl = blue
        if i == 0: re-=1
        else: bl-=1
        pl = player
        if pl=="human":
            pl="computer"
        else:
            pl="human"
        # print(red," ",blue)
        rest = find_alpha_beta(res,re,bl,alpha,beta,depth-1,pl)
        # print(rest)
        
        score= rest[0]
        if player=="human":
            if score>res:
                res = score
                move = i
            # print(res,"yellow",move)
            alpha = max(alpha,res)
        else:
            if score<res:
                res = score
                move = i
            beta = min(beta,res)
            # print(res,"yellow",move)
        # print(alpha,beta,1)
    
        if beta<=alpha:
            break
    return score,move  
      
def findminmaxAlgo(red,blue,alpha,beta,depth,player):
    # base case
    # print(red,"yellow",blue)
    if red==0 or blue==0 or depth==0:
        # we need to call the eval function
        return eval(red,blue,player),-1
    #computer will be the max player
    # human will be the min player
    res=0
    # print(red,"yellow",blue)
    return find_alpha_beta(res,red,blue,alpha,beta,depth,player)

def main():
    length=len(sys.argv)
    # print(length)
    red = sys.argv[1]
    blue = sys.argv[2]
    red = int(red)
    blue = int(blue)
    depth =  -1
    player = "computer"
    if length==3:
        player = "computer"
    if length==4:
        x = sys.argv[3]
        if len(x) >= 4:
            player = x
        else:
            player = "computer"
            depth=int(x)
    if length == 5:
        x = sys.argv[3]
        y = sys.argv[4]
        if len(x) == 5:
            player =x
        else:
            player = "computer"
        depth= int(y)
    lis = [red,blue]
    find_color(lis,red,blue,depth,length,player) 

def stmt():
    print("The turn is yours.\nChoose 1 for red and 2 for blue")

def stmt1(ls):
    print("The turn is computer's.")
    print("Computer has picked option")
    print(ls)
    
def print_sol(player,lis):
    res = 0
    blue=3
    red=2
    for i in range(len(lis)):
        if i==0:
            res = res+lis[0]*red
        if i==1:
            res = res+lis[1]*blue
    winner=""
    if player == "human":
        winner="You"
    else:
        winner = "Computer"
    print("\nGAME ENDED!")
    print(winner,"has won the game with score :",res)

def find_color(lis,red,blue,depth,length,player):
    choice = 0
    # lister = [red,blue]
    # print(lis)
    while(lis[0]>0 and lis[1]>0):
        print("\nCurrent state :")
        print(lis[0],"Red ",lis[1],"Blue\n")
        # if the player is computer then we need to do implement minMaxAlgo
        if player=="computer":
            ls=findminmaxAlgo(lis[0],lis[1],-1000000,1000000,depth,player)
            # print(ls)
            if ls is None:
                ls=None
            else:
                choice = ls[1]
            stmt1(ls[1]+1)
        elif player=="human":
            stmt()
            choice = int(input())
            choice -=1
        lis[choice] = lis[choice] - 1
        # red = lis[0]
        # blue = lis[1]
        # print(red,"  ",blue)
        if player=="computer":
            player = "human"
        else:
            player = "computer"
    print_sol(player,lis)

main()
end=datetime.datetime.now()
print("Time taken :",end-now)


