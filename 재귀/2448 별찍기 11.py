n = int(input())

def star(l):
    if l == 3:
        return ['  *  ', ' * * ', '*****']
    
    arr = star(l//2)
    stars = []
    
    for i in arr:
        stars.append(' ' * (l // 2)+ i + ' ' * (l//2))
        
    for i in arr:
        stars.append(i + ' ' + i)
        
    return stars

print('\n'.join(star(n)))