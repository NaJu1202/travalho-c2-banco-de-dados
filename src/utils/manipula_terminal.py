"""Classe responsavel por manipular o terminal."""

import os
import time

from tqdm import tqdm


def limpar_terminal() -> None:
    """Limpa o terminal."""
    os.system("cls" if os.name == "nt" else "clear")


def spinner(msg_carregamento: str) -> None:
    """Exibe um spinner de carregamento no terminal."""
    for _ in tqdm(range(100), desc=msg_carregamento, colour="red"):
        time.sleep(0.03)


def pausa_terminal() -> None:
    """Pausa o terminal até que o usuário pressione Enter."""
    input("Pressione Enter para continuar...")
