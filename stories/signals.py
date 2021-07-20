# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.conf import settings
# from django.shortcuts import reverse

# from .models import Story


# @receiver(post_save, sender=Story)
# def set_signed_url_on_create(sender, instance, created, **kwargs):
#     """
#     Post creation of Story instance (when using s3 storage backend) 
#     update default s3 url to signed s3 url
#     """
#     if not created:
#         return None
#     if settings.USE_AWS:
#         # point to view to generate signed url 
#         # for admin access to private s3 bucket
#         instance.pdf.url = reverse('download_story', args=[instance.id])
#         instance.save()

#         print('filefield url updated to download_story view url upon create')  # TEST
