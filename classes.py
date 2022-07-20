#define a class 

class Point():
    #use __init__ which is auto called when making new point
    #all methods take first argument self
    #self represents the argument in question
    #point also needs x and y
    def __init__(self, input1, input2):
        #allow point to store its own x and y
        self.x = input1
        self.y = input2
        #need to make sure the inputs are self stored

#create a point, which implicitly calls init
p = Point(2, 8)

#go into point and access x value
print(p.x)
print(p.y)
        