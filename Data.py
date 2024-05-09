import pandas as pd

# Dados das músicas
nomes_musicas = ["Nightmare", "Danger Line", "Best Friend", "Voz do Coração", "Angels Fall"]
artistas = ["Avenged Sevenfold", "Avenged Sevenfold", "Froid", "Planta e Raiz", "Breaking Benjamin"]
generos = ["Rock", "Rock", "Rap", "Reggae", "Rock"]
ano_lancamento = [2010, 2010, 2020, 2002, 2015]
duracao_minutos = [6.2, 5.3, 4.1, 3.5, 3.5]

# Criando um dicionario contendo os dados
dados_musicas = {
    'Música': nomes_musicas,
    'Artista': artistas,
    'Gênero': generos,
    'Ano de Lançamento': ano_lancamento,
    'Duração (minutos)': duracao_minutos
}

# Criando um DataFrame a partir do dicionário
musicas_df = pd.DataFrame(dados_musicas)

#a) Mais ouvidas
print("- Mais ouvida: ")
mais_ouvida = musicas_df.loc[musicas_df['Ano de Lançamento'].idxmax()]['Música']
print(mais_ouvida)
print()

#b) Artista com mais músicas
print("- Artista com mais músicas:")
artistas_mais_musicas = musicas_df['Artista'].mode()[0]
print(artistas_mais_musicas)
print()

#c) Gênero mais popular
print("- Gênero mais popular:")
genero_mais_popular = musicas_df['Gênero'].mode()[0]
print(genero_mais_popular)
print()

#d) Música mais recente
print("- Música mais recente:")
musica_mais_recente = musicas_df.loc[musicas_df['Ano de Lançamento'].idxmax()]['Música']
print(musica_mais_recente)
print()

#e) Adicionar uma nova coluna com a duração em segundos
musicas_df['Duração (segundos)'] = musicas_df['Duração (minutos)'] * 60
print("e) DataFrame de Músicas com Duração em Segundos:")
print(musicas_df)
print()