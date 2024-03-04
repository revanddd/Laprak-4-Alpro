def cek_digit_belakang(a, b, c):

    digit_a = str(a)[-1]
    digit_b = str(b)[-1]
    digit_c = str(c)[-1]

    if digit_a == digit_b or digit_a == digit_c or digit_b == digit_c:
        return True
    else :
        return False
    
input_a = int(input("masukkan bilangan a"))
input_b = int(input("masukkan bilangan b"))
input_c = int(input("masukkan bilangan c"))

hasil_digit = cek_digit_belakang(input_a, input_b, input_c)
print(hasil_digit)