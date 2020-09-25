# Josh Cominelli
# CS511
# 9/25/20

from z3 import *

def hw3p5():
    s = SolverFor("QF_LIA")
    set_option(produce_models=True)

    a,b,c,d,e,f = Ints('a b c d e f')

    s.add(a >= 0)
    at = 2

    s.add( b >= 0)
    bt = 1

    s.add(c >= 0)
    ct = 2

    s.add(d >= 0)
    dt = 2

    s.add(e >= 0)
    et = 7

    s.add(f >= 0)
    ft = 5

    s.add(Or((a+at<=c), (c+ct<=a)))
    s.add(Or((b+bt<=d), (d+dt<=b)))
    s.add(Or((b+bt<=e), (e+et<=b)))
    s.add(Or((d+dt<=e), (e+et<=d)))
    s.add(And((d+dt<=f), (e+et<=f)))
    s.add(a+at<=b)

    end = 14

    s.add(a+at<=end)
    s.add(b+bt<=end)
    s.add(c+ct<=end)
    s.add(d+dt<=end)
    s.add(e+et<=end)
    s.add(f+ft<=end)

    print(s.check())
    print(s.model())

hw3p5()