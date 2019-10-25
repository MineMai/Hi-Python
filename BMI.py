weight = input('請輸入體重：')
height = input('請輸入身高：')

weight = float(weight)
height = float(height)

BMI = weight/(height * height) * 10000


print('你的BMI是', BMI)