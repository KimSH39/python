weight, tall = input("몸무게(kg)와 키(cm) 입력: ").split()

tall=float(tall)
weight=float(weight)
bmi = weight/(tall*0.01)**2

if bmi >= 20 and bmi <25:
    print("표준입니다.")
else:
    print("체중관리가 필요합니다.")
