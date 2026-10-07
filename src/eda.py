import csv
import numpy as np

ARQUIVO = "data/vendas.csv"


def carregar_vendas():
    datas = []
    vendas = []

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            datas.append(linha["data"])
            vendas.append(float(linha["vendas"]))

    return datas, np.array(vendas)


def analise_estatistica(vendas):
    print("\n===== ANÁLISE EXPLORATÓRIA DOS DADOS =====")

    print(f"Número de observações: {len(vendas)}")
    print(f"Total de vendas: {np.sum(vendas):.2f}")
    print(f"Média: {np.mean(vendas):.2f}")
    print(f"Mediana: {np.median(vendas):.2f}")
    print(f"Desvio padrão: {np.std(vendas):.2f}")
    print(f"Valor mínimo: {np.min(vendas):.2f}")
    print(f"Valor máximo: {np.max(vendas):.2f}")
    print(f"Amplitude: {np.ptp(vendas):.2f}")


def analisar_variacao(vendas):
    variacoes = np.diff(vendas)

    print("\n===== VARIAÇÃO DIÁRIA =====")
    print(f"Maior aumento diário: {np.max(variacoes):.2f}")
    print(f"Maior redução diária: {np.min(variacoes):.2f}")
    print(f"Variação média diária: {np.mean(variacoes):.2f}")


def main():
    datas, vendas = carregar_vendas()

    analise_estatistica(vendas)
    analisar_variacao(vendas)


if __name__ == "__main__":
    main()
