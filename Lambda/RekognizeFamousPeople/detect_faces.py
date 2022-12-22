import json
import boto3

def detect_faces(photo, bucket):
    # boto3 provides low-level API access to AWS services 
    # - in this case reckognition 
    client = boto3.client("rekognition")
    
    response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])
    
    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')

        print('Here are the other attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))

		# Access predictions for individual face details and print them
        print("Gender: " + str(faceDetail['Gender']))
        print("Smile: " + str(faceDetail['Smile']))
        print("Eyeglasses: " + str(faceDetail['Eyeglasses']))
        print("Emotions: " + str(faceDetail['Emotions'][0]))
    
    return len(response['FaceDetails'])
    
def main(event, context):
    photo='barak_obama.jpg'
    bucket='famous-people-faces'
    face_count=detect_faces(photo, bucket)
    print("Faces detected: " + str(face_count))
