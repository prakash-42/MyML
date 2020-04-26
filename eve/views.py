from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.core.serializers.python import Serializer
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework import status
import json
import simplejson

import tensorflow as tf
import numpy as np
from tensorflow.keras.models import model_from_json

from .serializers import FileSerializer
from .models import File
from .imageprep import *
from .file_handler import *

def index(request):
    context = {'key': 'value'}
    return render(request, 'eve/index.html', context)


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            # On how to get python object from file_serializer object
            # https://www.django-rest-framework.org/tutorial/1-serialization/
            file_serializer.save()
            file_id = file_serializer['id'].value
            file_obj = File.objects.get(id=file_id)

            file = file_obj.file
            cloudinary_url, upload_status = upload_to_cloudinary(file)
            prediction = make_prediction(file)
            file_obj.cloudUrl = cloudinary_url
            file_obj.prediction = prediction
            file_obj.save()
            dict_obj = model_to_dict(file_obj)
            print(dict_obj)
            print('ID: ', file_id,  '\nfile: ', file, '\nremark: ',  file_obj.remark)

            # Approach 1:
            # return HttpResponse(serializers.serialize('json', [file_obj])[1:-1], status=status.HTTP_201_CREATED)

            # Approach 2:
            # return HttpResponse(serializers.serialize('json', list(File.objects.filter(id=file_id))),
            #                     status=status.HTTP_201_CREATED)

            # Approach 3:
            # serializer = MySerializer()
            # return HttpResponse(serializer.serialize([file_obj]), status=status.HTTP_201_CREATED)

            # Approach 4: Maybe not the best one, but it works!
            response_id = '"id": "' + str(file_obj.id) + '"'
            response_cloud_url = '"cloudUrl": "' + file_obj.cloudUrl + '"'
            response_prediction = '"prediction": "' + str(file_obj.prediction) + '"'
            response = '{ ' + response_id + ', ' + response_cloud_url + ', ' + response_prediction + '}'
            return HttpResponse(response, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# https://stackoverflow.com/a/5768757
class MySerializer(Serializer):
    def end_object(self, obj):
        self.objects.append(self._current)


def get_prediction_from_probabilities(predictions):
    print(predictions.shape)
    simple_list = predictions.tolist()
    return simple_list.index(max(simple_list))


def make_prediction(file):
    print(file)
    image_data = imageprepare(file)
    input_data_2d = get_2d_from_list(image_data, 28, 28)

    for i in range(28):
        for j in range(28):
            print(image_data[i * 28 + j], end='\t')
        print('')

    numpy_array_3d = np.array([input_data_2d], dtype=np.uint8)

    # Serialising the model now
    path = 'eve/'

    json_file = open(path + 'model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(path + "model.h5")
    print("Loaded model from disk")

    loaded_model.compile(optimizer=tf.optimizers.Adam(),
                         loss='sparse_categorical_crossentropy',
                         metrics=['accuracy'])

    prediction = loaded_model.predict(numpy_array_3d)
    print('prediction: ', prediction)

    return get_prediction_from_probabilities(prediction[0])
