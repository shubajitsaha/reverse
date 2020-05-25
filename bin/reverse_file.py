from reverse import *
import os,sys

if __name__ == "__main__":
    rv = reverse.ReverseFile(sys.args[1],sep='\n')
    rv.reverse()
    rv.write(sys.args[2])
    print("Success")
    