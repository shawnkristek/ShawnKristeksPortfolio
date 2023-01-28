import os

def printVar(var=""):
    if var == "":
        for k,v in sorted(os.environ.items()):
            print(k+":",v)
    else:
        print(os.getenv(var))