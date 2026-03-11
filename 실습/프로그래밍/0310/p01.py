num = input("숫자를 입력하세요.")
if '3' in num or '6' in num or '9' in num:
    print("박수 짝")
else:
    print("369숫자가 아닙니다.")


score = int(input("성적을 입력하시오."))
if score >=60:
    print("합격")
else:
    print("불합격")

card = int(input("카드 잔액을 입력하세요."))
if card >= 1000:
    print("버스 탑승 가능")
else:
    print("버스 탑승 불가능")

capt = input("보안문자를 입력하세요 : ")
if capt == "N8SHA" :
    print("비밀번호 찾기 허용")
else:
    print("비밀번호 찾기 허용 안함")

base = 270
cost = 0
use = int(input("전기 사용량(kW)입력 : "))
if use > 100:
    cost = (base * use) * 1.1
else:
    cost = (base * use)
print(f'전기 사용량 : {use} kW ')
print(f'전기 요금: {cost} 원')

id = input("id를 입력하시오.")
pwd = input("pwd를 입력하세요 : ")
if id == 'info' and pwd == 'edu':
    print("로그인 되었습니다.")
else:
    print("로그인에 실패하였습니다.")

kind = input('당신의 승객 유형은? [임산부, 노약자, 일반]')
if kind == "노약자" or kind == "일반":
    print("이용가능")
else:
    print('이용 불가능')

kind = input('당신의 승객 유형은? [임산부, 노약자, 일반]')
if not kind == "임산부": 
    print("이용가능")
else:
    print('이용 불가능')

point = int(input("점수를 입력하시오"))
if point >= 90:
    print("A")
elif point >= 80:
    print("B")
elif point >= 70:
    print("C")
else:
    print("D")

num = int(input("정수를 입력하시오"))
if num % 2==0:
    print("짝수입니다.")

else:
    print("홀수입니다.")

num = int(input("정수를 입력하시오. "))
if num > 0:
    print("양수입니다.")
elif num == 0:
    print("0입니다.")
else:
    print("음수입니다.")



age = int(input("나이를 입력하세요."))
cost = 140000
if age >= 60:
    print("30%할인 대상입니다.")
    cost = cost*0.7
elif age <= 10:
    print("20%할인 대상입니다.")
    cost = cost * 0.8
else:
    print("할인대상이 아닙니다.")

print(f'찜질방 이용요금: {cost}')

age = int(input("나이를 입력하세요."))
cost = 140000
if age > 10:
    if age >= 60:
        print("30%할인 대상입니다.")
        cost = cost*0.7
    else:
        print("할인대상이 아닙니다.")
else:
    print("20%할인 대상입니다.")
    cost = cost * 0.8
    
print(f'찜질방 이용요금: {cost}')


n1 =int(input("첫 번째 정수 :"))
n2 =int(input("두 번째 정수 :"))

if n1 > n2 :
    print(f"{n1} 이(가) 더 큽니다.")
elif n1 == n2:
    print(f"두 수가 같습니다.")
else:
    print(f"{n2} 이(가) 더 큽니다.")

a = int(input('점수를 입력하세요. '))
if a > 60:
    print('합격입니다.')
    if a > 90:
        print('장합금 대상')
else:
    print("불합격입니다.")