<?php
/**
 * Suma de dos variables y devuelve el resultado de la suma
 * @param int $a Numero 1
 * @param int $b Numero 2
 * @return int suma de $a y $b
 * @throws Exception si algunas de las variables no es un numero
 */
function sumar($a, $b) { return $a + $b; }

/**
 * Resta de dos variables y devuelve el resultado de la resta
 * @param int $a Numero 1
 * @param int $b Numero 2
 * @return int resta de $a y $b
 * @throws Exception si algunas de las variables no es un numero
 */
function restar($a, $b) { return $a - $b; }

/**
 * Multiplicacion de dos variables y devuelve el resultado de la multiplicacion
 * @param int $a Numero 1
 * @param int $b Numero 2
 * @return int multiplcacion de $a y $b
 * @throws Exception si algunas de las variables no es un numero
 */
function multiplicar($a, $b) { return $a * $b; }

/**
 * Suma de dos variables y devuelve el resultado de la suma
 * @param int $a Numero 1
 * @param int $b Numero 2
 * @return int division de $a y $b
 * @throws DivisionByZeroError si la variable $b es 0
 */
function dividir($a, $b) {
    if ($b == 0) throw new Exception("No se puede dividir entre cero");
    return $a / $b;
}