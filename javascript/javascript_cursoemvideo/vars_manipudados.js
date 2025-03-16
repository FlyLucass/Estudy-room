let nome = window.prompt('Qual o seu nome? ')
let idade = Number(window.prompt('Qual sua idade? '))
let maior_menor = String(idade >= 18 ? "Maior de Idade" : "Menor de idade") //operador ternario sintaxe(TESTE?TRUE:FALSE)

console.log(`Seu nome é: ${nome} e você tem ${idade} anos`)
console.log(`Você e: ${maior_menor}`)
console.log(`O tipo primitivo da primeira variavel é ${typeof nome} \nDa segunda variavel é ${typeof idade} \nO tipo da terceira variavel é:${typeof maior_menor} `)

document.write(`Olá ${nome.toUpperCase()}!!! Seu nome tem ${nome.length} letras`) //mostra no body do hmtl

