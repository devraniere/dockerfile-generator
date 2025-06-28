# Dockerfile Generator

Uma ferramenta de linha de comando interativa para gerar Dockerfiles otimizados para projetos web.

## Visão Geral

Este gerador automatiza a criação de um `Dockerfile` e de um arquivo `.dockerignore`. Ao executar o script, o usuário responde a algumas perguntas sobre a linguagem, framework e porta do projeto. A ferramenta então gera um `Dockerfile` com multi-stage build, resultando em imagens Docker finais menores e mais seguras.

## Tecnologias Suportadas

- **Python**
  - Flask, FastAPI, Django
- **Java**
  - Spring Boot

## Pré-requisitos

Para usar esta ferramenta, é necessário ter o **Docker** instalado na sua máquina.

- [Instalar Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Instalar Docker Engine](https://docs.docker.com/engine/install/)

## Como Usar

O processo é automatizado por um script de shell.

1.  **Clone o Repositório:**

    ```bash
    git clone [https://github.com/devraniere/dockerfile-generator.git](https://github.com/devraniere/dockerfile-generator.git)
    cd dockerfile-generator
    ```

2.  **Execute o Gerador:**

    Execute o script `run.sh` na raiz do projeto. O script irá construir a imagem Docker da ferramenta e iniciar o gerador.

    ```bash
    ./run.sh
    ```

3.  **Siga as Instruções:**

    Responda às perguntas no terminal sobre a configuração do seu projeto. Os arquivos `Dockerfile` e `.dockerignore` serão gerados no diretório `output/`.
