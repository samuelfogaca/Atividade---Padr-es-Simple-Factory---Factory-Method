from abc import ABC, abstractmethod
from notificacao import (
    Notificacao,
    NotificacaoEmail,
    NotificacaoSMS,
    NotificacaoWhatsApp
)


class NotificacaoFactory(ABC):

    @abstractmethod
    def criar_notificacao(self, destino: str, mensagem: str) -> Notificacao:
        pass

    def processar_notificacao(self, destino: str, mensagem: str) -> bool:
        notificacao = self.criar_notificacao(destino, mensagem)

        print("\n" + "=" * 60)
        print(f"Iniciando processamento da notificação:")
        print(f" - Tipo: {notificacao.__class__.__name__}")
        print(f" - Destino: {notificacao.destino}")
        print("=" * 60)

        return notificacao.enviar()


class FactoryNotificacaoUrgente(NotificacaoFactory):

    def criar_notificacao(self, destino: str, mensagem: str) -> Notificacao:
        mensagem_urgente = f"[URGENTE] {mensagem}"

        if '@' in destino and '.' not in destino:
            print("[Factory Urgente] Selecionado: WhatsApp")
            return NotificacaoWhatsApp(destino, mensagem_urgente)

        print("[Factory Urgente] Selecionado: SMS")
        return NotificacaoSMS(destino, mensagem_urgente)


class FactoryNotificacaoNormal(NotificacaoFactory):

    def criar_notificacao(self, destino: str, mensagem: str) -> Notificacao:
        if '@' in destino and '.' in destino:
            print("[Factory Normal] Selecionado: E-mail")
            return NotificacaoEmail(destino, mensagem)

        print("[Factory Normal] Selecionado: WhatsApp")
        return NotificacaoWhatsApp(destino, mensagem)
