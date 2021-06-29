#!/usr/bin/python3

import string

rev_strs = string.ascii_lowercase[::-1]

def decode(message):
	result = [x if x == " " else rev_strs[string.ascii_lowercase.index(x)] for x in message]
	
	return "".join(result)

