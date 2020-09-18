# Josh Cominelli
# CS511
# 9/18/20

from z3 import *

def problem6():

    p1,p2,p3,p4 = Bools('p1 p2 p3 p4')

    phi = And(Or(Not(p1), Not(p2), p3, p4),
              Or(Not(p1), p2, Not(p3), p4),
              Or(Not(p1), p2, p3, Not(p4)),
              Or(p1, Not(p2), Not(p3), p4),
              Or(p1, Not(p2), p3, Not(p4)),
              Or(p1, p2, Not(p3), Not(p4)),
              Or(p1, p2, p3, p4))

    psi = Or(And(p1, p2, Not(p3), Not(p4)), 
             And(p1, Not(p2), p3, Not(p4)), 
             And(p1, Not(p2), Not(p3), p4), 
             And(Not(p1), p2, p3, Not(p4)), 
             And(Not(p1), p2, Not(p3), p4), 
             And(Not(p1), Not(p2), p3, p4), 
             And(p1, p2, p3, p4), 
             And(Not(p1), Not(p2), Not(p3), Not(p4)))

    theta = ((p1 == p2) == (p3 == p4))

    s = Solver() 
    s.add(phi == psi, phi == theta, psi == theta) 
    print(s.check())

problem6()