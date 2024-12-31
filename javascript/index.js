function calculando() {

    const num1 = document.getElementById("num1").value;
    const num2 = document.getElementById("num2").value;
    const op = document.getElementById("op").value;
    let valor;


    switch (op) {
        case '+':
            valor = +num1 + +num2;
            break;
        case '-':
            valor = num1 - num2;
            break;
        case '*':
            valor = num1 * num2;
            break;
        case '/':
            valor = num1 / num2;
            break;

        default: valor = "siga os padroes estabelecidos";
    }

    alert(valor);


}