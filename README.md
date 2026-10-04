# Calculadora de descuentos en una tienda

Programa que calcula el precio total tras aplicar un descuento según el importe de la compra.

## 1. Análisis

### Entradas

- 'importe' : importe total de la compra en euros.
- Tipo: 'float'
- El valor debe ser mayor de 0.

### Salidas

- 'precio_final' : importe final con el descuento ya aplicado.
- Se muestra con dos decimales.

### Reglas

- Si el importe es menor a 100 el descuento aplicado es del 0%.
- Si el importe es mayor o igual a 100 y menor a 300 el descuento aplicado es del 10%.
- Si el importe es mayor o igual a 300 el descuento aplicado es del 15&.

### Restricciones

- El importe no puede ser negativo.
- El importe se expresa en euros.

## 2. Diseño

### Pseudocódigo

Algoritmo CalcularPrecioDescuento
<ul>// Entradas
    <ul>Escribir “Introduce el precio sin descuento: “</ul>
	<ul>Leer precio</ul>
// Proceso
	<ul>Si precio <= 0 Entonces
		<ul>Escribir “El precio introducido no puede ser negativo.”</ul>
	Si no si precio >= 300 Entonces
		<ul>descuento = 0.15</ul>
	Si no si precio >= 100 Entonces
		<ul>descuento = 0.10</ul>
	precio_final = precio * (1 - descuento)</ul>
// Salidas
	<ul>Escribir “El precio final con el descuento es: “, precio_final </ul>
// Fin Algoritmo</ul>

### Ordinograma

![ordinograma](https://raw.githubusercontent.com/xanmyx/ud1-practica-d3/refs/heads/main/ordinograma.jpeg?token=GHSAT0AAAAAAEK4JGQBYTG6SFWPIV62D72Q2WCPL3A)

## 4. Pruebas

| Caso | Importe | Descuento | Precio final (€) | Resultado esperado |
| --- | --- | --- | --- | --- |
| 1 | 50,00 | 0% | 50,00 | 50,00 |
| 2 | 99,99 | 0% | 99,99 | 99,99 |
| 3 | 100,00 | 10% | 90,00 | 90,00 |
| 4 | 150,00 | 10% | 135,00 | 135,00 |
| 5 | 299,99 | 10% | 269,99 | 269,99 |
| 6 | 300,00 | 15% | 255,00 | 255,00 |
| 7 | 500,00 | 15% | 425,00 | 425,00 |
| 8 | -10,00 | - | Error | El importe introducido no puede ser cero o negativo |
