from file_logger import FileLogger


class ModuloPagamento:

    def __init__(self):
        self.logger = FileLogger()

    def pagar(self, valor: float, metodo: str) -> bool:

        self.logger.info(
            f"Tentando processar pagamento de R${valor:.2f} via {metodo}")

        if valor <= 0:
            self.logger.error(
                f"Operação rejeitada: valor não permitido (R${valor:.2f})")
            return False
        
        if valor > 10000:
            self.logger.warning(
                f"Atenção: valor elevado detectado (R${valor:.2f})")

        self.logger.info("Pagamento concluído com sucesso.")
        return True
