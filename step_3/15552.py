# A+B를 빠르게 여러 번 출력하는 문제
import sys #import 필요! 

T = int(sys.stdin.readline()) #테스트 케이스의 개수
for i in range (1, T+1):
  A, B = map(int, input().split())
  print(A+B)