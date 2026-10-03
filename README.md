1. Análisis 
Entradas: precio
Salidas: precio_final
Restricciones: 
  - No se permite introducir precios negativos.
  - Según el precio se varía el porcentaje del descuento aplicado.

2. Diseño
Pseudocódigo
	Algoritmo CalcularPrecioDescuento
		//Entradas
		Escribir “Introduce el precio sin descuento: “
		Leer precio
		// Proceso
		Si precio <= 0 Entonces
			Escribir “El precio introducido no puede ser negativo.”
		Si no si precio >= 300 Entonces
			descuento = 0.15
		Si no si precio >= 100 Entonces
			descuento = 0.10
    precio_final = precio * (1 - descuento)
    //Salidas
	  Escribir “El precio final con el descuento es: “, precio_final
    //Fin Algoritmo
Ordinograma
               ┌─────────────┐
               │   INICIO    │
               └──────┬──────┘
                      │
                      ▼
               ┌─────────────┐
               │ Leer        │
               │ precio      │
               └──────┬──────┘
                      │
                      ▼
             ┌──────────────────┐
             │   ¿precio < 0?   │
             └───┬─────────┬────┘
                Sí         No
                 │         │
                 ▼         ▼
       ┌──────────────┐ ┌──────────────┐
       │ Mostrar      │ │ ¿importe >=  │
       │ "Error"      │ │    300?      │
       └──────┬───────┘ └──┬───────┬───┘
              │           Sí       No
              │            │       │
              │            ▼       ▼
              │      ┌─────────┐ ┌──────────────────┐
              │      │15 %     │ │ ¿importe >= 100? │
              │      │descuento│ └──┬───────────┬───┘
              │      └────┬────┘    │           │
              │           │        Sí           No
              │           │         │           │
              │           │         ▼           ▼
              │           │    ┌─────────┐ ┌─────────┐
              │           │    │10 %     │ │ 0 %     │
              │           │    │descuento│ │descuento│
              │           │    └────┬────┘ └────┬────┘
              │           │         │           │
              │           └─────────┴───────────┘
              │                     │
              │                     ▼
              │              ┌──────────────┐
              │              │ Calcular     │
              │              │ precio final │
              │              └──────┬───────┘
              │                     │
              │                     ▼
              │              ┌──────────────┐
              │              │ Mostrar      │
              │              │ resultado    │
              │              └──────┬───────┘
              │                     │
              └─────────────────────┤
                                    ▼
                             ┌─────────────┐
                             │     FIN     │
                             └─────────────┘

4. Pruebas
 Caso     Importe (€)	  Descuento	    Cálculo    	        Resultado esperado
  1	         0,00	         —	        Importe inválido	         Error
  2         99,99	         0 %	      99,99 × 1	                 99,99 €
  3        100,00	        10 %	      100 × 0,90	               90,00 €
  4        150,00	        10 %	      150 × 0,90	              135,00 €
  5	       300,00	        15 %	      300 × 0,85	              255,00 €
  6        500,00	        15 %	      500 × 0,85	              425,00 €
  7	       -10,00	         —	        Importe inválido	         Error
