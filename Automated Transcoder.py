import json
import boto3

def copy(processedBucket, copySource, key):
    # Copy video to procssed
    try: 
        response = s3Client.copy_object(
            Bucket=processedBucket,
            CopySource=f"/{bucket}/720p-{key}",
            Key=key
        )
    except:
        raise S3.Client.exceptions.ObjectNotInActiveTierError
    
    print(response)
    
    # TO-DO Validate response
    
    # if response.statuscode == "OK":
    #    return True
    # else:
    #    return False

def transcode(bucket, key, formats):
    # Build a list of video formats
    for format in formats:
        
        # transcode in x format
        try:
            Name='string',
            InputBucket='string',
            OutputBucket='string',
            Role='string',
            AwsKmsKeyArn='string',
            Notifications={
                'Progressing': 'string',
                'Completed': 'string',
                'Warning': 'string',
                'Error': 'string'
            },
            ContentConfig={
                'Bucket': 'string',
                'StorageClass': 'string',
                'Permissions': [
                    {
                        'GranteeType': 'string',
                        'Grantee': 'string',
                        'Access': [
                            'string',
                        ]
                    },
                ]
            },
            ThumbnailConfig={
                'Bucket': 'string',
                'StorageClass': 'string',
                'Permissions': [
                    {
                        'GranteeType': 'string',
                        'Grantee': 'string',
                        'Access': [
                            'string',
                        ]
                    },
                ]
            }
        )
            
        except:
            ElasticTranscoder.Client.exceptions.ValidationException
            ElasticTranscoder.Client.exceptions.IncompatibleVersionException
            ElasticTranscoder.Client.exceptions.ResourceNotFoundException
            ElasticTranscoder.Client.exceptions.AccessDeniedException
            ElasticTranscoder.Client.exceptions.LimitExceededException
            ElasticTranscoder.Client.exceptions.InternalServiceException
            
        print(response)
        
        if response[CopyObjectResult][Etag] == "":
            return False
        else:
            
            # Copy procssed video to bucket
            copy(processedBucket, copySource, key
            
            return True
        
        
def lambda_handler(event, context):
    #print(json.dumps(event))
    tcClient = boto3.client('elastictranscoder')
    s3Client = boto3.client('s3')
    
    # default formats
    
    processedBucket = "elastictranscoderproject-videos-processed"
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        print(f"Bucket: '{bucket}'")
        print(f"Key: '{key}'")
    
        transcode(bucket,key)