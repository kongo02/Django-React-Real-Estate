from django.db import models
from django.contrib.auth import get_user_model
#from common.models import TimeStampedUUIDModel
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel

# Create your models here.
User = get_user_model()

class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")
    PREFER_NOT_TO_SAY = "Prefer not to say", _("Prefer not to say")
    
class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), blank=True, null=True, unique=True,max_length=12, default="+27721046440")
    about_me = models.TextField(verbose_name=_("About Me"), default="Say something about yourself")
    estate_license = models.CharField(verbose_name=_("Real Estate License"), max_length=20, blank=True, null=True)
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"), default="/profile_default.png")
    gender = models.CharField(verbose_name=_("Gender"),choices=Gender.choices, default=Gender.PREFER_NOT_TO_SAY, max_length=20)
    country= CountryField(verbose_name=_("Country"), blank=False, null=False, default="ZA")
    city = models.CharField(verbose_name=_("City"), max_length=100, blank=False, null=False, default="Johannesburg")
    is_buyer = models.BooleanField(verbose_name=_("Buyer"), default=False, help_text=_("Are you looking to Buy a Property?"))
    is_seller = models.BooleanField(verbose_name=_("Seller"), default=False, help_text=_("Are you looking to Sell a Property?"))
    is_agent = models.BooleanField(verbose_name=_("Agent"), default=False, help_text=_("Are you an Agent?"))
    top_agent = models.BooleanField(verbose_name=_("Top Agent"), default=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name=_("Rating"))
    num_reviews = models.IntegerField(verbose_name=_("Number of Reviews"), default=0, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    