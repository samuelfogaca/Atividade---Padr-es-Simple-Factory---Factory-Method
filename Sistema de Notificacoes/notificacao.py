from abc import ABC, abstractmethod
from datetime import datetime


class Notificacao(ABC):

    def __init__(self, destino: str, mensagem: str):
        self.destino = destino
        self.mensagem = mensagem
        self.timestamp = datetime.now()

    @abstractmethod
    def enviar(self) -> bool:
        pass

    def _formatar_hora(self) -> str:
        return self.timestamp.strftime("%H:%M:%S")

    def __str__(self):
        return f"{self.__class__.__name__}(destino='{self.destino}')"


class NotificacaoEmail(Notificacao):

    def enviar(self) -> bool:
        print("\n--- ENVIO DE E-MAIL ---")
        print(f"Destinatário : {self.destino}")
        print(f"Assunto      : Aviso Automático")
        print(f"Conteúdo     : {self.mensagem}")
        print(f"Status       : ✔ Enviado às {self._formatar_hora()}")
        return True


class NotificacaoSMS(Notificacao):

    def enviar(self) -> bool:
        print("\n--- ENVIO DE SMS ---")
        print(f"Para   : {self.destino}")
        print(f"Texto  : {self.mensagem}")
        print(f"Status : ✔ Entregue às {self._formatar_hora()}")
        return True


class NotificacaoWhatsApp(Notificacao):

    def enviar(self) -> bool:
        print("\n--- ENVIO DE WHATSAPP ---")
        print(f"Contato: {self.destino}")
        print(f"Mensagem:")
        print(f"   {self.mensagem}")
        print(f"Status : ✔ Mensagem enviada às {self._formatar_hora()}")
        return True
