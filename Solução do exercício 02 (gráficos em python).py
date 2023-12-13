import random

# Gerar 1000 pontos seguindo a distribuição normal
media = 20
desvio_padrao = 2
pontos = [int(random.gauss(media, desvio_padrao)) for _ in range(1000)]

# Calcular as frequências dos valores gerados
frequencias = {}
for ponto in pontos:
    frequencias[ponto] = frequencias.get(ponto, 0) + 1

# Encontrar o valor máximo para normalização
max_frequencia = max(frequencias.values())

# Normalizar as frequências para ajustar a escala
frequencias_normalizadas = {k: int(40 * v / max_frequencia) for k, v in frequencias.items()}

# Imprimir o histograma
for i in range(max_frequencia, 0, -1):
    linha = ''
    for valor, freq in frequencias_normalizadas.items():
        if freq >= i:
            linha += '#'
        else:
            linha += ' '
    print(linha)

# Imprimir rótulos dos valores
print(' ' * 2 + '-' * (len(frequencias_normalizadas) * 2 - 1))
rotulos = '  '.join(map(str, frequencias_normalizadas.keys()))
print(rotulos)
