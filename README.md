# Coffee Machine Project

## Objetivo

Implementar un simulador de mAquina de cafE funcional en Python que gestione recursos, procese transacciones y permita operaciones administrativas. El proyecto demuestra programaciOn orientada a procedimientos con validaciOn de datos, gestiOn de estados y manejo de errores.

## Requerimientos

### TEcnicos
- Python 3.x
- MOdulos: `random`, `sys`, `io`, `unittest.mock`
- No requiere dependencias externas

### Funcionales
- GestiOn de recursos: agua, leche, granos, vasos
- MenU de cafE: espresso ($4), latte ($7), cappuccino ($6)
- Sistema de pagos con cambio automAtico
- Operaciones administrativas con contraseNa
- ValidaciOn de entrada y manejo de errores
- LImites mAximos de recursos

## Estructura del Proyecto

```
Coffee-Machine/
-> main.py                      # Interfaz de usuario y menU principal
-> coffee_machine.py            # LOgica central de la mAquina
-> machine_operations.py        # Operaciones auxiliares y validaciOn
-> test_coffee_machine.py       # Tests fijos predefinidos
-> test_random_coffee_machine.py # Tests aleatorios variables
-> README.md                    # DocumentaciOn
```

## Funcionalidades

1. **Visualizar estado** - Recursos disponibles y dinero
2. **Rellenar mAquina** - ANadir recursos con validaciOn de lImites
3. **Comprar cafE** - SelecciOn, pago y preparaciOn automAtica
4. **Depositar dinero** - FunciOn administrativa
5. **Retirar dinero** - Con contraseNa y opciOn de caridad
6. **ValidaciOn completa** - Recursos suficientes y pagos vAlidos

## Uso

### EjecuciOn Principal
```bash
python main.py
```

### Tests Aleatorios
```bash
python test_random_coffee_machine.py
```

## Ejemplo de EjecuciOn de Tests Aleatorios

### 6 Casos de Uso Ejecutados:

**Caso 1: Rellenar MAquina**
- Estado inicial: 87g beans, 2 cups, 856ml water, 332ml milk
- Inputs aleatorios: +24g beans, +636ml water, +407ml milk, +8 cups
- Resultado: 111g beans, 10 cups, 1492ml water, 739ml milk

**Caso 2: Compra Exitosa**
- SelecciOn aleatoria: Cappuccino ($6)
- Pago: $6 (exacto)
- Resultado: CafE entregado, recursos descontados, +$6 en mAquina

**Caso 3: Recursos Insuficientes**
- Estado crItico: 28g beans, 0 cups, 139ml water, 127ml milk
- Intento: Latte (requiere 350ml water, 20g beans)
- Resultado: "One, or more, ingredients are missing" - sin cambios

**Caso 4: Pago Insuficiente**
- SelecciOn: Cappuccino ($6)
- Pago insuficiente: $2
- Resultado: "Insufficient payment. Money returned" - sin cambios

**Caso 5: Operaciones Admin**
- Estado inicial: $57
- DepOsito aleatorio: +$48 = $105 total
- Retiro aleatorio: $12 a caridad
- Resultado: $93 final

**Caso 6: Estado Aleatorio**
- GeneraciOn aleatoria: 124g beans, 2 cups, 1203ml water, 777ml milk, $74
- Muestra variabilidad en condiciones iniciales

## CaracterIsticas TEcnicas

- **ValidaciOn robusta** de entradas numEricas
- **GestiOn de estados** consistente
- **LImites mAximos** respetados automAticamente
- **Manejo de errores** sin crashes
- **Tests exhaustivos** con casos edge
- **Aleatoriedad real** usando timestamps

## ContraseNa Administrativa

Password por defecto: `1234`