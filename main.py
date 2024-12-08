from openai import OpenAI


def analizar(msg):
    ENDPOINT = "http://localhost:39281/v1"
    MODEL = "llama3.2:3b-gguf-q4-km"

    client = OpenAI(base_url=ENDPOINT, api_key="not-needed")

    #Seteamos el prompt
    messages = [
                    {
                        "role": "system",   #Definimos rol en este caso como se comportara el sistema
                        "content":          #Definimos el prompt
                                            """
                                            Actua como analizador de sentimientos, 
                                            Responder de forma extricta JSON:
                                            {   
                                                "comment": {{msg}},
                                                "result" : "REGLA"
                                            }
                                            
                                            REGLA se define por:
                                            "-1" sentimiento de insatisfacción
                                            "0"  sentimiento neutro 
                                            "1"  sentimiento de satisfacción. 
                                            """
                    },
                    {
                            "role": "user",         #Definimos rol usuario por lo que el contenido sera el texto a procesar
                            "content": f"{msg}"     #Texto a procesar para extraer información relevante
                    }
            ]

    response = client.chat.completions.create(
        top_p=0.9, 
        temperature=0.6, 
        model=MODEL, 
        messages=messages
    )

    resultado = response.choices[0].message.content
    print(resultado)

    return resultado






msg = [
"Me encanta cómo funciona esta aplicación, es muy fácil de usar.",
"La comida en este restaurante es espectacular, definitivamente volveré.",
"Excelente atención al cliente, me sentí muy bien recibido.",

"La calidad del producto dejó mucho que desear, no lo volveré a comprar.",
"El servicio fue muy lento, tuve que esperar más de una hora.",
"No recomiendo este restaurante, la comida estaba fría y mal preparada.",

"La aplicación tiene algunas funciones útiles, pero le falta algo.",
"El libro tiene una buena trama, pero algunos capítulos fueron lentos.",
"La atención fue correcta, pero no hubo un trato especial."
]

import random
# random.shuffle(msg)

for m in msg:
    analizar(m)
    input()

