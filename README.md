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


#Desde Python

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
