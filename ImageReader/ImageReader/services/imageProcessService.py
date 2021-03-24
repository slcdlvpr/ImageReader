from ImageReader.cognitiveservices.ocrImageService import ocrImageService
from ImageReader.cognitiveservices.ImageMetadataService import imageMetadataService
from ImageReader.model.coordinates import coordinates

class imageProcessService(object):

    def __init__(self,subscriptionKey, endpoint):
        self.subscription_key = subscriptionKey
        self.endpoint = endpoint


    def process_image(self, uploaded_file):
        uploaded_file.stream.seek(0) # Go back to the start of the file
        processortext = ocrImageService(self.subscription_key,self.endpoint)
        processorImage = imageMetadataService(self.subscription_key,self.endpoint)
        textresult = processortext.image_to_text(uploaded_file.stream)
        uploaded_file.stream.seek(0)
        imagetag = processorImage.image_tags(uploaded_file.stream)  
        uploaded_file.stream.seek(0)
        imageobj = processorImage.image_definition(uploaded_file.stream)
        uploaded_file.stream.seek(0)
        imgcordinates =  list(map(self.newcordinates, imageobj.objects))
        uploaded_file.stream.seek(0)
        imgDescription = processorImage.image_description(uploaded_file.stream)
        return imageobj, imagetag, imgcordinates, textresult,imgDescription


    def newcordinates(self, object):
        return coordinates( object.rectangle.x, object.rectangle.y, object.rectangle.w,  object.rectangle.h)
    

