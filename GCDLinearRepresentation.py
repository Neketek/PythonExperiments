from copy import deepcopy
from EuclidAlgorithm import EuclidAlgorithmIterations
from EuclidAlgorithm import EuclidAlgorithmIterationsToString
def GCDLinearRepresentationIterations(eu_a_iterations):
    result = list(eu_a_iterations)
    result.reverse()
    result.pop(0)
    return result
def __ReplaceAll(vars,value,target):
    for var_name in vars:
        if(isinstance(vars[var_name],dict)):
            __ReplaceAll(vars[var_name],value,target)
        elif(vars[var_name]==target):
            vars[var_name] = dict(value)
    return None
def __CreateReplacer(it):
    replacer = {"a":it["a"],"b":it["b"],"d":(-it["d"])}
    return replacer
def __ReplaceABByVariables(a,b,euclid_iterations):
    euclid_iterations[0]["a"] = ["a",1]
    euclid_iterations[0]["b"] = ["b",1]
    euclid_iterations[1]["a"] = ["b",1]
    return None
def __Mul(complex,d):
    a_value = complex["a"]
    b_value = complex["b"]
    d_value = complex["d"]
    if(isinstance(a_value,dict)):
        __Mul(a_value,d)
    else:
        if(isinstance(a_value,list)):
            a_value = deepcopy(a_value)
            a_value[1]*=d
            complex["a"] = a_value
        else:
            complex["a"]*=d
    if(isinstance(b_value,dict)):
        __Mul(b_value,d)
    else:
        if(isinstance(b_value,list)):
            b_value = deepcopy(b_value)
            b_value[1]*=d
            complex["b"] = b_value
        else:
            complex["b"]*=d
    return None
def __SimplifyDCoef(complex):
    a_value = complex["a"]
    b_value = complex["b"]
    d_value = complex["d"]
    if(isinstance(a_value,dict)):
        __SimplifyDCoef(a_value)        
    if(isinstance(b_value,dict)):
        __SimplifyDCoef(b_value)
        __Mul(b_value,d_value)
    elif(isinstance(b_value,list)):
        b_value = deepcopy(b_value)
        b_value[1]*=d_value
        complex["b"] = b_value
    else:
        complex["b"]*=d_value
    complex["d"] = 1
    return complex
def GCDLinearRepresentationComplex(gcdlr_iterations):
    complex = gcdlr_iterations.pop(0)
    complex["d"]*=-1
    replacer = None
    for i in gcdlr_iterations:
        replacer = __CreateReplacer(i)
        __ReplaceAll(complex,replacer,i["r"])
    return complex
def __CaclulateABCoefSum(complex,result):
    var = None
    for var_name in complex:
        var = complex[var_name]
        if(isinstance(var,dict)):
            __CaclulateABCoefSum(var,result)
        elif(isinstance(var,list)):
            if(var[0]=="a"):
                result["a"]+=var[1]
            else:
                result["b"]+=var[1]
    return None
def GCDLinearRepresentationComplexToString(complex):
    patternB = "%s*(%s)"
    patternA = "(%s)"
    result = ""
    a_value = complex["a"]
    b_value = complex["b"]
    d_value = complex["d"]
    if(isinstance(a_value,dict)):
        result+=patternA%GCDLinearRepresentationComplexToString(a_value)
    else:
        result+=str(a_value)
    if(isinstance(b_value,dict)):
        if(d_value<0):
            result+=patternB%(d_value,GCDLinearRepresentationComplexToString(b_value))
        else:
            result+="+"+patternB%(d_value,GCDLinearRepresentationComplexToString(b_value))
    else:
        if(d_value>0):
            result+="+"+str(d_value)
        else:
            result+=str(d_value)
        if(isinstance(b_value,int)):
            if(b_value<0):
                result+="*("+str(b_value)+")"
            else:
                result+="*"+str(b_value)
        else:
            result+="*"+str(b_value)
    return result
def GCDLinearRepresentation(result_format,a,b):
    if(result_format not in ["full_string","short_string","dict"]):
        raise BaseException("Unknown format! Possible formats = [full_string,short_string,dict]")
    short_format = result_format in ["dict","short_string"]
    eu_iterations = EuclidAlgorithmIterations(a,b)
    a_value = eu_iterations[0]["a"]
    b_value = eu_iterations[0]["b"]
    if(len(eu_iterations)==1):
        if(result_format=="dict"):
            return {"r":0,"a":1,"a_value":a_value,"b":-eu_iterations[0]["d"],"b_value":b_value}
        else:
            return "0=1*%d%d*%d"%(a_value,-eu_iterations[0]["d"],b_value)
    if(short_format):
        __ReplaceABByVariables(eu_iterations[0]["a"],eu_iterations[0]["b"],eu_iterations)
    linear_rep_iterations = GCDLinearRepresentationIterations(eu_iterations)
    complex = GCDLinearRepresentationComplex(linear_rep_iterations)
    if(not short_format):
        return "%d=%s"%(complex["r"],GCDLinearRepresentationComplexToString(complex))
    __SimplifyDCoef(complex)
    result = {"a":0,"b":0}
    __CaclulateABCoefSum(complex,result)
    result["a_value"] = a_value
    result["b_value"] = b_value
    result["r"] = complex["r"]
    if(result_format=="dict"):
        return result
    else:
        short_string = ""
        short_string+="%d=%d*%d"%(result["r"],result["a"],result["a_value"])
        if(result["b"]>0):
            short_string+=("+%d*%d"%(result["b"],result["b_value"]))
        else:
            short_string+=("%d*%d"%(result["b"],result["b_value"]))
        return short_string
    return None