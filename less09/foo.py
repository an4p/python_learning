import main
x = 42
def callf(func):
    return(func())

print(callf(main.helloworld))