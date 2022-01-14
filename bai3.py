def kiemTra(chuoi):
    chuoi=str(chuoi);
    chuoi1=chuoi[::-1]
    if(chuoi==chuoi1):
        return True;
    else:
        return False;
name = str(input("Nhập tên của bạn : "))
list=name.split(" ")[::-1];
n=0;
x=1;
for i in range(0,len(list)):
    n+=(len(list[i])*x);
    x*=10;
print("Tên của bạn là : ",name);
print("Tên bạn có số kí tự là : ",n);
# n = int(input("Nhập số nguyên dương n = "));
ketqua=kiemTra(n)
if(ketqua):
    print("Số ",n," là số thuận nghịch")
else:
    print("Số ",n," không là số thuận nghịch")

