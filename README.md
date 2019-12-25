# Projeto
Projeto desenvolvido com intuito de realizar raspagem de 
dados do site [Cinema em Cena](https://www.cinemaemcena.com.br)

## Como Funciona?

O projeto possui um único arquivo capaz de realizar a 
raspagem de dados do site Cinema em Cena na sessão de críticas.

Os dados coletados são:
- Nome do filme
- Data de Lançamento
- Data da Crítica
- Nota do Crítico
- Nota dos Visitantes

### Rodando o projeto

Assim que realizar o download ou clonar o projeto, 
basta rodar o comando:

```bash
$ python criticas.py -p 15
```

Após isso, o script raspará as informações presentes 
nas 15 primeiras páginas.

O parâmetro '-p' é opcional, sendo que, caso não seja 
passado, ele buscará as informações presentes na primeiras 
10 páginas.

Quando o script terminar de rodar, o arquivo 
'criticas.csv' será criado com as informações coletadas.
