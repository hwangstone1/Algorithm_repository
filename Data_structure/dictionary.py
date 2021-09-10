#대응 관계를 나타낼 수 있는 자료형
#요즘 사용하는 대부분의 언어도 이러한 대응 관계를 나타내는 자료형을 갖고 있는데,
#이를 연관 배열(Associative array) 또는 해시(Hash)라고 한다.
# 기본적인 구조 dic = { key : value }

# dictionary 쌍 추가하기
dic = {1:'firstvalue' }
dic[2] = 'secondvalue'
dic['twokey'] = 'thirdvalue'
print(dic)

del dic['twokey'] # 키가 삭제되면 value 도 동시에 삭제
print(dic)

dic = {"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "귀도":"파이썬"}
for i in dic:
    print(dic[i])
print(dic.keys()) # key 함수