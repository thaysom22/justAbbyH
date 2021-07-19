import boto3
from botocore.exceptions import ClientError


# CREDIT [5]
def create_presigned_url(bucket_name, object_key, expiration=300):
    """
    Generate a presigned URL to share an S3 object
    :param bucket_name: string
    :param object_key: string (full path in s3)
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': object_key,
            },
            ExpiresIn=expiration
        )
    except ClientError:
        return None

    # The response contains the presigned URL
    return response
