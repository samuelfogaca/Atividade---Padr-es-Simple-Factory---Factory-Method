from file_logger import FileLogger
from modulo_usuario import ModuloUsuario
from modulo_pagamento import ModuloPagamento
from modulo_email import ModuloEmail


def verificar_singleton():
    print("\n" + "="*65)
    print("TESTE 1 — Verificando Unicidade do Singleton")
    print("="*65)

    a = FileLogger()
    b = FileLogger()
    c = FileLogger()

    print(f"Instância A: {id(a)}")
    print(f"Instância B: {id(b)}")
    print(f"Instância C: {id(c)}")

    if a is b is c:
        print("✔ Todas as referências apontam para a mesma instância!\n")
    else:
        print("❌ Erro: mais de uma instância detectada.\n")


def testar_niveis_log():
    print("\n" + "="*65)
    print("TESTE 2 — Registrando Mensagens em Diferentes Níveis")
    print("="*65)

    logger = FileLogger()

    logger.info("Aplicação iniciada.")
    logger.warning("Uso elevado de memória detectado.")
    logger.error("Falha ao conectar ao servidor de dados.")
    logger.info("Aplicação encerrada.")

    print("✔ Registros realizados com sucesso.\n")


def testar_modulos():
    print("\n" + "="*65)
    print("TESTE 3 — Acesso ao Logger por Múltiplos Módulos")
    print("="*65)

    print("\n[ Módulo de Usuários ]")
    usuarios = ModuloUsuario()
    usuarios.cadastrar("ana")
    usuarios.cadastrar("carlos")
    usuarios.remover("ana")

    print("\n[ Módulo de Pagamentos ]")
    pagamentos = ModuloPagamento()
    pagamentos.pagar(120.00, "Pix")
    pagamentos.pagar(85.90, "Cartão")
    pagamentos.pagar(-10, "Boleto")  # Erro esperado

    print("\n[ Módulo de E-mails ]")
    emails = ModuloEmail()
    emails.enviar("contato@empresa.com", "Bem-vindo ao sistema!")
    emails.enviar("email_invalido", "Mensagem de teste.")  # Erro esperado

    print("\n" + "="*65)
    print("CONTEÚDO DO ARQUIVO DE LOG")
    print("="*65)

    logger = FileLogger()
    print(logger.mostrar_logs())
    print("\n")


def main():
    print("\n" + "="*65)
    print("DEMONSTRAÇÃO — PADRÃO SINGLETON (FILE LOGGER)")
    print("="*65)

    verificar_singleton()
    testar_niveis_log()
    testar_modulos()

    print("="*65)
    print("Fim da execução — Verifique o arquivo 'app.log'")
    print("="*65)


if __name__ == "__main__":
    main()
