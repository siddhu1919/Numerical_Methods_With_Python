"""Bisection Method With Python"""

"""Bisection Method Definition
The bisection method is used to find the roots of a polynomial equation. It separates the interval and subdivides the interval in which the root of the equation lies. The principle behind this method is the intermediate theorem for continuous functions. It works by narrowing the gap between the positive and negative intervals until it closes in on the correct answer. This method narrows the gap by taking the average of the positive and negative intervals. It is a simple method and it is relatively slow. The bisection method is also known as interval halving method, root-finding method, binary search method or dichotomy method.

Let us consider a continuous function “f” which is defined on the closed interval [a, b], is given with f(a) and f(b) of different signs. Then by intermediate theorem, there exists a point x belong to (a, b) for which f(x) = 0."""

import math


# TODO: code


# TODO: 1.Functionality -> Initial Root Finding Function
# TODO: 2.Functionality -> Create a new Bisection Method for taking custom Equations
# TODO: 3.Functionality -> Floting Point Value Fix For Root(Aka-> C)(User Defined)
# TODO: 4.Functionality -> creating a Beautiful Table OutPut

# sfafsfasfa

# Defining Function
def f(x):
    return x**3 - 4 * x - 9


# ∴ the root lies in [2, 3]
# a = 2 b = 3

def f(a):
    pass

def bisection(a, b):
    Iteration = 1
    a, b = a, b
    for i in range(10):
        c = (a + b) / 2
        print(
            f"Iteration {Iteration} | a = {a} | b = {b} | c = {c} | f(a) = {f(a)} | f(b) = {f(b)} | f(c) = {f(c)}"
        )
        Iteration += 1
        if f(c) < 0:
            a = c
        else:
            b = c


if __name__ == "__main__":
    a = 2
    b = 3
    bisection(a, b)
