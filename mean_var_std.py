import numpy as np

def calculate(a):
    try:
        b = a.reshape(3,3)
        data = {}
        data["mean"] = [b.mean(axis=0), b.mean(axis=1), a.mean()]
        data["variance"] = [b.var(axis=0), b.var(axis=1), a.var()]
        data["standard deviation"] = [b.std(axis=0), b.std(axis=1), a.std()]
        data["max"] = [b.max(axis=0), b.max(axis=1), a.max()]
        data["min"] = [b.min(axis=0), b.min(axis=1), a.min()]
        data["sum"] = [b.sum(axis=0), b.sum(axis=1), a.sum()]
    except ValueError:
        return "List must contains nine numbers."
    return data
