#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def mul_digits(num):
    temp = list(str(num))
    temp_mul = 1
    for i in temp:
        if int(i) == 0:
            continue
        else:
            temp_mul *= int(i)
    return temp_mul  

def snake_case2(data):
    for letter in data:
        if letter.isupper():
            data=data.replace(letter,'_'+letter.lower())
    return data.strip('_')

def monkey_typing(data, words):
    cnt = 0
    for i in words:
        if i in data:
            cnt += 1
    return cnt

def snake_case(text):
    temp_snake = []
    for i in text:
        if ord(i) >= 65 and ord(i) <= 90:
            i = chr(ord(i) + 32)
            if len(temp_snake) > 0:
                temp_snake.append("_")           
        temp_snake.append(i)
    snake_case_name = ''.join(temp_snake)

    return snake_case_name


def to_camel_case(text):
    return text.title().replace('_','')

