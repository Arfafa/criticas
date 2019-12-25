import argparse
import requests
import pandas as pd
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-p',
                    '--pages',
                    default=10,
                    type=int,
                    help='Número de páginas a serem percorridas. Default 10')

args = parser.parse_args()


def main():

    columns = ['Nome',
               'Lançamento',
               'Data da Crítica',
               'Nota do Crítico',
               'Nota dos Visitantes']

    df = pd.DataFrame(columns=columns)

    url = 'https://www.cinemaemcena.com.br/critica?page='

    index = 0

    for count in range(1, args.pages+1):

        page = requests.get(url+str(count))
        soup = BeautifulSoup(page.content, 'html.parser')

        for filme in soup.find_all('div', class_='critica-item'):
            name = filme.find('h3').text.strip()

            info_list = [x.text.split(':')[-1].strip()
                         for x in filme.find_all('li')]

            info_list = [name]+info_list

            df.loc[index] = info_list
            index += 1

    df.to_csv('criticas.csv', index=False)


if __name__ == '__main__':
    main()
