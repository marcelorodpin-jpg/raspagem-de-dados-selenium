# 📱 Raspagem de Dados de Preços na Amazon com Python

Este projeto é um script de automação e web scraping desenvolvido em Python para capturar em tempo real o preço de um smartphone no site da Amazon Brasil.

## 🚀 Tecnologias Utilizadas

* **Python 3**
* **Selenium WebDriver**: Para automação do navegador e interação com elementos dinâmicos da página.
* **WebDriver Manager**: Para gerenciamento e instalação automática do driver do Google Chrome.

## 📋 Pré-requisitos

Antes de rodar o script, você precisa ter o Python instalado em sua máquina e as bibliotecas necessárias. Você pode instalar as dependências rodando o comando abaixo no terminal:

```bash
pip install selenium webdriver-manager
```

## 🛠️ Como Executar o Projeto

1. Clone este repositório para a sua máquina local:
   ```bash
   git clone https://github.com
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd NOME-DO-REPOSITORIO
   ```
3. Execute o script Python:
   ```bash
   python nome_do_seu_arquivo.py
   ```

## 🧠 Como o Código Funciona

1. **Acesso Automatizado**: O Selenium abre uma instância do Google Chrome de forma automática e navega até o link do produto configurado.
2. **Espera Inteligente**: O script aguarda alguns segundos para garantir que todos os elementos e scripts de preço da página sejam carregados.
3. **Extração de Dados**: Utilizando seletores `By.CLASS_NAME`, o robô localiza a parte inteira (`a-price-whole`) e a fracionada (`a-price-fraction`) do valor do produto.
4. **Tratamento de Texto**: Limpa quebras de linhas indesejadas e exibe o preço formatado diretamente no terminal.
5. **Encerramento Seguro**: Fecha o navegador e encerra o processo do driver ao final da execução.

## ⚠️ Observações Importantes

Grandes plataformas de e-commerce como a Amazon possuem sistemas robustos de segurança (como CAPTCHAs). Se o script rodar muitas vezes seguidas em um curto período de tempo, o robô pode ser bloqueado temporariamente ou desafiado por uma tela de verificação.

---
✒️ Desenvolvido por [Marcelo](https://github.com)
