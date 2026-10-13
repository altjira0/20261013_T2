#Queremos calcular la cuota mensual que tengo que pagar.
#La fórmula es C = V*(i*(1 + i)**N)/(((1+i)**N)-1)
capital_prestado = int(input("¿Cuánto dinero te ha prestado el Lucifer <3?(capital prestado en €):"))
#Obtener el tipo de interés: Se calcula a partir del euribor más 1 porque el banco te da eso.
#El EURIBOR es en porcentaje, es 3,354%, entonces tenemos que quitarle el porcentaje multiplicando por 100. 
#El interés necesitamos que sea mensual, entonces el interés lo dividimos por 12 meses. 
EURIBOR = 3.354
interes = EURIBOR + 1
interes_mensual = interes / 12 / 100
#Obtener el numero de cuotas
numero_anos = int(input("Cuánto tiempo vas a estar encadenado?(en años):"))
numero_cuotas = numero_anos * 12

#Calcular cuota mensual en base a fórmula de AF
cuota_menual = capital_prestado*( interes_mensual * (1 + interes_mensual )** numero_cuotas ) / (((1 + interes_mensual)**numero_cuotas)- 1)
cuota_menual = round(cuota_menual,2)
print(f"Cada mes vas a estar {cuota_menual}€ más cerca del infierno")
#Me dan la hipoteca: 
sueldo_mensual = int(input("Cuánto te dá tu patrón?(en euros):"))
#Veamos si tu sueldo da para ello.
if cuota_menual < int( 30/100 * (sueldo_mensual)):
    print("Condenda a favor")
else:
    print("Por ahora eres libre pero homeless :) :")

    