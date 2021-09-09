# Guia 2

## Ejercicio 1

a)

- Si K < S(T) ==> Payoff S(T)
- Si K >= S(T) ==> Payoff K

Payoff = S(T) + max(K - S(T), 0);

Ganancia = S(T) + max(K - S(T), 0) - Prima

b)

Payoff = 2 \* max(K - S(T), 0) + max(S(T) - K, 0)
Ganancia = Payoff - P1 - P2 - P3

- Si K < S(T) ==> Payoff = S(T) - K
- Si K >= S(T) ==> Payoff = 2 \* (K - S(T))

c)

Payoff = max(K1 - S(T), 0) + max(K3 - S(T), 0) - 2 \* max(K2 - S(T), 0)

- Si S(T) < K1 ===> Payoff = 0
- Si S(T) < K2 ===> Payoff = - K1 + S(T)
- Si S(T) < K3 ===> Payoff = K3 + S(T)
- otherwise ===> Payoff = 2 \* S(T)

## Ejercicio 2

a) Call cubierta, elijo la del strike 242.00. Tengo que invertir 246.55 - 7.71

b) Put protectora, elijo la del strike 255.00. Tengo que invertir 246.55 + 9.51

c) Straddle, elijo la del strike 247.00. Tengo que invertir 4.12 + 5.15

d) Butterfly spread con puts, elijo las de strike 246, 247, 248. Con las puts que vendo, pago la inversion de comprar las 2 puts necesarias, y me sobran 16 centavos

## Ejercicio 3

La estrategia para un arbitragista es pedir todos los prestamos que pueda de $500. Con cada prestamo comprar una onza de oro a $500, y entrar short en el contrato forward para cada onza. Entonces gana $600 al otro anio por cada onza, y con eso paga los $525 de cada prestamo que pidio.

La tasa para no permitir arbitraje es del 20% anual.

## Ejercicio 4

a) Payoff = K + max(S(T) - K, 0)
Ganancia = K + max(S(T) - K, 0) - c - K / (1 + i) \*\* T

b) Payoff = S(T)
Ganancia = S(T) - S(0)

Notese que

- Poner en el banco K / (1 + i) \*\* T => K - K / (1 + i) \*\* T
- Comprar una call ==> max(S(T) - K, 0) - c
- Ser short en el subyacente ==> S(0) - S(T)

K - K / (1 + i) \*\* T + max(S(T) - K, 0) - c + S(0) - S(T) <= 0
K - K / (1 + i) \*\* T + S(T) - K - c + S(0) - S(T) <= 0

- K / (1 + i) \*\* T + S(T) - c + S(0) - S(T) <= 0
- K / (1 + i) \*\* T - c + S(0) <= 0
- K / (1 + i) \*\* T + S(0) <= c

## Ejercicio 5

5 <= 64 - 58.25

Lo mismo de arriba

## Ejercicio 6

Mirar la siguiente estrategia

- Poner en el banco K / (1 + i) \*\* T
- Vender una put
- Vender la accion apenas la tenga

## Ejercicio 7

(1 + i) \*\* 12 = (1 + 0.06)

i = 0.005 (interes mensual)

Y ahora fijemonos la siguiente estrategia:

- Pedir un prestamo de $49.75 (K / (1 + i))
- Compras la accion a 47
- Comprar una put (y venderla si o si)

## Ejercicio 8

3 - 31 + 30 / (1 + 0.05) = p
p = 0.5714
