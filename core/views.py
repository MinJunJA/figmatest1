import os
import numpy as np
from gtts import gTTS
from playsound import playsound
from .models import Snack,Nutrition # models.py 안의 Snack 클래스 호출

import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img , img_to_array
from django.conf import settings
from django.template.response import TemplateResponse
from django.utils.datastructures import MultiValueDictKeyError
# from keras.models import model_from_json
# https://im-nanna.tistory.com/27 //MultiValueDictKeyError에 대한 설명
# https://windybay.net/post/39/

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.db import connection



class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name


def index(request):
    message = ""
    prediction = ""
    fss = CustomFileSystemStorage()
    
    try:
        image = request.FILES["image"]
        print("Name", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" + image.name
        # image details
        image_url = fss.url(_image)
        
        # Read the image

        imag = load_img(path,target_size = (75,75))
        imag = img_to_array(imag)
        img = imag.reshape(1,75,75,3)
        img = img.astype('float32')
        test_image = img/255.0

        # load model(CNN)
        model = tf.keras.models.load_model(os.getcwd() + '/3rd_cnn_1.h5')
        result = model.predict(test_image)

        # ----------------
        # LABELS
        # Banana 0
        # Chip 1
        # Heim 2
        # Onion 3
        # Oreo 4
        # Pepero 5
        # Pie 6
        # Pizza 7
        # Shrimp 8
        # Turtle 9
        # ----------------
        print("Prediction: " + str(np.argmax(result)))

        prediction = np.argmax(result)
        snack_object = Snack.objects.get(id=prediction+1)
        nutrition_object = Nutrition.objects.get(id=prediction+1)

        name = snack_object.name
        info = snack_object.info
        price = snack_object.price

        total_content = str(nutrition_object.total_content)
        calories = str(nutrition_object.calories)
      
        # snack_name="snack_name.mp3"
        # name_tts = gTTS(text="이 상품은 "+ name+"입니다. 가격은 " +str(price)+"원입니다.", lang="ko")
        # name_tts.save("./assets/"+snack_name)

        # snack_info="snack_info.mp3"
        # info_tts = gTTS(text=info+"상품의 총량은 "+total_content+"그램이며, 칼로리는 "+calories+"칼로리입니다." ,lang="ko") # info에 해당하는 str값을 가져와서 음성으로 변환
        # info_tts.save("./assets/"+snack_info)

        return TemplateResponse(
            request,
            "pred.html",
            {
                "message": message,
                "image": image,
                "image_url": image_url,
                "prediction": prediction,
                "name": name,
                "info": info,
                "price": price,
                "total_content": total_content,
                "calories": calories
            },
        )
    except MultiValueDictKeyError:

        return TemplateResponse(
            request,
            "index.html",
            {
                "message": "업로드한 이미지가 없습니다."
            },
        )


def pred(request):
    message = ""
    prediction = ""
    fss = CustomFileSystemStorage()
    
    try:
        image = request.FILES["image"]
        print("Name", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" + image.name
        # image details
        image_url = fss.url(_image)
        
        # Read the image

        imag = load_img(path,target_size = (75,75))
        imag = img_to_array(imag)
        img = imag.reshape(1,75,75,3)
        img = img.astype('float32')
        test_image = img/255.0

        # load model(CNN)
        model = tf.keras.models.load_model(os.getcwd() + '/3rd_cnn_1.h5')
        result = model.predict(test_image)

        # ----------------
        # LABELS
        # Banana 0
        # Chip 1
        # Heim 2
        # Onion 3
        # Oreo 4
        # Pepero 5
        # Pie 6
        # Pizza 7
        # Shrimp 8
        # Turtle 9
        # ----------------
        print("Prediction: " + str(np.argmax(result)))

        prediction = np.argmax(result)
        snack_object = Snack.objects.get(id=prediction+1)
        nutrition_object = Nutrition.objects.get(id=prediction+1)

        name = snack_object.name
        info = snack_object.info
        price = snack_object.price

        total_content = str(nutrition_object.total_content)
        calories = str(nutrition_object.calories)
      
        # snack_name="snack_name.mp3"
        # name_tts = gTTS(text="이 상품은 "+ name+"입니다. 가격은 " +str(price)+"원입니다.", lang="ko")
        # name_tts.save("./assets/"+snack_name)

        # snack_info="snack_info.mp3"
        # info_tts = gTTS(text=info+"상품의 총량은 "+total_content+"그램이며, 칼로리는 "+calories+"칼로리입니다." ,lang="ko") # info에 해당하는 str값을 가져와서 음성으로 변환
        # info_tts.save("./assets/"+snack_info)

        return TemplateResponse(
            request,
            "pred.html",
            {
                "message": message,
                "image": image,
                "image_url": image_url,
                "prediction": prediction,
                "name": name,
                "info": info,
                "price": price,
                "total_content": total_content,
                "calories": calories
            },
        )
    except MultiValueDictKeyError:

        return TemplateResponse(
            request,
            "index.html",
            {
                "message": "업로드한 이미지가 없습니다."
            },
        )

def banana(request):
    return TemplateResponse(request,
    "banana.html",
    )

def pepero(request):
    return TemplateResponse(request,
    "pepero.html",
    )

def chip(request):
    return TemplateResponse(request,
    "chip.html",
    )

def heim(request):
    return TemplateResponse(request,
    "heim.html",
    )

def onion(request):
    return TemplateResponse(request,
    "onion.html",
    )

def oreo(request):
    return TemplateResponse(request,
    "oreo.html",
    )

def pie(request):
    return TemplateResponse(request,
    "pie.html",
    )

def pizza(request):
    return TemplateResponse(request,
    "pizza.html",
    )

def shrimp(request):
    return TemplateResponse(request,
    "shrimp.html",
    )

def turtle(request):
    return TemplateResponse(request,
    "turtle.html",
    )