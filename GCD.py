from EuclidAlgorithm import EuclidAlgorithmIterations
from EuclidAlgorithm import EuclidAlgorithmIterationsToString
from GCDLinearRepresentation import GCDLinearRepresentation
def GetGCDAlgorithmIterations(a,b):
    return EuclidAlgorithmIterations(a,b)
def GetGCDAlgorithmIterationsToString(iterations):
    return EuclidAlgorithmIterationsToString(iterations)
""" result format = {full_string,short_string,dict}"""
def GetGDCLinearRepresentation(result_format,a,b):
    return GCDLinearRepresentation(result_format,a,b)