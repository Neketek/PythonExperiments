from GCD import GetGCDAlgorithmIterations
from GCD import GetGCDAlgorithmIterationsToString
from GCD import GetGDCLinearRepresentation
gcd_values = {"a":0,"b":0,"stop":0}
def InsertValue(values,value_name):
     while(True):
        values[value_name] = input("Insert %s:"%value_name)
        try:
            values[value_name] = int(values[value_name])
            break
        except:
            print ("Incorrect input")
while(True):
    print ("GCD(a,b)")
    InsertValue(gcd_values,"a")
    InsertValue(gcd_values,"b")
    print("------------------------------------------------")
    print ("GCD Algorithm iterations")
    gcd_iterations = GetGCDAlgorithmIterations(gcd_values["a"],gcd_values["b"])
    print (GetGCDAlgorithmIterationsToString(gcd_iterations))
    print("------------------------------------------------")
    print ("GCD Linear Representation:short_string")
    print (GetGDCLinearRepresentation("short_string",gcd_values["a"],gcd_values["b"]))
    print("------------------------------------------------")
    print ("GCD Linear Representation:full_string")
    print (GetGDCLinearRepresentation("full_string",gcd_values["a"],gcd_values["b"]))
    print("------------------------------------------------")
    print ("GCD Linear Representation:dict")
    print (GetGDCLinearRepresentation("dict",gcd_values["a"],gcd_values["b"]))
    print("------------------------------------------------")
    print ("If you wanna stop insert value<=0 else value>0")
    InsertValue(gcd_values,"stop")
    if(gcd_values["stop"]<0):
        break