from notificacaoFactory import FactoryNotificacaoUrgente, FactoryNotificacaoNormal
from servicoNotificacao import ServicoNotificacao


def main():
    print("\n" + "=" * 70)
    print("         SISTEMA DE NOTIFICAÇÃO — DEMONSTRAÇÃO (FACTORY METHOD)")
    print("=" * 70)

    print("\n[A] Envio de notificações URGENTES")
    print("-" * 70)

    urgente = FactoryNotificacaoUrgente()
    serviço_urgente = ServicoNotificacao(urgente)

    serviço_urgente.notificar(
        "+55 71 99988-7766",
        "⚠ Alerta crítico: instabilidade detectada no sistema!"
    )

    serviço_urgente.notificar(
        "@admin_suporte",
        "⚠ Intervenção necessária: latência acima do normal."
    )

    print("\n[B] Envio de notificações NORMAIS")
    print("-" * 70)

    normal = FactoryNotificacaoNormal()
    serviço_normal = ServicoNotificacao(normal)

    serviço_normal.notificar(
        "usuario@empresa.com",
        "Seu relatório mensal já está disponível para download."
    )

    serviço_normal.notificar(
        "+55 71 98877-6655",
        "Seu agendamento foi confirmado com sucesso!"
    )

    print("\n[C] Mudança dinâmica de estratégia de notificação")
    print("-" * 70)

    serviço_dinamico = ServicoNotificacao(normal)

    serviço_dinamico.notificar(
        "cliente@loja.com",
        "Seu pedido foi recebido e está sendo processado."
    )

    print("\n>> Situação mudou: mensagem agora precisa ser tratada como URGENTE.")
    serviço_dinamico.trocar_factory(urgente)

    serviço_dinamico.notificar(
        "+55 71 98765-4321",
        "⚠ Problema detectado no processamento do seu pedido."
    )

    print("\n" + "=" * 70)
    print("Execução finalizada — Demonstração concluída!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
