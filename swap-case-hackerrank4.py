def swap_case(s):
    final=''
    for i in s:
        if i.isupper():
            final=final+i.lower()
        elif i.islower():
            final=final+i.upper()
        else:
           final=final+i
    return final

#question link
#https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
