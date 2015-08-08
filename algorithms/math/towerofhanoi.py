"""
   towerofhanoi.py

   Recursive approach to solve the famous tower of Hanoi problem
"""


#returns when height of the tower is 0
def movePeg(height,fromPole, toPole, withPole):
    if height >= 1:
        movePeg(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        movePeg(height-1,withPole,toPole,fromPole)

#allowed to be called only when movePeg function returns
#movies the disk from peg fp to tp
def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

movePeg(3,"A","B","C")
