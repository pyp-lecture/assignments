#!/usr/bin/env python
import numpy as np

A = np.array([[1143, 0], [320, 48], [2314, 22]])
B = np.array([[123, 2111], [33, 41], [2999, 2861]])


def main():
    print(np.cumsum(A, axis=0)[:, 0])
    print(np.cumsum(B, axis=0)[:, 0])
    print(np.max(A))
    print(np.max(B))
    print(np.min(A))
    print(np.min(B))
    print(np.cross(A, B))


if __name__ == "__main__":
    main()
