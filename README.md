# Anonimizador de Caras con OpenCV

Sistema inteligente de anonimización de rostros utilizando OpenCV y MediaPipe para detectar y difuminar caras en imágenes, videos y transmisiones en tiempo real.

##  Descripción

Este proyecto utiliza la detección facial de MediaPipe para identificar rostros en diferentes fuentes (imágenes, videos y cámara web) y aplicar un efecto de desenfoque gaussiano.

##  Funcionalidades

### 1. Procesamiento de Imágenes
Anonimiza caras en imágenes estáticas.
- Detecta múltiples rostros en una imagen
- Aplica desenfoque gaussiano a cada cara detectada
- Guarda la imagen procesada en la carpeta de salida

**Uso:**
```bash
python main.py --mode image --filePath "resources/images/tu_imagen.jpg"
```

### 2. Procesamiento de Videos
Procesa videos completos cuadro por cuadro.
- Lee archivos de video (MP4, AVI, etc.)
- Detecta y anonimiza caras en cada frame
- Genera un video procesado con todas las caras difuminadas
- Mantiene la resolución y duración original del video

**Uso:**
```bash
python main.py --mode video --filePath "resources/video/tu_video.mp4"
```

### 3. Cámara en Tiempo Real
Anonimización en vivo desde la webcam.
- Captura video en tiempo real desde tu cámara
- Detecta y difumina caras instantáneamente
- Muestra la transmisión procesada en una ventana

**Uso:**
```bash
python main.py --mode webcam
```

## Estructura del Proyecto

```
anonymizer_faces_with_opencv/
│
├── main.py                 # Archivo principal del programa
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Documentación
│
└── resources/
    ├── images/            # Carpeta para imágenes de entrada
    ├── video/             # Carpeta para videos de entrada
    └── output/            # Carpeta de salida (se crea automáticamente)
```

## Ejemplos de Uso

### Procesar una imagen específica
```bash
python main.py --mode image --filePath "resources/images/foto_grupal.jpg"
```
Resultado: `resources/output/output.png`

### Procesar un video
```bash
python main.py --mode video --filePath "resources/video/conferencia.mp4"
```
Resultado: `resources/output/output_video.mp4`

### Iniciar cámara en tiempo real
```bash
python main.py --mode webcam
```
Para cerrar: presiona cualquier tecla mientras la ventana está activa

## Parámetros de Configuración

El programa acepta los siguientes argumentos:

| Parámetro | Descripción | Valores | Por defecto |
|-----------|-------------|---------|-------------|
| `--mode` | Modo de operación | `image`, `video`, `webcam` | `webcam` |
| `--filePath` | Ruta del archivo a procesar | Ruta completa o relativa | `None` |


## Problemas Conocidos

### Error al cerrar video o cámara en tiempo real
**Descripción**: El programa puede cerrarse inesperadamente con un error cuando se intenta cerrar la ventana en modo video o webcam.

**Estado**: En desarrollo 

**Actualización futura**: Se implementará un sistema mejorado de manejo de eventos para:
- Capturar correctamente la tecla ESC para salir
- Manejar el cierre de ventana de forma segura
- Liberar recursos apropiadamente al finalizar
- Añadir mensajes informativos sobre cómo cerrar la aplicación

**Solución temporal**: Si el programa no responde, puedes cerrarlo desde el administrador de tareas o terminal (Ctrl+C).

## 📝 Notas Técnicas

- Las coordenadas de detección facial son relativas al tamaño de la imagen (0-1) y se convierten a píxeles
- El desenfoque utiliza un kernel de 30x30 píxeles
- Los videos se exportan en formato MP4V a 25 FPS
- La carpeta de salida se crea automáticamente si no existe


**Desarrollado con:** Python  | OpenCV  | MediaPipe 
