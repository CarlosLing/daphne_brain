import logging

# Get an instance of a logger
logger = logging.getLogger('data-mining')


from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import numpy as np
import sys,os
import json
import csv


# Print all paths included in sys.path
# from pprint import pprint as p
# p(sys.path)

from data_mining_API.api import DataMiningClient



# Create your views here.
class GetDrivingFeatures(APIView):

    def __init__(self):
        self.DataMiningClient = DataMiningClient()
        pass

    def post(self, request, format=None):
        
        try:
            # Start data mining client
            self.DataMiningClient.startConnection()
            
            # Get threshold values for the metrics
            supp = float(request.POST['supp'])
            conf = float(request.POST['conf'])
            lift = float(request.POST['lift'])
            
            # Get selected arch id's
            selected = request.POST['selected']
            selected = selected[1:-1]
            selected_arch_ids = selected.split(',')
            # Convert strings to ints
            behavioral = []
            for s in selected_arch_ids:
                behavioral.append(int(s))

            # Get non-selected arch id's
            non_selected = request.POST['non_selected']
            non_selected = non_selected[1:-1]
            non_selected_arch_ids = non_selected.split(',')
            # Convert strings to ints
            non_behavioral = []
            for s in non_selected_arch_ids:
                non_behavioral.append(int(s))

            # Load architecture data from the session info
            logger.debug(request.session)
            architectures = request.session['data']

            problem = request.POST['problem']
            inputType = request.POST['input_type']

            drivingFeatures = self.DataMiningClient.getDrivingFeatures(problem, inputType, behavioral, non_behavioral,
                                                                       architectures, supp, conf, lift)
                
            output = drivingFeatures

            # End the connection before return statement
            self.DataMiningClient.endConnection() 
            return Response(output)
        
        except Exception as detail:
            logger.exception('Exception in getDrivingFeatures: ' + str(detail))
            self.DataMiningClient.endConnection()
            return Response('')
        
        
        
class GetMarginalDrivingFeaturesConjunctive(APIView):
    
    def __init__(self):
        self.DataMiningClient = DataMiningClient()
        pass

    def post(self, request, format=None):
        
        try:
            # Start data mining client
            self.DataMiningClient.startConnection()
            
            # Get threshold values for the metrics
            supp = float(request.POST['supp'])
            conf = float(request.POST['conf'])
            lift = float(request.POST['lift'])
            
            # Get selected arch id's
            behavioral = json.loads(request.POST['selected'])
            non_behavioral = json.loads(request.POST['non_selected'])
                
            featureName = request.POST['featureName']            
            highlighted = json.loads(request.POST['highlighted'])

            # Load architecture data from the session info
            architectures = request.session['data']

            drivingFeatures = self.DataMiningClient.getMarginalDrivingFeaturesConjunctive(behavioral,non_behavioral,architectures,featureName,highlighted,supp,conf,lift)            
            output = drivingFeatures

            # End the connection before return statement
            self.DataMiningClient.endConnection() 
            return Response(output)
        
        except Exception as detail:
            logger.exception('Exception in getDrivingFeatures: ' + detail)
            self.DataMiningClient.endConnection()
            return Response('')
        
        
class GetMarginalDrivingFeatures(APIView):

    def __init__(self):
        self.DataMiningClient = DataMiningClient()
        pass

    def post(self, request, format=None):
        
        try:
            # Start data mining client
            self.DataMiningClient.startConnection()
            
            # Get threshold values for the metrics
            supp = float(request.POST['supp'])
            conf = float(request.POST['conf'])
            lift = float(request.POST['lift'])
            
            # Get selected arch id's
            behavioral = json.loads(request.POST['selected'])
            non_behavioral = json.loads(request.POST['non_selected'])
                
            featureExpression = request.POST['featureExpression']            

            # Load architecture data from the session info
            architectures = request.session['data']

            drivingFeatures = self.DataMiningClient.getMarginalDrivingFeatures(behavioral,non_behavioral,architectures,
                                                                               featureExpression,supp,conf,lift)            
            output = drivingFeatures

            # End the connection before return statement
            self.DataMiningClient.endConnection() 
            return Response(output)
        
        except Exception as detail:
            logger.exception('Exception in getDrivingFeatures: ' + detail)
            self.DataMiningClient.endConnection()
            return Response('')
        
        
        
        
        
def booleanArray2booleanString(booleanArray):
    leng = len(booleanArray)
    boolString = ''
    for i in range(leng):
        if booleanArray[i] == True:
            boolString += '1'
        else:
            boolString += '0'
    return boolString

