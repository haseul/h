import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/the-hurdle-race/problem
#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    # print(f"{k} {height}")
    max_hurdle = max(height)

    if k > max_hurdle:
        return 0
    else:
        return abs(k - max_hurdle)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    print(str(result))