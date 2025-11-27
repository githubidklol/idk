s = input("Nhập họ tên: ")
for i in range(10):
    s = s.replace(str(i), "")
s = " ".join(s.split())
print(s.capitalize())
print("Số chữ cái:", len(s)-s.count(" "))