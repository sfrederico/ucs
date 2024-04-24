"""Exploring the Spotify dataset with Pandas functions"""
import matplotlib.pyplot as plt
import pandas as pd


def list_music_same_birthday(df):
    """List the songs with the same release date"""
    new_df = df[['track_name', 'artist(s)_name', 'released_day', 'released_month', 'released_year']].copy()
    new_df['release_date'] = new_df['released_month'].astype(str) + '-' + new_df['released_day'].astype(str)
    grouped = new_df.groupby('release_date')
    date = '7-8'
    new_df = grouped.get_group(date)
    new_df = new_df[['track_name', 'artist(s)_name', 'released_day', 'released_month', 'released_year']]
    print('Músicas com o mesmo aniversário:')
    print(new_df)

def list_artist_with_more_than_noe_million_streams(df):
    """List the artists with more than one million streams"""
    df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
    df = df[df['streams'] > 1000000]
    df = df.sort_values(by='streams', ascending=False)
    df = df[['artist(s)_name', 'track_name', 'streams']]
    df = df.head(10)
    return df

def graph_streams_by_year(df):
    """Plot a bar graph with the average streams by year of release"""
    df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
    df['released_year'] = pd.to_datetime(df['released_year'], format='%Y')
    average_streams_by_year = df.groupby(df['released_year'].dt.year)['streams'].mean()
    average_streams_by_year.plot(kind='bar', color='skyblue', figsize=(15, 6))
    plt.xlabel('Ano de Lançamento')
    plt.ylabel('Total de Streams')
    plt.title('Distribuição dos Streams ao Longo dos Anos')
    plt.show()

def group_by_year(df):
    """Group the dataframe by the year of release and calculate the average the streams by year """
    print('Agrupando por ano de lançamento e calculando a média de streams por ano:')
    df['streams'] = pd.to_numeric(df['streams'], errors='coerce')
    df['released_year'] = pd.to_datetime(df['released_year'], format='%Y')
    average_streams_by_year = df.groupby(df['released_year'].dt.year)['streams'].mean()
    return average_streams_by_year

def check_values(df):
    """Verify if the values in the dataframe are correct or null"""
    print('Colunas com valores nulos:')
    null_counts = df.isnull().sum()
    columns_with_nulls = null_counts[null_counts > 0]
    print(columns_with_nulls)
    print(df.info())


def main():
    """Main function to call the other functions"""
    df = pd.read_csv('spotify-2023.csv', encoding='latin-1')
    print('\n##########################################\n')
    print('1 - Listar músicas com o mesmo aniversário')
    print('2 - Listar artistas com mais de 1 milhão de streams')
    print('3 - Gráfico de streams por ano')
    print('4 - Agrupar por ano')
    print('5 - Verificar valores nulos')
    print('6 - Sair')
    option = input('Digite a opção desejada: ')
    while option != '6':
        if option == '1':
            list_music_same_birthday(df)
        elif option == '2':
            print(list_artist_with_more_than_noe_million_streams(df))
        elif option == '3':
            graph_streams_by_year(df)
        elif option == '4':
            print(group_by_year(df))
        elif option == '5':
            check_values(df)
        else:
            print('Opção inválida!')
        option = input('Digite a opção desejada: ')
    print('Fim do programa!')



if __name__ == "__main__":
    main()
