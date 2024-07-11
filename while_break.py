# i = 0
# while i < 1000 :
#     i = i + 1
#     if i == 500 :
#         break
#     print("대기번호는", i, "번 입니다.")
#
# else :
#     print("대기번호가 1000번 초과입니다.")

# 내가 푼 풀이1
i = 1
result = []
while i < 100 :
    i = i + 1
    if i % 2 == 1 :
        result.append(i)
print(sum(result))

# 내가 푼 풀이2
# o = 0
# i = 0
# while i < 100 :
#     i = i + 1
#     if i % 2 == 1 :
#         o = o + i
# print(o)

# 교수님의 풀이
# i 변수가 하는 역할 : 수열 만들기, 반복문 제어
# i = 1
# result = []
# while i < 100 :
#     i = i + 1
#     if i % 2 == 1 :
#         result = result + i
# print(result)
