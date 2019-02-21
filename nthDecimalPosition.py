import math
import pdb #for debugging. 

def CalculateE(val):
    eValue = round(math.e,val)
    return eValue

inputVal = input('Please enter integer value for decimal positions: ')
try:
    val = int(inputVal)
    print(CalculateE(val))
except:
    print("please enter integer value")
