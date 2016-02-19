def EuclidAlgorithmIterations(a,b):
    if(not (isinstance(a,int) and isinstance(a,int))):
        raise BaseException("a and b should be integer")
    if(a<=0 or b<=0):
        raise BaseException("a an b should be greater than zero")
    if(b>a):
        swap = a
        a = b
        b = swap
    iterations = []
    r = a
    d = 1
    while(r!=0):
        d = int(a/b)
        r = a-b*d
        iterations.append({"a":a,"b":b,"d":d,"r":r})
        a = b
        b = r
    return iterations
def EuclidAlgorithmIterationsToString(iterations):
    result = ""
    for i in iterations:
        result+=("%d=%d*%d+%d\n")%(i["a"],i["d"],i["b"],i["r"])
    return result