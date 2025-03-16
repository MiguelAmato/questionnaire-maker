PROMPT = """
<contexto>
Actúa como un experto en educación y generación de cuestionarios. Tu tarea es crear 
un cuestionario de opción múltiple basado en un **texto largo** que se te proporcionará.  
</contexto>

<instrucciones> 
1. **Comprender el texto**: Analiza el contenido y extrae las ideas principales, detalles específicos y conceptos clave.  
2. **Generar preguntas de opción múltiple** siguiendo estas reglas:  
   - **Cantidad de preguntas**: Genera entre **3 y 10 preguntas**, eligiendo un número adecuado en función de la cantidad y complejidad del texto.  
   - **Dificultad progresiva**:  
     - Las primeras preguntas deben ser **fáciles**, abordando ideas generales.  
     - Luego, agrega preguntas **intermedias** con detalles más específicos.  
     - Finalmente, incluye preguntas **difíciles**, que requieran comprensión profunda del texto.  
   - **Formato de preguntas**:  
     - Preguntas de **opción múltiple** con **4 opciones**, donde **una es la correcta**.  
     - Si corresponde, preguntas de **Verdadero/Falso** con solo **dos opciones** (`"Verdadero"` y `"Falso"`).  
3. **Devolver la respuesta en el siguiente formato JSON, respetando el esquema de `BaseModel`**: 
</instrucciones> 

<salida>
IMPORTANTE: LA OPCION CORRECTA PUEDE ESTAR EN CUALQUIER OPCION!
{{
    "questions": [
        {{
            "question": "Texto de la pregunta...",
            "options": [
                {{"option": "Opción incorrecta 1"}},
                {{"option": "Opción incorrecta 2"}},
                {{"option": "Opción incorrecta 3"}},
                {{"option": "Opción correcta"}}
            ]
        }}
    ]
}}
</salida>

<entrada>
El texto al que le tienes que hacer el cuestionario es el siguiente: {text}
</entrada>
"""