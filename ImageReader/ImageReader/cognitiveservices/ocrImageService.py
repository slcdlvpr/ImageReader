from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

class ocrImageService(object):

    def __init__(self, subscriptionKey, endpoint):
        self.subscription_key = subscriptionKey
        self.endpoint = endpoint
        computervision_client = ComputerVisionClient(self.endpoint, CognitiveServicesCredentials(self.subscription_key))
        self.client = computervision_client
    
    def image_to_text(self, imagestream):
     
        result = []
        computervision_client = ComputerVisionClient(self.endpoint, CognitiveServicesCredentials(self.subscription_key))
        # Get an image with text
        recognize_handw_results = computervision_client.read_in_stream(imagestream,  raw=True)
        # Get the operation location (URL with an ID at the end) from the response
        operation_location_remote = recognize_handw_results.headers["Operation-Location"]
        # Grab the ID from the URL
        operation_id = operation_location_remote.split("/")[-1]
        while True:
            get_handw_text_results = computervision_client.get_read_result(operation_id)
            if get_handw_text_results.status not in ['notStarted', 'running']:
                break
            time.sleep(1)
        if get_handw_text_results.status == OperationStatusCodes.succeeded:
            for text_result in get_handw_text_results.analyze_result.read_results:
                for line in text_result.lines:
                    result.append(line.text)
        
        return result

    def ocr_text(image_file):
        image_to_text(image_file, image_file.replace(".jpg", ".txt"))
