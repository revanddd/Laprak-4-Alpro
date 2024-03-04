celcius_to_fahrenheit = lambda C: (9/5) * C + 32
celcius_to_reamur = lambda C: 0.8 * C

input_C1 = 100
output_F1 = celcius_to_fahrenheit(input_C1)
print("Input C =", input_C1, "Output F =", output_F1)

input_C2 = 80
output_R2 = celcius_to_reamur(input_C2)
print("Input C =", input_C2, "Output R =", output_R2)

input_C3 = 0
output_F3 = celcius_to_fahrenheit(input_C3)
print("Input C =", input_C3, "Output F =", output_F3)
