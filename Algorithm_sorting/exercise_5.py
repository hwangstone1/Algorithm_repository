# i 번째 스테이지 실패율 = (i번째 스테이지에있는사람 // 남은사람수)
# i+1 번째 스테이지 실패율 = (i+1번째 스테이지에 있는사람수 // 남은사람수
# 각 스테이지 인덱스가 담긴 배열을 만들고
# 각 스테이지의 실패율을 스테이지 인덱스가있는 리스트에 추가한다 .
def solution(N,stage):
    dic = {}
    result =[]
    stage_user = len(stage)
    for i in range(1,N+1):
        if stage_user == 0:
            dic[i] = 0
            continue
        else:
            cnt = stage.count(i)
            dic[i] = cnt/stage_user
            stage_user -= cnt
    dicsort = sorted(dic.items(),key = lambda x : x[1] , reverse =True)
    for i in range(len(dicsort)):
        result.append(dicsort[i][0])
    return result

N = int(input())
stages = list(map(int, input().split()))
print(solution(N,stages))