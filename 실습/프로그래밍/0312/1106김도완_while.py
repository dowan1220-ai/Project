i = 1
while i <= 5:
    print('Hellow Would')
    i += 1

i = int(input())
hap = 0
while i <=5:
    print(i)
    hap += i
    i += 1
print(f'1~5까지의 합은 {hap} 이다.')

count = 0
while True:
    i = int(input("숫자를 입력하세요: "))
    count += (i)
    if count > 20:
        break
print(f"입력한 수의 합은 {count}")


count = 0
while count <= 20:
    i = int(input("숫자를 입력하세요: "))
    count += (i)

print(f"입력한 수의 합은 {count}")

point = 0
sum = 0
while sum <= 20:
    point = int(input('다트 점수를 입력하세요 : '))
    print(f'이번 점수는 {point}입니다.')
    sum += point
print(f'합계 점수는 {sum}입니다.')