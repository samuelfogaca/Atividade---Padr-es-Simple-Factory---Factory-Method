from file_logger import FileLogger


class ModuloEmail:
    
    def __init__(self):
        self.logger = FileLogger()

    def enviar(self, destino: str, assunto: str) -> bool:


        self.logger.info(f"Iniciando envio para '{destino}'")

        if "@" not in destino or destino.count("@") != 1:
            self.logger.error(
                f"Falha: endereço de e-mail inválido ('{destino}')")
            return False

        self.logger.info(f"E-mail enviado com sucesso para {destino}")
        return True
