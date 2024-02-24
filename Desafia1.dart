// ignore_for_file: unused_import

import 'dart:io';

void main() {
  int opcao = 0;
  while (opcao != 1) {
    print('Você se Acha Feio ou Bonito?');
    print('1-Feio \n 2-Bonito');
    print('Você tem certeza? S\N? \nNão estou certo disso!');
    String resp = stdin.readLineSync() ?? '';
    if (resp == 'S'){
      print('Você tem Espelho em Casa????');
    } else {
      print('Ataaaa!!!');
    }
  }
}
