def tach(n):
    result=0;
    list=[];
    while(n>0):
        list.append(int(n%10))
        n=int(n/10);
    return list;
name = str(input("Nhập tên của bạn : "))
n=len(name);
print("Tên của bạn là : ",name);
print("Độ dài tên bạn là : ",n," kí tự");
# n = int(input("Nhập số nguyên dương n = "));
list=tach(n)[::-1];
sb="";
total=0;
for i in range (0,len(list)):
    total+=list[i];
    if(i== len(list)-1):
        sb+=str(list[i])+" = "+str(total);
    else:
        sb+=str(list[i])+" + ";
print("Kết quả:", sb);
