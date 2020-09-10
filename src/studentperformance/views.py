import os
import pickle

import numpy as np
import pandas as pd

from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Performance

CLASSIFIER_BASE = os.path.join(settings.BASE_DIR, 'studentperformance', 'classifiers')

class PerformanceTestView(LoginRequiredMixin, CreateView):
    model = Performance
    fields = (            
                'age',
                'study_time',
                'activities',
                'higher_edu',
                'freetime_level',
                'outing_level',
                'weekend_alcohol_level',
                'health_status',
                'absent_weeks',
                'gp1',
                'gp2',
            )
    
    def form_valid(self, form):
        fv = form.instance
        fv.student = self.request.user
        pickle_in = open(os.path.join(CLASSIFIER_BASE, 'student_performance.pkl'), 'rb')
        clf_class = pickle.load(pickle_in)
        answers = pd.DataFrame([
            [
                fv.age, 
                fv.study_time, 
                fv.activities, 
                fv.higher_edu, 
                fv.freetime_level, 
                fv.outing_level, 
                fv.weekend_alcohol_level, 
                fv.health_status, 
                fv.absent_weeks, 
                fv.gp1, 
                fv.gp2
            ]
        ])
        result = clf_class.predict(answers)
        print('CLASS: ', result)

        if(result == [1]):
            fv.predicted_class = 'PASS'
        elif(result == [2]):
            fv.predicted_class = 'LOWER'
        elif(result == [3]):
            fv.predicted_class = 'UPPER'
        elif(result == [4]):
            fv.predicted_class = 'DISTINCTION'


        return super().form_valid(form)
    

class PerformanceDetailView(DetailView):
    model = Performance
