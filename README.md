# LLM-Analisis-Sentimientos-Local
Análisis de sentimientos de manera local utilizando Cortex y Llama3.2.

https://cortex.so/


# Correr LLM Local


### 1.- Instalar Cortex

Descarga y descomprime
```
wget https://github.com/janhq/cortex.cpp/releases/download/v1.0.2/cortex-1.0.2-linux-amd64.tar.gz

tar -xvf cortex-1.0.2-linux-amd64.tar.gz
````


### 2.- Modelo LLM llama3.2
Descarga llama3.2

```
./cortex pull llama3.2:3b-gguf-q4-km
````


### 3.- Engine
Descarga engine

```
./cortex engines install llama-cpp 
````

### 4.- Iniciar llama3.2

```
./cortex models start llama3.2:3b-gguf-q4-km

````

### 5.- Run Chat Terminal
Correr chat desde consola
```
./cortex run llama3.2:3b-gguf-q4-km
```

Lista de modelos
```
./cortex models list
```


# Desde Python

## Crear Enviroment

Crear entorno y activar
```
python3 -m venv env
source ./env/bin/activate
```

Instalar dependencia 
```
pip install openai===1.55.3
```


# Mas info

Abrir Servidor local
```
http://127.0.0.1:39281/
```



# Resultado 

Le entregamos algunos comentarios al modelo.

```
"Me encanta cómo funciona esta aplicación, es muy fácil de usar.",
"La comida en este restaurante es espectacular, definitivamente volveré.",
"La calidad del producto dejó mucho que desear, no lo volveré a comprar.",
"El servicio fue muy lento, tuve que esperar más de una hora.",
"El libro tiene una buena trama, pero algunos capítulos fueron lentos.",
"La atención fue correcta, pero no hubo un trato especial."
```

El modelo procesara y entregara el resultaro en un formato predefinido.

- "-1" sentimiento de insatisfacción
- "0"  sentimiento neutro 
- "1"  sentimiento de satisfacción. 

Resultado ejemplo
```json
[
    {
        "comment": "Me encanta cómo funciona esta aplicación, es muy fácil de usar.",
        "result": "1"
    },
    {
        "comment": "La comida en este restaurante es espectacular, definitivamente volveré.",
        "result": "1"
    },
    {
        "comment": "La calidad del producto dejó mucho que desear, no lo volveré a comprar.",
        "result" : "-1"
    },
    {   
        "comment": "El servicio fue muy lento, tuve que esperar más de una hora.",
        "result": "-1" 
    },
    {
        "comment": "El libro tiene una buena trama, pero algunos capítulos fueron lentos.",
        "result": "0"
    },
    {
        "comment": "La atención fue correcta, pero no hubo un trato especial.",
        "result": "0"
    }
]
```