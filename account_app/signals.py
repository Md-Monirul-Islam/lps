from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account, UserProfile

@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver function to create a UserProfile object for a newly created user.
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=Account)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal to save the UserProfile whenever the Account instance is saved.
    """
    instance.userprofile.save()