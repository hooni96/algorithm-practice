'''
★기출 03. 문자열 뒤집기★
0과 1로만 이루어진 문자열 s를 가지고 있다. s열 안에 모든 숫자를 전부 같게 만들려한다.
할 수 있는 행동은 s에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다.
문자열 s가 주어졌을 때, 다솜이가 해야 하는 행동의 최소 횟수를 출력하세요.

같은 숫자끼리 묶어서 숫자별 그룹이 적은 수인 것을 뒤집으면 되는 거 아니야? 라고만 생각하고
어떻게 구현해야될지 감조차 않아 해설지를 보았다.

전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산하면 된다.
아래와 같이 해설지에 있는 풀이 방법은 이해가 된다. 꼭 다시 풀어봐야됨. 풀 수 있는지 없는지~
'''

# A03
data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대한 처리
if data[0] == '1': # 첫 번째 원소가 1이라면 count0에 1추가
  count0 += 1
else: # 0아니라 1이라고 count1에 1추가
  count1 += 1

for i in range(len(data)-1):
# 첫 번째꺼 부터 처리한 이유는 마지막 원소까지 비교할 건데 i번째께 아니라 i+1번째 값을 보기에 
  if data[i] != data[i+1]: # 만약에 두개가 달라 1인지 0인지
    if data[i+1] == '1': # 다른데 i+1번째께 1이라면 count0에 1추가
      count0 += 1
    else: # 0이라면 count1에 1추가
      count1 += 1

print(min(count0, count1)) # 0이나 1이 묶여지는 그룹 수가 더 작은게 더 적은 횟수지~