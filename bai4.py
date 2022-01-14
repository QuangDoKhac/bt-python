name = str(input("Nhập tên và SBD của bạn : "))
print("Tên của bạn là : ",name);
name=name.replace(" ",",");
print("Chuoi kí tự đầu vào là : ",name);
# n=input("Nhập vào các giá trị:")
l=name.split(",")
t=tuple(l)
print (l)
print (t)