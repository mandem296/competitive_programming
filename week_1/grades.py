#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    final = []
    for grades in grades:
        if grades >= 38 and grades % 5 >= 3:
            grades = grades + 5 - (grades % 5)
        final.append(grades)
    return final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
