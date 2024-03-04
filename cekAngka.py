def cek_angka(a, b, c):
    if a == b or a==c or b==c :
        return False
    if a + b == c or a + c == b or b + c == a:
        return True
    else:
        return False
    
number1 = 6
number2 = 2
number3 = 8

hasil_cek = cek_angka(number1, number2, number3)
print (hasil_cek)