#!/bin/bash

IMAGE_NAME="dockerfile-generator:v1"

if [[ -z "$(docker images -q $IMAGE_NAME)" ]]; then
    echo "Imagem '$IMAGE_NAME' não encontrada. Construindo a imagem..."
    docker build -t $IMAGE_NAME

else
    echo "Imagem '$IMAGE_NAME' encontrada. Pulando a construção."
fi

echo "Iniciando a geração de Dockerfiles..."
docker run --rm -it -v "$(pwd)":/app:Z $IMAGE_NAME "$@"

echo "Execução concluída."