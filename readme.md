# Projeto de Pesagem de Boi com UDP

Este é um projeto simples que implementa um sistema de pesagem de boi usando comunicação UDP (User Datagram Protocol). O sistema consiste em dois componentes principais: um servidor de pesagem e um cliente.

## Funcionalidades

- O servidor de pesagem recebe os pesos dos bois enviados pelo cliente via UDP e os armazena em um arquivo.
- O cliente gera pesos aleatórios para simular a pesagem dos bois e os envia para o servidor.
- O servidor processa os pesos recebidos, os soma aos pesos anteriores e os armazena em um arquivo de registro.

## Requisitos

- Python 3.x instalado no sistema.

## Como usar

1. Clone este repositório para o seu sistema local:
Em seguida, escolha pelo protocolo desejado, entre no diretório, em seguida digite `docker-compose up --build`
Ex.: `cd udp` e `docker-compose up --build`

