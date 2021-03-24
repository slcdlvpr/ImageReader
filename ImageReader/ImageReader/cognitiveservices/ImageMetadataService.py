from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


class imageMetadataService(object):
    """image metadata processing class"""
         
    def __init__(self, subscriptionKey, endpoint):
        self.subscription_key = subscriptionKey
        self.endpoint = endpoint
        computervision_client = ComputerVisionClient(self.endpoint, CognitiveServicesCredentials(self.subscription_key))
        self.client = computervision_client

    def image_description (self, imageurl):
        description_results = self.client.describe_image_in_stream(imageurl)
        return description_results

    def image_tags (self,imageUrl):
        tags_result_remote = self.client.tag_image_in_stream(imageUrl)
        return tags_result_remote

    def image_definition (self, imageUrl):
        detect_objects_results_remote = self.client.detect_objects_in_stream(imageUrl)
        return detect_objects_results_remote