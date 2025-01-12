
const rl = require('readline')

const prompt = rl.createInterface({
    input: process.stdin,
    output: process.stdout

})

prompt.question('qual seu ano de nascimento: ', (resposta) => {
    console.log(`Voce nasceu em: ${resposta}`)
    prompt.close()

})




