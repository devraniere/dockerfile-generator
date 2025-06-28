import os
from jinja2 import Environment, FileSystemLoader

# Define o nome do diretório de saída para os arquivos gerados
OUTPUT_DIR = "output"

# Função para criar os Dockerfiles a partir de templates do diretório, com base nas entradas do usuário na função interactive_cli
def generate_dockerfile(language, framework, version, port, output_file_name):
    print("\nIniciando a geração de arquivos...")

    # Cria o diretório de saída se ele não existir
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Diretório '{OUTPUT_DIR}' criado com sucesso para armazenar os Dockerfiles gerados.")

    # Armazenando os templates em uma variável
    template_env = Environment(loader=FileSystemLoader('templates'))

    # Declarando a variável que armazenará o template do Dockerfile a ser criado
    dockerfile_template_name = ""

    # Condicionais que vão definir o template do Dockerfile por meio das entradas de linguagem e frameworks escolhidos pelo usuário
    if language == "python":
        if framework == "flask":
            dockerfile_template_name = "python_flask.j2"
        elif framework == "fastapi":
            dockerfile_template_name = "python_fastapi.j2"
        elif framework == "django":
            dockerfile_template_name = "python_django.j2"

    elif language == "java":
        if framework == "springboot":
            dockerfile_template_name = "java_springboot.j2"
        else:
            print(f"\nERRO: Framework '{framework}' não suportado para Java. Apenas 'springboot' é suportado.")
            return

    # Caso o usuário insira valores inválidos, uma mensagem irá aparecer para notificá-lo
    if not dockerfile_template_name:
        print(f"\nERRO: Combinação de linguagem '{language}' e framework '{framework}' não suportada.")
        return

    print(f"\nBuscando template do Dockerfile: {dockerfile_template_name}")
    
    # Constrói o caminho completo para o arquivo Dockerfile de saída dentro do diretório OUTPUT_DIR
    output_dockerfile_path = os.path.join(OUTPUT_DIR, output_file_name)

    # Try except para tentar criar o arquivo com base nas entradas do usuário
    try:
        dockerfile_template = template_env.get_template(dockerfile_template_name)
        dockerfile_content = dockerfile_template.render(
            version=version,
            port=port
        )

        with open(output_dockerfile_path, 'w') as f:
            f.write(dockerfile_content)

        print(f"\nArquivo '{output_dockerfile_path}' gerado com sucesso.")

    except Exception as e:
        print(f"\nERRO: Não foi possível gerar o Dockerfile. Verifique se o template '{dockerfile_template_name}' existe.")
        print(f"\nDetalhes do erro: {e}")
        return

    # --- Lógica para gerar o .dockerignore ---
    # Constrói o caminho completo para o arquivo .dockerignore de saída dentro do diretório OUTPUT_DIR
    output_dockerignore_path = os.path.join(OUTPUT_DIR, ".dockerignore")
    dockerignore_template_name = ".dockerignore.j2"
    dockerignore_template_path = os.path.join('templates', dockerignore_template_name)

    print(f"\nTentando gerar o arquivo '.dockerignore' a partir do template: {dockerignore_template_path}.")

    if not os.path.exists(dockerignore_template_path):
        print(f"\nAVISO: O template {dockerignore_template_path} NÃO foi encontrado. O arquivo .dockerignore não será gerado.")
    else:
        try:
            dockerignore_template_obj = template_env.get_template(dockerignore_template_name)
            dockerignore_content = dockerignore_template_obj.render()

            with open(output_dockerignore_path, 'w') as f:
                f.write(dockerignore_content)

            print(f"Arquivo '{output_dockerignore_path}' gerado com sucesso!")

        except Exception as e:
            print(f"\nAVISO: Ocorreu um erro ao renderizar ou escrever o arquivo '.dockerignore'.")
            print(f"\nDetalhes do erro: {e}")


# Função para a interatividade do usuário via terminal
def interactive_cli():
    print("----- GERADOR DE DOCKERFILES -----")

    # Aqui o usuário irá inserir a linguagem de programação que deseja para o seu Dockerfile puxar a imagem base
    while True:
        lang = input("\nQual a linguagem do projeto? (python / java): ").lower()

        if lang in ["python", "java"]:
            break

        else:
            print("\nLinguagem não suportada. Por favor, escolha entre 'python' ou 'java'.")

    framework = ""

    # Aqui o usuário irá inserir o framework dependendo da linguagem escolhida
    while True:
        if lang == "python":
            framework = input("\nQual é o framework que você deseja para o seu projeto? (flask / fastapi / django): ").lower()

            if framework in ["flask", "fastapi", "django"]:
                break

            else:
                print("\nFramework não suportado para Python. Por favor, escolha entre 'flask', 'fastapi' ou 'django'.")

        elif lang == "java":
            print("\nO framework suportado para Java é o SpringBoot.")
            framework = "springboot"
            break

    version = ""

    if lang == "python":
        print("\nA versão utilizada para o Python será a 3.11")
        version = "3.11"

    elif lang == "java":
        print("\nA versão utilizada para o Java será a 21")
        version = "21"

    while True:
        try:
            port = int(input("\nQual a porta que você quer expor? (ex: 5000): "))
            break

        except ValueError:
            print("\nEntrada inválida, insira um número inteiro.")

    # Input para o usuário inserir o nome que deseja para o seu dockerfile
    output_file_name = input("\nQual será o nome do seu Dockerfile? \nPadrão: Dockerfile\nPressione ENTER para o nome padrão ou digite o nome desejado: ")

    if not output_file_name:
        output_file_name = "Dockerfile"
    # Caso o usuário não insira a extensão .dockerfile no nome do arquivo, o programa fará isso
    elif not output_file_name.lower().endswith(('.dockerfile', '.dockerfile')):
        output_file_name += ".dockerfile"

    generate_dockerfile(lang, framework, version, port, output_file_name)

    print("\nProcesso de geração concluído!")

if __name__ == '__main__':
    interactive_cli()