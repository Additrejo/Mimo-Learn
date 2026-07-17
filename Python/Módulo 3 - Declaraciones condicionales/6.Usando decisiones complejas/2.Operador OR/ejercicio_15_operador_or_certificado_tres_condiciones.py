# Podemos usar or para agregar tantas condiciones como queramos, como
# también agregar won_competition.

average_grade = "B"
final_score = 1400
won_competition = True

if average_grade == "A" or final_score >= 1500 or won_competition:
    print("Certificate achieved!")

# Salida esperada:
# Certificate achieved!
# (won_competition es True, por lo que basta para cumplir la condición con or)
