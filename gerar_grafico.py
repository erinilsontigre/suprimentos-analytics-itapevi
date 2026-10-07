import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------------------------------------
# 1. ESTRUTURAÇÃO E TRATAMENTO DOS DADOS (PANDAS)
# ---------------------------------------------------------
dados = {
    "Frente Operacional": [
        "Compras / Ganho de Escala",
        "Perdas, Avarias e Vencimentos",
        "Combustível e Rodagem de Frota",
    ],
    "Situação Atual (R$)": [45000000.00, 2700000.00, 1200000.00],
    "Com o Projeto (R$)": [39600000.00, 400000.00, 840000.00],
}

df = pd.DataFrame(dados)

# Cálculo automatizado das métricas de economia
df["Economia Anual (R$)"] = (
    df["Situação Atual (R$)"] - df["Com o Projeto (R$)"]
)
df["Redução (%)"] = (
    df["Economia Anual (R$)"] / df["Situação Atual (R$)"]
) * 100

# Totais gerais
total_atual = df["Situação Atual (R$)"].sum()
total_projeto = df["Com o Projeto (R$)"].sum()
total_economia = df["Economia Anual (R$)"].sum()
total_reducao = (total_economia / total_atual) * 100

linha_total = pd.DataFrame(
    [{
        "Frente Operacional": "TOTAL GERAL",
        "Situação Atual (R$)": total_atual,
        "Com o Projeto (R$)": total_projeto,
        "Economia Anual (R$)": total_economia,
        "Redução (%)": total_reducao,
    }]
)

df_completo = pd.concat([df, linha_total], ignore_index=True)

# Exibição no terminal para conferência de dados
print("\n=== VALIDAÇÃO DE DADOS: PROJETO SUPRIMENTOS ITAPEVI ===")
print(df_completo.to_string(index=False))

# ---------------------------------------------------------
# 2. GERAÇÃO E EXPORTAÇÃO DO GRÁFICO (MATPLOTLIB)
# ---------------------------------------------------------
plt.style.use("ggplot")
fig, ax = plt.subplots(figsize=(10, 6))

categorias = df["Frente Operacional"]
x = range(len(categorias))
largura = 0.35

barras1 = ax.bar(
    [i - largura / 2 for i in x],
    df["Situação Atual (R$)"] / 1e6,
    largura,
    label="Situação Atual",
    color="#d9534f",
)
barras2 = ax.bar(
    [i + largura / 2 for i in x],
    df["Com o Projeto (R$)"] / 1e6,
    largura,
    label="Com o Projeto (Suprimentos)",
    color="#5cb85c",
)

ax.set_ylabel("Valor em Milhões de Reais (R$ Mi)", fontsize=12)
ax.set_title(
    "Impacto Financeiro do Projeto de Suprimentos - Itapevi",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
ax.set_xticks(list(x))
ax.set_xticklabels(categorias, fontsize=10)
ax.legend(fontsize=11)


def adicionar_rotulos(barras):
    for barra in barras:
        altura = barra.get_height()
        ax.annotate(
            f"R$ {altura:.1f}M",
            xy=(barra.get_x() + barra.get_width() / 2, altura),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )


adicionar_rotulos(barras1)
adicionar_rotulos(barras2)

plt.tight_layout()

# Exporta a imagem em alta resolução para o repositório/relatório
plt.savefig("grafico_economia_itapevi.png", dpi=300)
print(
    "\n✓ Sucesso: Imagem 'grafico_economia_itapevi.png' gerada e validada!"
)
plt.show()