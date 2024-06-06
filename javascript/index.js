// SEPARAÇÃO ENTRE PALAVRAS EX: A+""+B
//"console.log" uma forma de executar o javascript sera mostrado no console
//"document.getElementById" Outra forma de executar o javascript

function soma(valor1, valor2) { return valor1 + valor2 };
let valor = soma(1, 17);

document.getElementById("teste2").textContent = valor;
console.log(valor);

let casa_quarto = [
    "Cama",
    "Gurda-roupa",
    "Ventilador",
    "Bancada",
    "Cadeira",
    "Tv",
    "Cama do gato" //isso aquí e um array
];
document.getElementById("teste").innerHTML = casa_quarto;
console.log(casa_quarto);
casa_quarto.push("Roupas"); //Add intem
console.log(casa_quarto.length);

//"JSON" BASICAMENTE TRASFORMA TEXTO EM OBJETO(NÃO SENDO REALMENTE OBJETO MAS MANIPULANDO) OU AO CONTRÁRIO 
function PROCURAR() {
    let input = document.getElementById('CEP').value;
    const ajax = new XMLHttpRequest();
    ajax.open('get', 'https://viacep.com.br/ws/' + input + '/json/');
    ajax.send();
    ajax.onload = function () { document.getElementById('teste1').innerHTML = this.responseText; }
}

//isso aquí e um objeto
const Avião = {
    Modelo: "Airbus",
    Motorização: "CFM or IAE",
    Variante: "321,320 or 319",
    completo: function () { return "O Avião é um:" + this.Modelo + ",o motor deve ser:" + this.Motorização + ",a variante provavelmente é:" + this.Variante }
};
console.log(Avião);
document.getElementById("teste10").innerHTML = Avião.completo();
//alert(Avião.completo())
function aircraft() { alert(Avião.completo()) }
// e interresante fazer um objeto com declaração const
//JSON Acima

//A  Class sempre vem antes dos Objetos
class Aircraft {
    constructor(valor1, valor2, valor3) {
        this.Modelo = valor1;
        this.Motorização = valor2;
        this.Variante = valor3;
    }
}
const Avião2 = new Aircraft("Airbus", "CFM", "320");
console.log(Avião2)


let helloworld = "Hello World!"
console.log(helloworld);

function teste8() { alert("Olá Mundo"); }
teste8();
//vale resaltar que se uma coisa ja está colocada na function não precisa colocar novamente (ex:"alert")


var isBlue = false;
function changeBackground() {
    var body = document.body;
    if (isBlue) {
        body.style.background = "wheat"; // Mude para a cor original (branca, por exemplo)
    } else {
        body.style.background = "blue"; // Mude para a cor desejada (azul, por exemplo)
    }
    isBlue = !isBlue; // Inverte o estado

}
document.getElementById("meuBotao").addEventListener("click", changeBackground);

let number = 10;
if (number === 22) { console.log('yes, number its 22; so is very nice'); }
else if (number === 10) { console.log('yes, number its 10; so is very nice too'); }
else { console.log('number no is 22 and 10; Bad'); }

let horita = new Date();
let hora = horita.getHours();
if (hora < 12) { document.getElementById("teste3").innerHTML = "Is forenoon so good morning"; }
else if (hora < 18) { document.getElementById("teste3").innerHTML = "Is evening; so good afternoon"; }
else if (hora < 24) { document.getElementById("teste3").innerHTML = "nighttime;so good night"; }
else { document.getElementById("teste3").innerHTML = "so you life futur" };

let chamada = [
    "Carlos",
    "Joao",
    "Vitor",
    "Lucas",
    "Xubrisvaldo",
    "Ferran",
    "Hugo",
    "Malley",
    "shurek",
    "chamarrão"
];


if (chamada.length >= 4) { console.log("Eles estão no inicio:", chamada.slice(0, 4)) }
if (chamada.length >= 6) { console.log("Eles estão no meio:", chamada.slice(4, 6)) }
if (chamada.length >= 10) { console.log("Eles estão no final:", chamada.slice(6, 10)) }
if (chamada.length >= 12) { console.log("são eles:", chamada.slice(10, 12)) }
else if (chamada.length > 9) { console.log('Não tem mais ninguem na fila') }
// Bom os atributos adicionados foi o slice(pegar determinado valor) e lenght(pra identificar o numero de elementos)

for (chamada = 5; chamada < 0; chamada++) { document.getElementById("teste4").innerHTML += chamada + ", "; }
//não funcionando(repertir a matriz chamada)














