# Guia 1

## Ejercicio 1

Payoff = max(S(T) - 50, 0)
Ganancia = Payoff - 2.50

Solo gana si el precio sube mas de 52.50

## Ejercicio 2

Payoff = - max(60 - S(T), 0)
Ganancia = Payoff + 4

La opcion es ejercicida solo si el precio es mayor que 60

Siempre y cuando el precio sea mayor a 56, el chabon gana

## Ejercicio 3

PayoffCall = max(S(T) - 45, 0)
PayoffPut = max(40 - S(T), 0)

GananciaTotal = max(S(T) - 45, 0) + max(40 - S(T), 0) - 3 - 4

El chabon espera que el precio suba o baje mucho (mas de 45, menos de 40)
En el intervalo [40, 45], esta "seguro" solo pierde 7 pesos

## Ejercicio 4

a) ???
Payoff = max(S(T) - K, 0) + max(K - S(T), 0)

b) Payoff = max(S(T) - K, 0) + max(K - S(T), 0)

c) Payoff = max(S(T) - K1, 0) - max(S(T) - K2, 0)

d) Payoff = max(S(T) - K1, 0) + max(S(T) - K2, 0) - 2 \* max(S(T) - K, 0)

## Ejercicio 5

a) Puede comprarse 100 acciones, sino puede comprar 94 opciones call

b)
GananciaAcciones = 100 - (S(T) - 94)
GananciaCall = 94 - max(S(T) - 95, 0) - 441.8

c) Las acciones tienen que subir hasta 99.7

## Ejercicio 6

a) Hace un contrato forward para comprar X libras con 2.000.000 de usd
b) ????

## Ejercicio 7

## Ejercicio 8

Le conviene ser long en una opcion put

Payoff = S(T) + max(K - S(T), 0)

Si el precio es mayor a K, entonces no vende y se queda con S(T)
Sino, el precio bajo, y entonces vende a K cada accion

## Ejercicio 9

a) Al chabon le conviene comprar todas las calls que pueda, e inmediatamente vender la misma cantidad de libras por forward a 180 dias.

Va a terminar pagando 1.59 dolares cada libra, y recibir 1.6018 por cada libra luego. Es decir, 0.118 de ganancia por libra

b) En este caso le conviene comprar por forward todas las libras que pueda a 90 dias. Luego comprar la misma cantidad de opciones put para venderlas a 1.64 cada una. En total, la ganancia es de 1.64 - 0.02 - 1.6056 = 0.0144 por libra que compre
