from file_logger import FileLogger


class ModuloUsuario:

    def __init__(self):
        self.logger = FileLogger()

    def cadastrar(self, nome: str) -> bool:

        self.logger.info(f"Pedido de cadastro recebido para: '{nome}'")

        if not nome or nome.strip() == "":
            self.logger.error("Falha no cadastro: nome fornecido é inválido.")
            return False

        self.logger.info(f"Usuário '{nome}' cadastrado com sucesso.")
        return True

    def remover(self, nome: str):
        self.logger.warning(f"Iniciando remoção do usuário '{nome}'")
        self.logger.info(f"Usuário '{nome}' removido do sistema.")
