from math import sqrt
from algos.dot_product import dpv

def vl(vec)->float:
    """Vector's length |vec| - which is the square root of the dot product of the vector with itself.
    """
    return sqrt(dpv(vec, vec))
