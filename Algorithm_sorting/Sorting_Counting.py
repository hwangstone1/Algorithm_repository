"""
계수정렬 counting_sort
timecomplexity = O(N+K)
반복되는 수가 많은 상황에서 사용하는게 좋음
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
array_cnt = [0]*(len(array)+1)

for i in range(len(array)):
    array_cnt[array[i]] +=1

for i in range(len(array_cnt)): # 인덱스 번호 == 숫자
     for j in range(array_cnt[i]): # array_cnt[i]의 수 == j번 만큼 출력
        print(i,end=' ')


