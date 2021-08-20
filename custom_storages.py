from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


# CREDIT [3]
# subclassing and overriding attribute names
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    bucket_name = settings.AWS_STORAGE_PUBLIC_BUCKET_NAME
    custom_domain = settings.AWS_S3_CUSTOM_PUBLIC_DOMAIN
    file_overwrite = True


class PublicFileStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_PUBLIC_LOCATION
    bucket_name = settings.AWS_STORAGE_PUBLIC_BUCKET_NAME
    custom_domain = settings.AWS_S3_CUSTOM_PUBLIC_DOMAIN
    file_overwrite = False


class PrivateFileStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_PRIVATE_LOCATION
    bucket_name = settings.AWS_STORAGE_PRIVATE_BUCKET_NAME
    custom_domain = settings.AWS_S3_CUSTOM_PRIVATE_DOMAIN
    file_overwrite = False
