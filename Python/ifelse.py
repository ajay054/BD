#!/bin/python3

import math
import os
import random
import re
import sys



def classify_number(n):
    if n % 2 == 1:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    classify_number(n)

