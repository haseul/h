import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/plus-minus/problem
# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0; neg = 0; zero = 0
    for x in range(len(arr)):
        if arr[x] < 0:
            neg += 1
        elif arr[x] == 0:
            zero += 1
        elif arr[x] > 0:
            pos += 1

    print(f"{format(pos/len(arr), '.6f')}\n{format(neg/len(arr), '.6f')}\n{format(zero/len(arr), '.6f')}")



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)