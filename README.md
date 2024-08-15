# base_lat_long_mapa
 Geração de base completa de endereços


# 🗺️ Processamento e Enriquecimento de Dados Geográficos com Python

Bem-vindo ao repositório **Processamento e Enriquecimento de Dados Geográficos**! Este projeto em Python foi desenvolvido para realizar a manipulação, limpeza e junção de dados de endereços e coordenadas geográficas em grandes bases de dados. Utilizando bibliotecas poderosas como `pandas` e `pyarrow`, o script processa CSVs e gera saídas otimizadas em formatos CSV e Parquet.

## 📋 Funcionalidades

- **Remoção de Acentos e Espaços**: Normaliza os dados para facilitar a manipulação e comparação.
- **Junção de DataFrames**: Realiza a combinação de múltiplos DataFrames, cruzando dados de endereços com coordenadas geográficas.
- **Filtragem e Organização**: Separa os dados entre aqueles com e sem coordenadas geográficas, permitindo tratamento específico.
- **Exportação para CSV e Parquet**: Gera arquivos de saída nos formatos CSV e Parquet, prontos para análise ou carregamento em um Data Warehouse.

## 🛠️ Requisitos

Antes de começar, certifique-se de ter os seguintes requisitos:

- **Python 3.x**
- **Bibliotecas Python**: `pandas`, `unicodedata`, `pyarrow`

## 🚀 Como Usar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/ericfp87/base_lat_long_mapa.git
    ```

2. **Instale as dependências**:
    ```bash
    pip install pandas pyarrow
    ```

3. **Prepare seus arquivos CSV**:
   - Coloque seus arquivos CSV nas pastas corretas e ajuste os caminhos dos arquivos no script conforme necessário.

4. **Execute o script**:
    ```bash
    python processamento_dados_geograficos.py
    ```

5. **Verifique os arquivos de saída**:
   - Após a execução, verifique os arquivos gerados na pasta `OUTPUT`. Eles incluirão os resultados processados e filtrados, prontos para uso.

## 📦 Estrutura do Projeto

```plaintext
├── processamento_dados_geograficos.py   # Script principal
├── data/                                # Pasta para armazenar os arquivos CSV de entrada
│   ├── cep_matr_loc_logr.csv            # Arquivo de matrículas
│   ├── LOGRADOUROS_MG_UPPER.csv         # Arquivo de logradouros
│   └── MUNICIPIOS_LAT_LONG_UPPER.csv    # Arquivo de municípios
└── OUTPUT/                              # Pasta para armazenar os arquivos de saída
    ├── base_cep_matr.csv                # Resultado final de matrículas e CEPs
    ├── CEP_Inexistente.csv              # Endereços sem coordenadas
    ├── BASE_MATR_LOG_TOTAL.csv          # Base completa de matrículas e logradouros
    └── BASE_CEP_LAT_LONG.csv            # Base final de CEPs e coordenadas geográficas
```

## 🌟 Dicas e Sugestões

- **Grandes Bases de Dados**: Se você estiver trabalhando com grandes volumes de dados, o formato Parquet pode ser uma escolha melhor para armazenamento e análise devido à sua eficiência de compressão e leitura.
- **Customização**: O script pode ser adaptado para processar diferentes tipos de dados de endereços, basta ajustar as colunas e chaves de junção conforme necessário.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um *pull request* ou relatar problemas na aba de *Issues*.

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.