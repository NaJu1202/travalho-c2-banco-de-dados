import sys
import time

from loguru import logger

from src.apps.interface import Interface

if __name__ == "__main__":
    app = Interface()

    logger.configure(
        handlers=[
            {
                "sink": sys.stdout,
                "level": "DEBUG",
                "format": "<level>{message}</level>",
            }
        ]
    )

    while True:
        try:
            app.run()
        except KeyboardInterrupt:
            logger.info("Aplicação encerrada pelo usuário.")
            sys.exit(0)
        except ValueError:
            time.sleep(5)
            continue
        except Exception as e:
            logger.error(f"Ocorreu um erro inesperado: {e}")
            sys.exit(1)
