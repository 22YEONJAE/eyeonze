# 예제 1

print("세 변의 길이를 입력하시오:")
aa = input()
bb = input()
cc = input()

if aa + bb > cc or aa + cc > bb and bb + cc > aa :
  print("yes")
else :
  print("no")


# 문제 1

print("원피스의 구매 개수를 입력하시오:")
onepiece = input()
print("스웨터의 구매 개수를 입력하시오:")
sweater = input()

if (int(onepiece) * 5) + (int(sweater) * 3) < 10 : 
  suum = ((int(onepiece) * 5) + (int(sweater) * 3)) * 0.95
  print("총액:". format(suum * 10000))

elif 9 < (int(onepiece) * 5) + (int(sweater) * 3) < 20 :
  suum =  ((int(onepiece) * 5) + (int(sweater) * 3)) * 0.9
  print("총액:". format(suum * 10000))  

elif 19 < (int(onepiece) * 5) + (int(sweater) * 3) :
  suum = ((int(onepiece) * 5) + (int(sweater) * 3)) * 0.8 
  print("총액:". format(suum * 10000))


# 문제 2 : 일의 자리 수가 3,6,9 인지 여부 확인


print("임의의 정수를 입력하세요:")
jeongsu = input()

if int(jeongsu) % 10 == 3 or int(jeongsu) % 10 == 6 or int(jeongsu) % 10 == 9 : 
  print("yes")
else :
  print("no")


# 예제 2 : 자릿수의 합

print("0 ~ 1,000,000 사이의 숫자를 입력하시오:")
su = input()

aa = int(su) % 10
bb = (int(su) // 10) % 10
cc = (int(su) // 100) % 10
dd = (int(su) // 1000) % 10
ee = (int(su) // 10000) %10
ff = (int(su) // 100000) %10

suuum = int(aa) + int(bb) + int(cc) + int(dd) + int(ee) + int(ff)


print(f"{su}의 자릿수의 합은 {suuum} 입니다.")


# 문제 3 : 2 ** 0 부터 2 ** N 까지 합




# 문제 4 : 사용자가 입력한 숫자의 합


# 문제 5 : M * N  직사각형 출력

aa = input("가로 길이를 입력하시오: ")
bb = input("세로 길이를 입력하시오: ")
aa = int(aa)
bb = int(bb)


tmp = ("*" * aa) + "\n"
tmp = tmp * bb
print(tmp)


print(asdfasdfsad)

























