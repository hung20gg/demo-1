


print("Đây là chương trình tính tiền đóng họ")
Cost= int(input("Giá xe ô tô của bạn là: "))
current= int(input("Số tiền bạn đang có là: "))
price= Cost - current
i= float(input("Lãi suất hàng tháng là: "))
m= int(input("Thời hạn theo tháng: "))





a=1+i
b=1+i

for n in range(0,m-1):
    a=a*b
    n +=1 
    
c = (price*a)*i/(a-1)
print("Tiền lãi mà bạn phải trả hàng tháng là: ",str(round(c,3))," KVNĐ")  
