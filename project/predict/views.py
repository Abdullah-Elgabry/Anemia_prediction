from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults
import json
import numpy as np
from django.http import HttpResponse

def predict(request):
    return render(request, "predict/predict.html")


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client

        Gender = request.POST.get('Gender')
        Hemoglobin = request.POST.get('Hemoglobin')
        MCH = request.POST.get('MCH')
        MCHC = request.POST.get('MCHC')
        MCV= request.POST.get('MCV')

        # Unpickle model
        model = pd.read_pickle(r"/Users/macos/Desktop/test/project/new_model.pickle")
        # Make prediction
        result = model.predict([[Gender, Hemoglobin, MCH, MCHC, MCV]])

        prediction = result[0]
        
        PredResults.objects.create(Gender=Gender, Hemoglobin=Hemoglobin, MCH=MCH, MCHC=MCHC, MCV=MCV, prediction=prediction)
        
        return JsonResponse({'result': float(prediction), 'Gender': float(Gender),
                             'Hemoglobin': float(Hemoglobin), 'MCH': float(MCH), 'MCHC':float(MCHC)  ,'MCV': float(MCV) },
                            safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "predict/results.html", data)
