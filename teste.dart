void main(){
  print('Sextouuuuuuuuuu Rapaziada!!!!!!!!!');
  int idade = 17;
  String nome = 'Delfino';
  bool goleiro = true;
  print(idade);
  print(nome);
  print(goleiro);
  print('Cadê o Estádio Varmengo???');
  int a = 31, b = 29, r = 0;
  r = a + b;
  print(r); 
  List<int> numeros = [1,2,3,4,5];
  print('primeiro numero é: ${numeros[0]}');
  for (var i = 0; i < numeros.length; i++) {
    print('Número do Indice $i: ${numeros[i]}');
  }
  Map<String, int> idadeporpessoa = {
    'Delfino': 16,
    'Lorival': 19,
    'Weslley': 29,
    'Pinscher de Dondoca': 24
  };
  idadeporpessoa.forEach((nome, idade) { 
    print('$nome: $idade anos');
  });

}
