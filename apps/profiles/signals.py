import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from real_estate.settings.base import AUTH_USER_MODEL
from apps.profiles.models import Profile

logger = logging.getLogger(__name__)

@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a user profile when a new user is created.
    """
    if created:
        logger.info(f"Creating profile for user: {instance.username}")
        Profile.objects.create(user=instance)
    else:
        logger.info(f"User profile already exists for user: {instance.username}")
        
@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    Save the user profile when the user is saved.
    """
    try:
        instance.profile.save()
        logger.info(f"Profile for user {instance.username} saved successfully.")
    except Profile.DoesNotExist:
        logger.error(f"Profile for user {instance.username} does not exist.")
    except Exception as e:
        logger.error(f"Error saving profile for user {instance.username}: {e}")
