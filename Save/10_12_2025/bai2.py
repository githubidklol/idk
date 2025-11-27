h, m = map(float, input("Nhập vào chiều cao và cân nặng: ").split())
bmi = m/(h*h) #tính chỉ số BMI
print(f'Chiều cao: {h}, Cân nặng: {m}, BMI: {bmi}')