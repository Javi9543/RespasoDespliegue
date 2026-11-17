
/**
 * Funcion que suma el numero introducido en a y el numero introducido en b
 * @param {Number} a Numero 1 
 * @param {Number} b Numero 2 
 * @returns {Number} la suma de a + b 
 */
function sumar(a, b) {
    return a + b;
}

/**
 * Funcion que resta el numero introducido en a y el numero introducido en b
 * @param {number} a Numero 1 
 * @param {Number} b Numero 2 
 * @returns {Number} la resta de a - b 
 */
function restar(a, b) {
    return a - b;
}

/**
 * Funcion que multiplica el numero introducido en a y el numero introducido en b
 * @param {Number} a Numero 1
 * @param {Number} b Numero 2
 * @returns {Number} devuelve la multiplicacion de a * b
 */
function multiplicar(a, b) {
    return a * b;
}

/**
 * Funcion que divide entre el numero introducido en a y el numero introducido en b
 * @param {Number} a Numero 1 
 * @param {Number} b Numero 2
 * @returns {Number} devuelve la division de a / b
 */
function dividir(a, b) {
    if (b === 0) throw new Error("No se puede dividir entre cero");
    return a / b;
}