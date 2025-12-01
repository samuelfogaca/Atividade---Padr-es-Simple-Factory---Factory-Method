
# README — Atividade de Python

## Padrões: Factory Method e Singleton

Este projeto é uma atividade prática onde implementei dois padrões de projeto em Python:

* Sistema de Notificações usando Factory Method
* Sistema de Log em Arquivo usando Singleton (FileLogger)

# 📌 1. Sistema de Notificações (Factory Method)

Implementei um sistema onde o envio de notificações é feito através de factories.
Cada factory cria o tipo certo de notificação (e-mail, SMS, WhatsApp, etc).

### Como funciona:

* Existe uma classe base `Notificacao`.
* Existem notificações concretas (Email, SMS, WhatsApp).
* As fábricas (`NotificacaoFactory`) decidem qual notificação criar.
* O serviço (`ServicoNotificacao`) usa a factory para enviar mensagens.

# 📌 2. FileLogger (Singleton)

Aqui implementei um logger que sempre grava as mensagens em um único arquivo.

O padrão Singleton garante que:

✔ Só existe UMA instância do logger no programa inteiro.
✔ Todos os módulos usam o mesmo arquivo `app.log`.
✔ Os logs nunca se misturam ou criam instâncias duplicadas.

O logger escreve mensagens com:

* `info()`
* `warning()`
* `error()`

Ele cria uma pasta chamada "Singleton - FileLogger" e dentro dela o arquivo app.log.

# 📌 3. Outros módulos que usam o Logger

Para testar o Singleton, fiz três módulos simples que usam o logger:

* `ModuloUsuario`
* `ModuloPagamento`
* `ModuloEmail`

Eles só registram mensagens no arquivo, como:

* cadastrar usuário
* enviar email
* processar pagamento


