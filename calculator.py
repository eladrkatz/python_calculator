# -*- coding: utf-8 -*-
"""calculator basic"""
from __future__ import print_function



#NUSCHA = '2x+6+9x+4x=56+82x+19+30+5x'

NUSCHA = raw_input('Enter equation to calculate:')

# 15x + 6 = 75 + 82x
# 15x - 82x = 75 - 6
# -67x = 69

# -67x / -67 = 69 / -67
# x = 69 / - 67

SHAVE = NUSCHA.find('=')

LEFT_SIDE = NUSCHA[0:SHAVE]
RIGHT_SIDE = NUSCHA[SHAVE+1:]

def reversed_string(a_string):
    return a_string[::-1]

# print ('entire equation: ', NUSCHA)
# print ('left side ', LEFT_SIDE)
# print ('right side', RIGHT_SIDE)


FIRST_PLUS = LEFT_SIDE.find('+')
# print (FIRST_PLUS)

LEFT_SIDE_ELEMENTS = LEFT_SIDE.split('+')

# print (LEFT_SIDE_ELEMENTS)
# print (len(LEFT_SIDE_ELEMENTS))

def find_number_of_x_and_numbers(equation_side):
    elements = equation_side.split('+')
    total_x = 0
    total_not_x = 0

    for element in elements:
        x_position = element.find('x')
        if x_position != -1:
            x_value = float(element[0:x_position])
            total_x += x_value
        else:
            number_value = float(element)
            total_not_x += number_value
    
    return (total_x, total_not_x)



(l_total_x, l_total_not_x) = find_number_of_x_and_numbers(LEFT_SIDE)
(r_total_x, r_total_not_x) = find_number_of_x_and_numbers(RIGHT_SIDE)

print ('left', l_total_x, l_total_not_x)
print ('right', r_total_x, r_total_not_x)

total_x = l_total_x - r_total_x
total_not_x = r_total_not_x - l_total_not_x

value_of_x = total_not_x / total_x

print ('THE ANSWER IS: X=', value_of_x)

