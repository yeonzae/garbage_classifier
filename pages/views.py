# views.py
from datetime import timezone
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import uuid
from PIL import Image
from io import BytesIO
# load model
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json
import numpy as np
from PIL import Image
import cv2
from .models import ClassificationResult


def load_model():
    json_file = open("DenseNet_model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("DenseNet_model.h5")
    loaded_model.compile(loss="sparse_categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])
    return loaded_model

# 전역 변수로 모델을 로드
model = load_model()

class HomePageView(TemplateView):
    template_name = "pages/home.html"

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        # 이미지 데이터 처리
        image_data = request.POST.get('image')
        format, imgstr = image_data.split(';base64,') 
        image = Image.open(BytesIO(base64.b64decode(imgstr)))

        # RGBA 이미지를 RGB로 변환
        if image.mode == 'RGBA':
            image = image.convert('RGB')

        # 이미지 크기 조정 및 배열 변환
        image = image.resize((224, 224))
        image_array = np.expand_dims(np.array(image), axis=0)

        # 모델을 사용하여 예측
        prediction = model.predict(image_array)
        predicted_class = np.argmax(prediction, axis=1)

        # 데이터베이스에 결과 저장
        result = ClassificationResult(predicted_class=str(predicted_class))
        result.save()
        total_captures_today = ClassificationResult.objects.count()
        flammable_count = ClassificationResult.objects.filter(predicted_class='[0]').count()
        non_flammable_count = ClassificationResult.objects.filter(predicted_class='[1]').count()

        # 클라이언트에 JSON 형태로 결과 반환
        return JsonResponse({
            'status': 'success',
            'class': result.predicted_class,
            'total_captures_today': total_captures_today,
            'flammable_count': flammable_count,
            'non_flammable_count': non_flammable_count
        })

    return JsonResponse({'status': 'error'})


class AboutPageView(TemplateView):
    template_name = "pages/about.html"