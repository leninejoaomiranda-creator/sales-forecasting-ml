import csv

ARQUIVO = "data/vendas.csv"
SAIDA = "reports/grafico_vendas.svg"


def carregar_vendas():
    datas = []
    vendas = []

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            datas.append(linha["data"])
            vendas.append(float(linha["vendas"]))

    return datas, vendas


def criar_grafico(datas, vendas):
    largura = 900
    altura = 500
    margem = 70

    maior = max(vendas)
    menor = min(vendas)

    pontos = []

    for i, venda in enumerate(vendas):
        x = margem + i * (largura - 2 * margem) / (len(vendas) - 1)
        y = altura - margem - (venda - menor) * (altura - 2 * margem) / (maior - menor)
        pontos.append(f"{x:.1f},{y:.1f}")

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{largura}" height="{altura}" viewBox="0 0 {largura} {altura}">

<rect width="100%" height="100%" fill="white"/>

<text x="450" y="35" text-anchor="middle"
font-family="Arial" font-size="24" font-weight="bold">
Evolução das Vendas
</text>

<line x1="{margem}" y1="{altura-margem}"
x2="{largura-margem}" y2="{altura-margem}"
stroke="black"/>

<line x1="{margem}" y1="{margem}"
x2="{margem}" y2="{altura-margem}"
stroke="black"/>

<polyline points="{' '.join(pontos)}"
fill="none" stroke="blue" stroke-width="4"/>

"""

    for i, venda in enumerate(vendas):
        x = margem + i * (largura - 2 * margem) / (len(vendas) - 1)
        y = altura - margem - (venda - menor) * (altura - 2 * margem) / (maior - menor)

        svg += f'''
<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="blue"/>
<text x="{x:.1f}" y="{y-10:.1f}" text-anchor="middle"
font-family="Arial" font-size="12">{venda:.0f}</text>
'''

    svg += """
</svg>
"""

    with open(SAIDA, "w", encoding="utf-8") as arquivo:
        arquivo.write(svg)


def main():
    datas, vendas = carregar_vendas()
    criar_grafico(datas, vendas)

    print("Gráfico criado com sucesso!")
    print(f"Arquivo: {SAIDA}")


if __name__ == "__main__":
    main()
