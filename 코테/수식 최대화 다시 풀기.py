from itertools import permutations
def calculate(expression, n, priority):
    if n == 2:
        return str(eval(expression))    
    
    return str(eval(priority[n].join([calculate(e, n + 1, priority) for e in expression.split(priority[n])])))

def solution(expression):
    answer = 0
    priorities = list(permutations(['+', '-', '*'], 3))
    
    for priority in priorities:
        result = int(calculate(expression, 0, priority))
        answer = max(answer, abs(result))
        
    return answer