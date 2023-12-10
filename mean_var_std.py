import numpy as np

def calculate(list):
    a = list
    b = list.reshape(3,3)
    try:
        data = {}
        data["mean"] = list(b.mean(axis=0), b.mean(axis=1), a.mean())
        data["variance"] = list(b.var(axis=0), b.var(axis=1), a.var())
        data["standard deviation"] = list(b.std(axis=0), b.std(axis=1), a.std())
        data["max"] = list(b.max(axis=0), b.max(axis=1), a.max())
        data["min"] = list(b.min(axis=0), b.min(axis=1), a.min())
        data["sum"] = list(b.sum(axis=0), b.sum(axis=1), a.sum())
    except ValueError:
        return "List must contain nine numbers."
    
    return data
