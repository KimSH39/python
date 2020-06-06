weight = int(input("체중을 입력하세요: "))
tall = int(input("키(cm)를 입력하세요: "))
tall2= tall/100
bmi = weight/tall2**2

if bmi >= 20.0 and bmi <25:
    print("표준입니다.")
else:
    print("체중관리가 필요합니다.")