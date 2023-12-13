# Dados para o gráfico de barras
categorias = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D']
valores = [3, 8, 1, 10]

# Encontrar o valor máximo para normalização
max_valor = max(valores)

# Normalizar os valores para ajustar a escala
valores_normalizados = [int(40 * val / max_valor) for val in valores]

# Imprimir o gráfico de barras
for i in range(max_valor, 0, -1):
    linha = ''
    for val in valores_normalizados:
        if val >= i:
            linha += '#'
        else:
            linha += ' '
    print(linha)

# Imprimir rótulos das categorias
print(' ' * 2 + '-' * (len(valores) * 2 - 1))
rotulos = '  '.join(categorias)
print(rotulos)
