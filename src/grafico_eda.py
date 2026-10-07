import csv
import html


ARQUIVO = "data/vendas.csv"
SAIDA = "reports/grafico_eda.svg"


def carregar_dados():
    datas = []
    vendas = []

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            datas.append(linha["data"])
            vendas.append(float(linha["vendas"]))

    return datas, vendas


def criar_grafico(datas, vendas):
    largura = 1000
    altura = 600

    margem_esquerda = 90
    margem_direita = 40
    margem_superior = 60
    margem_inferior = 100

    grafico_largura = largura - margem_esquerda - margem_direita
    grafico_altura = altura - margem_superior - margem_inferior

    minimo = min(vendas)
    maximo = max(vendas)

    escala_x = grafico_largura / (len(vendas) - 1)
    escala_y = grafico_altura / (maximo - minimo)

    pontos = []

    for i, valor in enumerate(vendas):
        x = margem_esquerda + i * escala_x
        y = margem_superior + (maximo - valor) * escala_y
        pontos.append(f"{x:.2f},{y:.2f}")

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
        width="{largura}" height="{altura}"
        viewBox="0 0 {largura} {altura}">

        <rect width="100%" height="100%" fill="white"/>

        <text x="{largura / 2}" y="35"
              text-anchor="middle"
              font-family="Arial"
              font-size="24"
              font-weight="bold">
            Evolução das Vendas
        </text>

        <line x1="{margem_esquerda}" y1="{margem_superior}"
              x2="{margem_esquerda}" y2="{altura - margem_inferior}"
              stroke="black"/>

        <line x1="{margem_esquerda}" y1="{altura - margem_inferior}"
              x2="{largura - margem_direita}" y2="{altura - margem_inferior}"
              stroke="black"/>

        <polyline points="{' '.join(pontos)}"
                  fill="none"
                  stroke="black"
                  stroke-width="4"/>

        <text x="25" y="{altura / 2}"
              text-anchor="middle"
              transform="rotate(-90 25 {altura / 2})"
              font-family="Arial"
              font-size="16">
            Vendas
        </text>

        <text x="{largura / 2}" y="{altura - 25}"
              text-anchor="middle"
              font-family="Arial"
              font-size="16">
            Data
        </text>
    '''

    for i, (data, valor) in enumerate(zip(datas, vendas)):
        x = margem_esquerda + i * escala_x
        y = margem_superior + (maximo - valor) * escala_y

        svg += f'''
        <circle cx="{x:.2f}" cy="{y:.2f}" r="5" fill="black"/>
        <text x="{x:.2f}" y="{y - 12:.2f}"
              text-anchor="middle"
              font-family="Arial"
              font-size="12">
            {valor:.0f}
        </text>
        '''

        if i % 2 == 0:
            svg += f'''
            <text x="{x:.2f}" y="{altura - 65}"
                  text-anchor="middle"
                  font-family="Arial"
                  font-size="12">
                {html.escape(data[5:])}
            </text>
            '''

    svg += "</svg>"

    with open(SAIDA, "w", encoding="utf-8") as arquivo:
        arquivo.write(svg)


def main():
    datas, vendas = carregar_dados()
    criar_grafico(datas, vendas)

    print(f"Gráfico criado com sucesso: {SAIDA}")


if __name__ == "__main__":
    main()
