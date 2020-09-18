; Josh Cominelli
; CS511
; 9/18/20

(declare-const p1 Bool)
(declare-const p2 Bool)
(declare-const p3 Bool)
(declare-const p4 Bool)

(define-fun phi () Bool 
    (and
        (or (not p1) (not p2) p3 p4)
        (or (not p1) p2 (not p3) p4)
        (or (not p1) p2 p3 (not p4))
        (or p1 (not p2) (not p3) p4)
        (or p1 (not p2) p3 (not p4))
        (or p1 p2 (not p3) (not p4))
        (or p1 p2 p3 p4)
    )
)

(define-fun psi () Bool
    (or
        (and p1 p2 (not p3) (not p4))
        (and p1 (not p2) p3 (not p4))
        (and p1 (not p2) (not p3) p4)
        (and (not p1) p2 p3 (not p4))
        (and (not p1) p2 (not p3) p4)
        (and (not p1) (not p2) p3 p4)
        (and p1 p2 p3 p4)
        (and (not p1) (not p2) (not p3) (not p4))
    )
)

(define-fun theta () Bool
    (=
        (= p1 p2)
        (= p3 p4)
    )
)

(assert (= phi psi theta))
(check-sat)