
from colorama import Fore, Style, init

init(autoreset=True)

niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

def definir_cor(nivel):
    cores = [
        Fore.RED,
        Fore.YELLOW,
        Fore.GREEN,
        Fore.CYAN,
        Fore.BLUE
    ]
    return cores[nivel - 1]

def mostrar_niveis():
    print("    CONTROLE DE NÍVEIS DE ÁGUA    ")

    for i in range(5):
        nivel = i + 1
        cor = definir_cor(nivel)

        print(cor + f"Nível {nivel}: {niveis[i]}" + Style.RESET_ALL)

mostrar_niveis()
