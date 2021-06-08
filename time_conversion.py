import os
import sys

# https://www.hackerrank.com/challenges/time-conversion
#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == "AM":
        new = s.strip("AM")
        if new[0:2] == '12':
            return new.replace(new[0:2], "00")
        else:
            return new
    else:
        new = s.strip("PM")
        if s[-2:] == "PM" and s[:2] == "12":
            return new
        else:
            return new.replace(new[0:2], str(int(new[0:2]) + 12))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)

    f.write(result + '\n')

    f.close()