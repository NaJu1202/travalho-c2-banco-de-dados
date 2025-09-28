from time import sleep

from loguru import logger
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_fixed

from src.configs.menus import (
    MENU_CLIENTES,
    MENU_PRINCIPAL,
    MENU_PRODUTOS,
    MENU_RELATORIOS,
)
from src.utils.manipula_terminal import limpar_terminal, pausa_terminal, spinner


class Interface:
    def __init__(self):
        limpar_terminal()
        spinner(msg_carregamento="Iniciando aplicacao")

    def run(self):
        try:
            limpar_terminal()

            logger.success(MENU_PRINCIPAL)

            opcao_usuario = input("Informe sua opção [1 - 5]: ")

            match opcao_usuario:
                case "1":
                    self.interface_relatorios()
                case "2":
                    self.interface_produtos()
                case "3":
                    self.interface_clientes()
                case "4":
                    pass
                case "5":
                    pass
                    logger.info("Encerrando aplicação...")
                    sleep(5)
                    exit(0)
                case _:
                    raise ValueError("Opção inválida. Tente novamente.")

            pausa_terminal()
        except ValueError as e:
            logger.error(e)
            raise e
        except Exception as e:
            logger.error(f"Ocorreu um erro inesperado: {e}")
            raise e

    @retry(
        reraise=True,
        wait=wait_fixed(2),
        stop=stop_after_attempt(5),
        retry=retry_if_exception_type(ValueError),
    )
    def interface_relatorios(self):
        try:
            limpar_terminal()

            logger.success(MENU_RELATORIOS)

            opcao_usuario = input("Informe sua opção [1 - 9]: ")

            match opcao_usuario:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case "6":
                    pass
                case "7":
                    return
                case _:
                    raise ValueError("Opção inválida. Tente novamente.")

        except ValueError as e:
            logger.error(e)
            raise e
        except Exception as e:
            logger.error(f"Ocorreu um erro inesperado: {e}")
            raise e

    @retry(
        reraise=True,
        wait=wait_fixed(2),
        stop=stop_after_attempt(5),
        retry=retry_if_exception_type(ValueError),
    )
    def interface_clientes(self):
        try:
            limpar_terminal()

            logger.success(MENU_CLIENTES)

            opcao_usuario = input("Informe sua opção [1 - 4]: ")

            match opcao_usuario:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    return
                case _:
                    raise ValueError("Opção inválida. Tente novamente.")

        except ValueError as e:
            logger.error(e)
            raise e
        except Exception as e:
            logger.error(f"Ocorreu um erro inesperado: {e}")
            raise e

    @retry(
        reraise=True,
        wait=wait_fixed(2),
        stop=stop_after_attempt(5),
        retry=retry_if_exception_type(ValueError),
    )
    def interface_produtos(self):
        try:
            limpar_terminal()

            logger.success(MENU_PRODUTOS)

            opcao_usuario = input("Informe sua opção [1 - 4]: ")

            match opcao_usuario:
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    return
                case _:
                    raise ValueError("Opção inválida. Tente novamente.")

        except ValueError as e:
            logger.error(e)
            raise e
        except Exception as e:
            logger.error(f"Ocorreu um erro inesperado: {e}")
            raise e
