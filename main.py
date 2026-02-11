import cv2 as cv
import mediapipe as mp
import os
import argparse

def process_img(img, face_detection):
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None:
    # recorremos solamente detection, ya que este tiene una variable que nos importa, esta es location_data, la cual es un diccionario con las coordenadas de la cara detectada
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box  # estoy accendiendo a este lugar en especifico
            x1,y1 , w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
            
            x1 = int(x1 * W) #se hace para convertir las cordenadas quee stan de manera porcentual a pixeles, ya que el modelo de mediapipe devuelve las coordenadas de manera relativa al tamaño de la imagen
            y1 = int(y1 * H) 
            w = int(w * W)
            h = int(h * H)

            # cv.rectangle(img,(x1,y1),(x1+w,y1+h),(0,255,0),10)
            #para comprobar que las coordenadas son correctas.

            img[y1:y1+h,x1:x1+h] = cv.blur(img[y1:y1+h,x1:x1+h],(30,30))
            # anteriormente yo lo hice sin poner img[y1:y1+h,x1:x1+h] =..., pero lo que pasa es que solo muestra las seccion donde estaria  (anets yo puse img=...) la imagen, lo que nosostros queremos es toda a imagen y solo una seccion borrosa pero ver toda la imagen, no solo ver lo borroso
    elif out.detections is None:
        print("no se detecto ninguna cara")

    return img

arg = argparse.ArgumentParser() #creamos un objeto de la clase ArgumentParser, esta clase nos permite crear argumentos para nuestro programa, es decir, podemos pasarle argumentos desde la linea de comandos para que nuestro programa haga cosas diferentes dependiendo de los argumentos que le pasemos

arg.add_argument("--mode", default="image") # agregamos un argumento llamado mode, este argumento nos va a permitir elegir entre procesar una imagen o un video, por defecto se va a procesar una imagen, pero si queremos procesar un video, podemos pasarle el argumento --mode video
arg.add_argument("--filePath", default=".\\resources\\images\\test_image.jpg") # agregamos un argumento llamado filePath, este argumento nos va a permitir elegir la ruta del archivo que queremos procesar, por defecto se va a procesar una imagen que se encuentra en la carpeta resources/images/test_image.jpg, pero si queremos procesar otro archivo, podemos pasarle el argumento --filePath seguido de la ruta del archivo que queremos procesar

output_dir = "./resources/output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(0,0.5) as face_detection:
    if arg.parse_args().mode == "image": # si el argumento mode es igual a image, entonces se va a procesar una imagen
    
        img = cv.imread(arg.parse_args().filePath)
        H,W,_ = img.shape

        img= process_img(img,face_detection)

        cv.imwrite(os.path.join(output_dir,"output.png"), img)