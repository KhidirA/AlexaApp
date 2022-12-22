#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def compare_faces(sourceS3Object, targetS3Object):
    client=boto3.client('rekognition')

    response=client.compare_faces(SimilarityThreshold=80,
                                  SourceImage={'S3Object': sourceS3Object},
                                  TargetImage={'S3Object': targetS3Object})
    
    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
               str(position['Left']) + ' ' +
               str(position['Top']) +
               ' matches with ' + similarity + '% confidence')
  
    return len(response['FaceMatches'])          

def main(event, context):
    sourceS3Location = {'Bucket':'famous-people-faces','Name':'barak_obama.jpg'}
    targeS3Location = {'Bucket':'famous-people-faces-source','Name':'barak_obama_source.jpg'}
    face_matches=compare_faces(sourceS3Location, targeS3Location)
    print("Face matches: " + str(face_matches))
