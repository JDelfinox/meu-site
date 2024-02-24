// ignore_for_file: unused_import

import 'dart:io';

void main() {
  print('Digite um ANO:');
  String input = stdin.readLineSync() ?? '';
  int numero = int.parse(input);

  if (numero % 4 == 0 && numero % 100 != 0 || numero % 400 == 0) {
    print('Este ano é Bissexto');
  } else {
    print('Não é um Ano Bissexto');
  }
}
