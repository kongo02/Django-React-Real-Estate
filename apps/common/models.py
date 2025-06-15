from django.db import models
import uuid

# Create your models here.
class TimeStampedUUIDModel(models.Model):
    """
    An abstract base class model that provides self-updating 'created' and 'modified' fields
    and a unique identifier field.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        #ordering = ['-created']