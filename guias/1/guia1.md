# Guia 1

## Ejercicio 1

TODO

## Ejercicio 2

```
a) $60000
b) -$110000
```

## Ejercicio 3

Asumiendo que siempre es el 10%

```
a) $960
b) -$760
```

## Ejercicio 4

Compro 10.000.000 de yenes a un precio `x`, pero el precio en ese dia fue de `S(1 de enero de 2018)`.

`X = 10.000.000 * (S(1 de enero de 2018) - x)`

Vendo 10.000.000 de yenes a un precio `y`, pero el precio en ese dia fue de `S(1 de enero de 2018)`

`Y = 10.000.000 * (y - S(1 de enero de 2018))`

Entonces el payoff de la estrategia es

`X + Y = 10.000.000 * (y - x)`

## Ejercicio 5

Si el precio es menor a 230 centavos, llega a margin call

Si el precio es 280 centavos, la ganancia es de $1500

## Ejercicio 6

| Dia | Cotizacion | Ganancia | Ganancia Acumulada | Cuenta margen | Margin call |
| :-: | ---------: | -------: | -----------------: | ------------: | ----------: |
|  1  |        600 |        0 |                  0 |          4000 |           0 |
|  2  |      596.1 |  (780.0) |            (780.0) |        3220.0 |           0 |
|  3  |      598.2 |    420.0 |            (360.0) |        3640.0 |           0 |
|  4  |      597.1 |  (220.0) |            (580.0) |        3420.0 |           0 |
|  5  |      596.7 |   (80.0) |            (660.0) |        3340.0 |           0 |
|  6  |      595.4 |  (260.0) |            (920.0) |        3080.0 |           0 |
|  7  |      593.3 |  (420.0) |           (1340.0) |        2660.0 |      1340.0 |
|  8  |      593.6 |     60.0 |           (1280.0) |        4060.0 |           0 |
|  9  |      591.8 |  (360.0) |           (1640.0) |        3700.0 |           0 |
| 10  |      592.7 |    180.0 |           (1460.0) |        3880.0 |           0 |
| 11  |      587.0 | (1140.0) |           (2600.0) |        2740.0 |      1260.0 |
| 12  |      587.0 |      0.0 |           (2600.0) |        4000.0 |           0 |

Payoff short = 4000 - (4000 + 1340 + 1260) = -2600

| Dia | Cotizacion | Ganancia | Ganancia Acumulada | Cuenta margen | Margin call |
| :-: | ---------: | -------: | -----------------: | ------------: | ----------: |
|  1  |        600 |        0 |                  0 |          4000 |           0 |
|  2  |      596.1 |    780.0 |              780.0 |        4780.0 |           0 |
|  3  |      598.2 |  (420.0) |              360.0 |        4360.0 |           0 |
|  4  |      597.1 |    220.0 |              580.0 |        4580.0 |           0 |
|  5  |      596.7 |     80.0 |              660.0 |        4660.0 |           0 |
|  6  |      595.4 |    260.0 |              920.0 |        4920.0 |           0 |
|  7  |      593.3 |    420.0 |             1340.0 |        5340.0 |           0 |
|  8  |      593.6 |   (60.0) |             1280.0 |        5280.0 |           0 |
|  9  |      591.8 |    360.0 |             1640.0 |        5640.0 |           0 |
| 10  |      592.7 |  (180.0) |             1460.0 |        5460.0 |           0 |
| 11  |      587.0 |   1140.0 |             2600.0 |        6600.0 |           0 |
| 12  |      587.0 |      0.0 |             2600.0 |        6600.0 |           0 |

Payoff long = 6600 - (4000) = 2600

## Ejercicio 7

| Dia | Cotizacion | Ganancia | Ganancia Acumulada | Cuenta margen | Margin call |
| :-: | ---------: | -------: | -----------------: | ------------: | ----------: |
|  1  |        500 |        0 |                  0 |           200 |           0 |
|  2  |        480 |    (200) |              (200) |             0 |         200 |
|  3  |        490 |      100 |              (100) |           300 |           0 |
|  4  |        530 |      400 |                300 |           700 |           0 |
|  5  |        580 |      500 |                800 |          1200 |           0 |
|  6  |        520 |    (600) |                200 |           600 |           0 |
|  7  |        490 |    (300) |              (100) |           300 |           0 |

Payoff short = 300 - (200 + 200) = -100