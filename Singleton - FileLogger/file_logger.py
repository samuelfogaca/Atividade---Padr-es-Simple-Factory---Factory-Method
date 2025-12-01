from datetime import datetime
import os


class FileLogger:

    _instancia = None
    _diretorio = "Singleton-FileLogger"
    _nome_arquivo = "app.log"

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._configurado = False
        return cls._instancia

    def __init__(self):
        if not self._configurado:
            self._preparar_diretorio()
            self._caminho = os.path.join(self._diretorio, self._nome_arquivo)
            self._criar_arquivo_se_nao_existir()
            self._configurado = True
            print(
                f"[Logger] Instância inicializada — arquivo em: {self._caminho}")


    def _preparar_diretorio(self):
        if not os.path.exists(self._diretorio):
            os.makedirs(self._diretorio)

    def _criar_arquivo_se_nao_existir(self):
        if not os.path.isfile(self._caminho):
            with open(self._caminho, "w", encoding="utf-8") as arq:
                data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                arq.write(f"=== LOG INICIADO EM {data} ===\n\n")

    def _registrar(self, nivel: str, mensagem: str):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        linha = f"[{data}] [{nivel}] {mensagem}\n"

        with open(self._caminho, "a", encoding="utf-8") as arq:
            arq.write(linha)

    def info(self, mensagem: str):
        self._registrar("INFO", mensagem)
        print(f"[INFO] {mensagem}")

    def warning(self, mensagem: str):
        self._registrar("WARNING", mensagem)
        print(f"[AVISO] {mensagem}")

    def error(self, mensagem: str):
        self._registrar("ERROR", mensagem)
        print(f"[ERRO] {mensagem}")

    def mostrar_logs(self) -> str:
        with open(self._caminho, "r", encoding="utf-8") as arq:
            return arq.read()
