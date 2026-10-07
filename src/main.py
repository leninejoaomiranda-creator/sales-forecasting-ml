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


def analisar_vendas(vendas):
    media = np.mean(vendas)
    maior = np.max(vendas)
    menor = np.min(vendas)
    total = np.sum(vendas)

    print("\n===== ANÁLISE DE VENDAS =====")
    print(f"Total de vendas: {total:.2f}")
    print(f"Média diária: {media:.2f}")
    print(f"Maior venda: {maior:.2f}")
    print(f"Menor venda: {menor:.2f}")


def prever_proxima_venda(vendas):
    dias = np.arange(len(vendas))

    coeficientes = np.polyfit(dias, vendas, 1)
    modelo = np.poly1d(coeficientes)

    proximo_dia = len(vendas)
    previsao = modelo(proximo_dia)

    print("\n===== PREVISÃO =====")
    print(f"Previsão para o próximo dia: {previsao:.2f}")


def main():
    print("==========================================")
    print(" SISTEMA DE ANÁLISE E PREVISÃO DE VENDAS")
    print("==========================================")

    datas, vendas = carregar_vendas()

    analisar_vendas(vendas)
    prever_proxima_venda(vendas)


if __name__ == "__main__":
    main()
