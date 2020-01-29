from django.db import models
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

#kullanici:gul
#parola:1234

# Create your models here.
choices = [(i, i) for i in range(1990, datetime.now().year + 1)]
cities = (('54','Sakarya'), ('34','Istanbul'))


class Profile(models.Model):
    user = models.OneToOneField(to='auth.User', on_delete=models.CASCADE)
    picture = models.ImageField(blank=True)
    #age = models.PositiveSmallIntegerField(choices=choices,)
    city = models.CharField(choices=cities, max_length=20)

    def __str__(self):
        return f"{self.user.username} 'nin profili"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)   #ilk defa yaratiliyorsa profili yok demktir o yuzden profili ekledik
    instance.profile.save()    
