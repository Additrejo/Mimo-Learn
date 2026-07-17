# Aquí, final_score >= 1500 es False, pero el código aún se ejecuta porque
# average_grade == "A" es True.

average_grade = "A"
final_score = 1400

if average_grade == "A" or final_score >= 1500:
    print("Certificate achieved!")

# Salida esperada:
# Certificate achieved!
