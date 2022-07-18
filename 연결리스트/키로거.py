from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

for _ in range (n):
    stack_l = list()
    stack_r = list()
    
    commands = input().rstrip()
    for command in commands:
        if command == "<":
            if len(stack_l) != 0:
                stack_r.append(stack_l.pop())
            
        elif command == ">":
            if len(stack_r) != 0:
                stack_l.append(stack_r.pop())
                
        elif command == "-":
            if len(stack_l) != 0:
                stack_l.pop()
        else:
            stack_l.append(command)
            
    print( ''.join( stack_l  + list(reversed(stack_r))))
