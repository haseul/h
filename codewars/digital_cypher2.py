#!/usr/bin/python3

def decode(string, key):
    strl = len(string)
    keyl = len(str(key))

    res = strl // keyl * str(key) +str(key)[:keyl % key]
    res_ = [int(x) for x in res]

    new = [a - b for a, b in zip(string, res_)]
    new_ = [chr(ord('a')+ord(chr(v))-1) for v in new]

    return "".join(new_) 

