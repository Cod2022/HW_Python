# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

if a > b + c or b > a + c or c > a + b:
    print("Такой треугольник невозможен!")
else:
    if a == b and a == c:
        print("Треугольник равносторонний")
    elif a != b != c:
        print("Треугольник разносторонний")
    else:
        print("Треугольник равнобедренный")




