# A+B를 여러 번 출력하는 문제(3)
T = int(input()) #테스트 케이스의 개수
for i in range (1, T+1):
  A, B = map(int, input().split())
  print("Case #%d: %d"%(i, A+B))