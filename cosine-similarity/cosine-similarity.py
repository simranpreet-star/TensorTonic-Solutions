import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    x=np.asarray(a,dtype=float)
    y=np.asarray(b,dtype=float)
    num=float(np.dot(x,y))
    dino=float(np.linalg.norm(x)*np.linalg.norm(y))
    if dino==0:
        return 0.0
    return float(num/dino)
    
    pass