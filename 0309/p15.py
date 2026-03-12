#점수가 70점 이상 합격 그외 불합격
#그중 90점 이상 장학금

score = int(input("점수를 입력하시오...."))
if score >= 70:
    if score >= 90:
        print("장합금 예상")
    else:
        print("합격")
else:
    print("불합격")
