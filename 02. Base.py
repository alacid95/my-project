"""
print('\nEjercicio 2\n')
var = "Hola Mundo!"
print(var)


print('\nEjercicio 3\n')
nombre = input('Introduce tu nombre: ')
print ("Hola: ", nombre)


print('\nEjercicio 4\n')
var = pow((3+2)/(2*5),2)
print(var)

print('\nEjercicio 5\n')
horas = input('Nº horas trabajadas: ')
coste = input('Coste por hora: ')
print (horas*coste)
"""

#fizzbuzz
for i in range(101):
    var = i

    if i%3 == 0:
        var = 'Fizz'
        if i%5 == 0:
            var = 'FizzBuzz'
    elif i%5 == 0:
        var = 'Buzz'
    print (var)