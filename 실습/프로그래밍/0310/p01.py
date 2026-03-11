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
    print(로그인 되었습니다.)