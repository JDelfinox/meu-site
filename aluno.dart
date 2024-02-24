// ignore_for_file: unused_import

import 'dart:io';

void main() {
  print('Digite a Porcentagem de faltas do Aluno??');
  String r1 = stdin.readLineSync() ?? '';
  double n1 = double.parse(r1);

  print('Qual foi sua Média??');
  String r3 = stdin.readLineSync() ?? '';
  double n3 = double.parse(r3);

  if (n1 >= 15 && n3 >= 6) {
    print("Parabens!!!! O Aluno foi Aprovado.");
  } else {
    print('O aluno reprovou');
  }
}
