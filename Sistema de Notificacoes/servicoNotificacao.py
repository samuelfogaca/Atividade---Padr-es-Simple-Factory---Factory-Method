from notificacaoFactory import NotificacaoFactory


class ServicoNotificacao:

    def __init__(self, factory: NotificacaoFactory):

        self.factory = factory

    def notificar(self, destino: str, mensagem: str) -> bool:
        return self.factory.processar_notificacao(destino, mensagem)

    def trocar_factory(self, nova_factory: NotificacaoFactory):
        self.factory = nova_factory
        print(
            f"\n>> Estratégia de notificação atualizada para: {nova_factory.__class__.__name__}")
