
import boto3

def get_name(photoS3Object):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('famous-people-faces-source')
    
    s3Client = boto3.client('s3')
    rekogClient = boto3.client('rekognition')
    
    pic_keys = [o.key for o in bucket.objects.all()]
    
    for pic in pic_keys:
        
        response=rekogClient.compare_faces(SimilarityThreshold=80,
                              SourceImage={'S3Object': {'Bucket':'famous-people-faces-source','Name': pic}},
                              TargetImage={'S3Object': photoS3Object})
        print (response['FaceMatches'])
        
        if len(response['FaceMatches']) == 0:
            continue
        
        for faceMatch in response['FaceMatches']:
            if faceMatch['Similarity'] > 99:
                responseTag = s3Client.get_object_tagging(
                    Bucket='famous-people-faces-source', 
                    Key=pic
                )
                print(responseTag['TagSet'][0]['Value'])
                return
            
    
    
def main(event, context):
    
    # TODO: currently reading from S3, we want to get input from Alexa 
    # bucket and name of the photo we want to check against the saved faces
    photoS3Object = {'Bucket':'famous-people-faces','Name':'barak_obama.jpg'}
    get_name(photoS3Object)
