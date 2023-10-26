# b가 홀수
# # a = 10 , b = 11 , c = 12
# 10^11 % 12
# = ((10^5)%12 x (10^5)%12 x 10)% 12
# = ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12


# b가 짝수
# # a = 10 , b = 6 , c = 12
# 10^6 % 12
# = ((10^3)%12 x (10^3)%12)% 12
# = ((10^1)%12 x (10^1)%12 x 10) %12 x (10^1)%12 x (10^1)%12 x 10) %12 x 10) %12


# 솔직히 이해 안감 다시 풀기
import sys
a,b,c = map(int,sys.stdin.readline().split())

def multi (a,n):
  if n == 1:
      return a%c
  else:
      tmp = multi(a,n//2)
      if n %2 ==0:
          return (tmp * tmp) % c
      else:
          return (tmp  * tmp *a) %c
          
print(multi(a,b))