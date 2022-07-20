#decorater is a function that takes function as input and returns modified version as output
#in python, function is value and can be passed as input
#functional programming paradigm

#announce takes f and adds text before and after
def announce(f):
    #new function adding to original function
    def wrapper():
        print("About to run function...")
        f()
        print("Done with function")
    return wrapper

#call announce to decorate
@announce
def hello():
    print("Hello world")

#execute function
hello()