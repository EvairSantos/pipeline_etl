# Projeto de Pipeline ETL para Dados de Bitcoin

![Bitcoin](https://bitcoin.org/img/icons/opengraph.png)

Este projeto demonstra a configuração e implementação de um pipeline ETL para coletar, transformar e armazenar informações sobre o Bitcoin. O pipeline permite a extração de dados em tempo real sobre o preço do Bitcoin e a realização de análises simples sobre tendências de mercado.

## Sumário

- [Instruções de Uso](#instruções-de-uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Requisitos](#requisitos)
- [Configuração](#configuração)
- [Extração de Dados](#extração-de-dados)
- [Transformação de Dados](#transformação-de-dados)
- [Carga de Dados](#carga-de-dados)
- [Contribuições](#contribuições)
- [Licença](#licença)

## Instruções de Uso

1. Clone este repositório:


2. Instale as bibliotecas necessárias (se aplicável).

3. Execute os scripts na seguinte ordem:

- [ExtrairDados.py](ExtrairDados.py): Coleta informações em tempo real sobre o Bitcoin.
- [TransformarDados.py](TransformarDados.py): Realiza uma análise simples das tendências de mercado.
- [CarregarDados.py](CarregarDados.py): Carrega os dados transformados no GitHub.

## Estrutura do Projeto

- `ExtrairDados.py`: Script para extrair informações em tempo real sobre o Bitcoin.
- `TransformarDados.py`: Script para realizar análises simples das tendências de mercado.
- `CarregarDados.py`: Script para carregar os dados transformados no GitHub.

## Requisitos

- Python 3.x
- Bibliotecas Python (consulte o arquivo `requirements.txt`)

## Configuração

1. Configure uma conta no GitHub.
2. Crie um repositório no GitHub para armazenar os dados transformados.
3. Clone o repositório para sua máquina local.

## Extração de Dados

O script [ExtrairDados.py](ExtrairDados.py) utiliza a API CoinGecko para coletar informações em tempo real sobre o preço do Bitcoin.

## Transformação de Dados

O script [TransformarDados.py](TransformarDados.py) realiza uma análise simples das tendências de mercado, com base em uma comparação do preço atual com um valor anterior (a ser fornecido durante a extração).

## Carga de Dados

O GitHub é usado como o local de armazenamento para os dados transformados. Os dados são enviados para o repositório criado durante a configuração.

## Contribuições

Contribuições são bem-vindas! Se você deseja contribuir para o desenvolvimento deste projeto, por favor, siga as diretrizes de contribuição e crie um pull request.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).
