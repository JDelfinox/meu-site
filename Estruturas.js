function lancar_dados(){
    let numero =  1+ ((Math.round(Math.random()*100) % 6))
    return numero
}
let dados = lancar_dados()
if(dados === 6){
    console.log(`${dados},Parabéns seu cocô`)
} else if(dados === 5) {
    console.log(`${dados},Passou tirando tinta`)
}

else {
    console.log(` ${dados},Perdeu,seu otário`)
}

//Estruturas de repetição
let contador = 0 
while(dados !== 6){
    dados = lancar_dados()
    contador++
}
verifica_vencedor(dados)
console.log(contador)

do{
    console.log(`Diferença`)
    dados = lancar_dados()
}while(dados !== 6)

verifica_vencedor(dados)
console.log(console)
