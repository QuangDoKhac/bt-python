name = str(input("Nhập tên của bạn : "))
n=len(name);
# n = int(input("Nhập số nguyên dương n = ")) 
print("Tên của bạn là : ",name);
print("Độ dài tên bạn là : ",n," kí tự");
danhSach = dict()
for i in range(1, n + 1):
    danhSach[i] = i * i
print (danhSach)