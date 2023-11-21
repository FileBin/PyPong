import math
from typing import Callable
from operator import add, sub
vec2 = tuple[float, float]
sdf2d_func = Callable[[vec2], float]

def veclength(p: vec2) -> float:
    return math.sqrt(sum(x*x for x in p))

def sdbox(point: vec2, box = (1,1)) -> float:
    d = [abs(p) - b*0.5 for p, b in zip(point, box)]
    return min(max(d), 0) + veclength(vec2(max(x,0) for x in d))

def normalize(vec: vec2) -> vec2:
    l = veclength(vec)
    return vec2(x/l for x in vec)

def lerp(a: float, b: float, t: float) -> float:
    return (1 - t) * a + t * b

def normal_sdf(sdf: sdf2d_func, p: vec2, eps=0.001) -> vec2:
    return normalize([
            sdf(vec2(map(add, p, (eps, 0)))) - sdf(vec2(map(add, p, (-eps, 0)))),
            sdf(vec2(map(add, p, (0, eps)))) - sdf(vec2(map(add, p, (0, -eps)))),
    ])

def dot(a: vec2, b: vec2) -> float:
    return sum(x*y for x, y in zip(a, b))

def reflect(v: vec2, n: vec2) -> vec2:
    d = 2*dot(n,v)
    return vec2(map(sub, v, vec2(x*d for x in n))) 