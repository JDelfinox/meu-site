// ignore_for_file: unused_import

import 'dart:io';

void main() {
  print('Digite um N°:');
  String input = stdin.readLineSync() ?? '';
  int numero = int.parse(input);

  if (numero == 0) {
    print('Nulo');
  } else if (numero > 0) {
    print('Positivo');
  } if (numero < 0 ){
    print('Negativo');
  }
}





