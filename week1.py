##<Q1>
다양한 데이터를 수집해서 아래와 같은 num_list를 얻었습니다.
하지만 우리에게 필요한 데이터는 홀수 데이터입니다.
그렇다면 num_list 가 홀수인 데이터만 출력하도록 하는 함수를 작성해보세요.

num_list=[1,5,7,15,16,22,28,29]

def get_odd_num(num_list):
  odd_num=[]
  for num in num_list:
    if num%2==1:
      odd_num.append(num)
  return odd_num

print(get_odd_num(num_list))


##<Q2>
데이터 처리를 위해서 문자열을 입력받았습니다. 그런데, 문자열을 받았 더니 단어 단위로 거꾸로 입력되었습니다. 이를 다시 원래대로 출력하는 함수 를 작성해보세요.😎

string 문장을 받아 단어를 역순으로 출력하는 함수를 작성하세요.
string 연산을 이용해보세요.

sentence="way a is there will a is there Where"

def reverse_setence(sentence):
  result=' '.join(reversed(sentence.split())) #split으로 공백 기준 나눈 후 리스트로 반환, 
                                              #reverse후 join으로 요소들 연결
  return result

print(reverse_setence(sentence))


##<Q3>
이번 학기의 중간고사, 기말고사 점수가 발표되었습니다. 각 학생들의 점 수가 튜플 형태로 저장되어 있고, 이를 포함한 리스트가 있습니다. 이를 이용 해 각 학생들의 평균 점수를 출력하는 함수를 제작하세요. 😎

리스트와 반복문을 사용해 데이터를 불러오세요.
이를 이용해 각 학생별 평균을 구해보세요

score=[(100,100),(95,90),(55,60),(75,80),(70,70)] #리스트 안에 튜플

def get_avg(score): 
  for idx in range(5):
    avg=sum(score[idx])/len(score[idx])
    print("{0}번, 평균:{1}".format(idx+1, avg))

get_avg(score)


##<Q4>
두개의 납품처에서 각각 과일과 야채들이 납품되었습니다. 이를 각각 물 품의 갯수를 나타내는 2개의 딕셔너리로 정리했습니다. 물품을 정리하기 위해서 2 개의 딕셔너리 객체를 합쳐 출력하는 함수를 제작하세요.😎

중복되는 물품은 합쳐서 표시하세요.
각 딕셔너리 데이터의 데이터의 키값을 이용해 중복을 확인해보세요.

from collections import Counter       #collections.Counter 사용 (value가 모두 int형일 경우일 때만 Counter 사용가능)
dict_first=Counter({'사과':30, '배':15, '감':10, '포도':10})
dict_second=Counter({'사과':5, '감':25, '배':15, '귤':25})

def merge_dict(dict_first, dict_second):
  total_count=dict_first+dict_second_count
  # sorted(dict(total_count.items()))  #key를 기준으로 오름차순으로 정렬하고자 했는데, 잘 안됨
  print(dict(total_count))      #딕셔너리 형태로 출력

merge_dict(dict_first, dict_second)


##<Q5>
inputs="cat32dog16cow5"

def find_string(inputs):
  import re
  new_string=re.sub(r'[0-9]+',' ', inputs)
  new_string_list=new_string.split()
  return new_string_list

find_string(inputs)
