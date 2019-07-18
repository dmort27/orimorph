import fstinter
import math

def get_cost(aml):
    analysis, morphs, lemma = aml
    c = 0
    c += len(lemma)
    return c

def upper(l):
    return [w.upper() for w in l if w != 'Guess']

class OriMorph:
    def __init__(self, fstpath):
        self.fst = fstinter.FST(fstpath, get_cost)

    def lemmas(self, tokens):
        return [l for (w, (p, l)) in self.fst.analyses(tokens)]

    def analyses(self, tokens):
        return [upper(p) for (w, (p, l)) in self.fst.analyses(tokens)]
