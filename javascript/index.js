function calculando() {

    var num1 = document.getElementById("num1").value;
    var num2 = document.getElementById("num2").value;
    var op = document.getElementById("op").value;
    var valor;

    switch (op) {
        case '+':
            valor = num1 + num2;
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