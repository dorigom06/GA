import numpy as np

#initialize DNA
#assuming 3x3
#state should be 3x3 matrix in np.array format


class Face(object):
#the values in the state should be between 1 and 9 inclusive
    #initialize the face
    def __init__(self,state = np.zeros((3,3))):
        self.state = state
        self.center = self.state[1,1]
        self.fitness = None
        return

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def getCenter(self):
        self.center = self.state[1,1]
        return self.center

    def getFitness(self):
        score = 0.0
        for i in self.state:
            for j in i:
                if int(j)==int(self.center):
                    score += 1
        #print(score/9.0)
        return score/9.0
    
    def __str__(self):
        return str(self.state)

class Cube(object):
    def __init__(self,up=None,front=None,left=None,right=None,back=None,down=None):
        #the inputs should be instances of faces
        self.front = front
        self.back = back
        self.right = right
        self.left = left
        self.down = down
        self.up = up

        self.faces = [self.up, self.front, self.left, self.right, self.back, self.down]

        #self.possible_moves = [self.r1(),self.r2(),self.r3(),self.c1(),self.c2(),self.c3(),None]
        self.moves = []

        return None

    def getFaces(self):
        print(self.faces)
        return None
    
    #design the moves
    def updateMoves(self,move):
        self.moves.append(move)
        return None

    def r1(self):
        original1 = self.up.getState()
        original2 = self.front.getState()
        original3 = self.right.getState()
        original4 = self.left.getState()
        original5 = self.back.getState()
        
        new_up = np.zeros((3,3))
        new_front = np.zeros((3,3))
        new_right = np.zeros((3,3))
        new_left = np.zeros((3,3))
        new_back = np.zeros((3,3))

        #fixing up
        new_up[0,0] = original1[2,0]
        new_up[0,1] = original1[1,0]
        new_up[0,2] = original1[0,0]
        new_up[1,0] = original1[2,1]
        new_up[1,1] = original1[1,1]
        new_up[1,2] = original1[0,1]
        new_up[2,0] = original1[2,2]
        new_up[2,1] = original1[1,2]
        new_up[2,2] = original1[0,2]
        self.up.setState(new_up)

        #fixing front
        new_front[0,0] = original3[0,0]#from right
        new_front[0,1] = original3[0,1]#from right
        new_front[0,2] = original3[0,2]#from right
        new_front[1,0] = original2[1,0]
        new_front[1,1] = original2[1,1]
        new_front[1,2] = original2[1,2]
        new_front[2,0] = original2[2,0]
        new_front[2,1] = original2[2,1]
        new_front[2,2] = original2[2,2]
        self.front.setState(new_front)

        #fixing right
        new_right[0,0] = original5[0,0]#from back
        new_right[0,1] = original5[0,1]#from back
        new_right[0,2] = original5[0,2]#from back
        new_right[1,0] = original3[1,0]
        new_right[1,1] = original3[1,1]
        new_right[1,2] = original3[1,2]
        new_right[2,0] = original3[2,0]
        new_right[2,1] = original3[2,1]
        new_right[2,2] = original3[2,2]
        self.right.setState(new_right)

        #fixing left
        new_left[0,0] = original2[0,0]#from front
        new_left[0,1] = original2[0,1]#from front
        new_left[0,2] = original2[0,2]#from front
        new_left[1,0] = original4[1,0]
        new_left[1,1] = original4[1,1]
        new_left[1,2] = original4[1,2]
        new_left[2,0] = original4[2,0]
        new_left[2,1] = original4[2,1]
        new_left[2,2] = original4[2,2]
        self.left.setState(new_left)

        #fixing back
        new_back[0,0] = original4[0,0]#from left
        new_back[0,1] = original4[0,1]#from left
        new_back[0,2] = original4[0,2]#from left
        new_back[1,0] = original5[1,0]
        new_back[1,1] = original5[1,1]
        new_back[1,2] = original5[1,2]
        new_back[2,0] = original5[2,0]
        new_back[2,1] = original5[2,1]
        new_back[2,2] = original5[2,2]
        self.back.setState(new_back)
        


        
        return "r1"

    def r2(self):
        return

    def r3(self):
        return

    def c1(self):
        return

    def c2(self):
        return

    def c3(self):
        return

    def finished(self):
        if self.getFitness == 1.0:
            return True
    

    #overall fitness
    def getFitness(self):
        s = 0.0
        for face in self.faces:
            s += face.getFitness()
        s = s/len(self.faces)
        print(s)
        return s

    def __str__(self):
        ans = []
        for face in self.faces:
            ans.append(face)
        return 

#testing site
u = Face(np.array([[1.,1.,1.],[1.,1.,1.],[1.,1.,1.]]))
#u.getFitness()
f = Face(np.array([[2.,2.,2.],[2.,2.,2.],[2.,2.,2.]]))
#f.getFitness()
l = Face(np.array([[3.,3.,3.],[3.,3.,3.],[3.,3.,3.]]))
#l.getFitness()
r = Face(np.array([[4.,4.,4.],[4.,4.,4.],[4.,4.,4.]]))
#r.getFitness()
b = Face(np.array([[5.,5.,5.],[5.,5.,5.],[5.,5.,5.]]))
#b.getFitness()
d = Face(np.array([[6.,6.,6.],[6.,6.,6.],[6.,6.,6.]]))
#d.getFitness()

c = Cube(u,f,l,r,b,d)
c.r1()
#c.getFaces()
c.getFitness()
print(c)

    
