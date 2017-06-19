#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import array, ndarray, exp, log


def ans11():
    print(sorted((lambda s: [(x, s.count(x)) for x in set(s)])(input().split()), key=lambda x: -x[1]))


def ans12():
    from simpleeval import EvalWithCompoundTypes as E
    print(''.join(('\n' if x[1] == 'B' else ' ') + x[0] for x in E().eval(input()) if x[1] != 'O')[1:])


class _Shape(tuple):
    def __call__(self):
        return self[0]


class tensor_1d(ndarray):
    def __new__(cls, vector):
        assert isinstance(vector, (tuple, list))
        r = ndarray.__new__(cls, len(vector), dtype=array(vector).dtype)
        r[:] = vector
        return r

    @property
    def shape(self):
        return _Shape(super().shape)

    def print(self):
        print(self.tolist())

    def sum(self):
        return array(self).sum()

    def exp(self):
        return exp(self)

    def log(self):
        return log(self)


def ans2():
    a = tensor_1d([1, 2, 3])
    b = tensor_1d([4, 5, 8])
    c = a + b
    d = a - b
    e = a * b
    print((c + d + e).sum())
    c.print()
    d.exp().print()
    e.log().print()


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        if sys.argv[1] == 'hw11':
            ans11()
        elif sys.argv[1] == 'hw12':
            ans12()
        elif sys.argv[1] in ('hw21', 'hw22', 'hw2'):
            ans2()
        else:
            print('Usage:', sys.argv[0], 'hwXX')
    else:
        print('Usage:', sys.argv[0], 'hwXX')
