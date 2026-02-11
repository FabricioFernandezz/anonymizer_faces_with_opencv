import cv2 as cv
import mediapipe as mp
import os

img_path = ".\\resources\\images\\test_image.jpg"

img = cv.imread(img_path)

output_dir = "./resources/output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# cv.imshow(" test_image", img)

H, W , _ = img.shape #ignoramos los canales

mp_face_detection = mp.solutions.face_detection


with mp_face_detection.FaceDetection(0,0.5) as face_detection:
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    print(out.detections)


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


cv.imwrite(os.path.join(output_dir,"output.png"), img)