void main() {
  //Função Simples
  saudacao() {
    print('Olá!!! Seja bem-vindo');
  }

  //Função que Retorna um valor
  soma(double a, int b) {
    return a + b;
  }

  // Chamando as Funções
  saudacao();
  var resultado = soma(3.5, 5);
  print('A soma é: $resultado');

  var contador = 0;
  while (contador < 5) {
    print('Contador: $contador');
    contador++;
  }
}
