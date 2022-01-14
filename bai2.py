# nguyễn Quang Linh 
# MSV 1451020140
ten = input(" Nhập tên đệm:  ")
print(ten)
n = len(ten)
def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
 
n = int(input("Quang Linh thi n = "));
print("Tổng các chữ số của", n , "là", totalDigitsOfNumber(n));
