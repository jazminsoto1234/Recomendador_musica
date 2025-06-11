# 🎧 Extracción de Características de Audio con MFCC

Este proyecto en Python utiliza la biblioteca `librosa` para procesar archivos de audio y extraer características relevantes mediante los coeficientes cepstrales en las frecuencias de Mel (MFCC). Esta representación es ampliamente utilizada en tareas de clasificación de audio, recomendación musical, análisis acústico, entre otras aplicaciones en el campo del audio digital.

---

## 🎯 Objetivo

Obtener una representación numérica y compacta de archivos de audio, basada en MFCC, que pueda ser usada como entrada en modelos de Machine Learning o análisis exploratorio de datos musicales.

---

## 🧠 Función Principal

### `extract_mfcc(file_path, n_mfcc=13)`

Extrae los coeficientes MFCC de los primeros 30 segundos de un archivo de audio.

- `file_path`: ruta al archivo de audio.
- `n_mfcc`: número de coeficientes por frame (por defecto 13).

Este valor ofrece un equilibrio entre compacidad y nivel de detalle. Puedes ajustarlo según el objetivo del análisis:
- `1–10`: muy compacto, pierde detalles finos.
- `13`: recomendado por su balance.
- `20+`: más detallado pero más ruidoso y costoso computacionalmente.

---

## 📂 Estructura del Proyecto

ANACONDA/
├── audio/ # Archivos de audio (.mpeg, .wav, etc.)
├── proyect_audio.ipynb # Notebook principal con lógica de extracción
├── requirements.txt # Lista de dependencias necesarias
└── .gitignore # Archivos ignorados por Git]



---

## ⚙️ Instalación de Dependencias

Ejecuta el siguiente comando en tu entorno virtual o local:

```bash
pip install -r requirements.txt



🧾 Paquetes necesarios:
librosa

numpy

jupyter (para ejecutar el notebook)

🚀 Uso Básico
Coloca tus archivos de audio dentro de la carpeta audio/.

Abre proyect_audio.ipynb con Jupyter Notebook o VSCode.

Ejecuta las celdas para cargar el audio, procesar y visualizar los coeficientes MFCC.

💡 Recomendaciones
Asegúrate de trabajar con archivos de audio de buena calidad para evitar errores de lectura.

Si planeas usar los MFCC en modelos de aprendizaje automático, puedes normalizar los resultados o aplicar técnicas de reducción de dimensionalidad.

📌 Créditos
Este proyecto fue desarrollado como parte de una práctica de análisis de audio para sistemas de recomendación musical, aprendizaje automático y procesamiento de señales.
