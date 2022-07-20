#bring in custom function from another file
from functions import square

#test use that function
for i in range(5):
    print(f"the square of {i} is {square(i)}")