"""
반 학생 N명의 이름과 , 국어 , 영어 , 수학  점수가 주어진다.
이때 다음조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.
1.국어점수가 제일 높은 순으로
2.국어점수가 같으면 영어점수가  증가하는 순으로
3.국어점수와 영어점수가 같으면 수학점수가 감소하는 순서로
3.모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
"""
n = int(input())
student = []
for i in range(n):
    student.append(input().split())
print(student)
student = sorted(student, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# - 는 내림 차순 + 는 오름차순 정렬
for i in student:
    print(i[0])