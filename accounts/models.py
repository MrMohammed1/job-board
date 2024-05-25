from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey("City", on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/')

    class Meta:
        verbose_name_plural = ("profiless")


    def __str__(self):
        return str(self.user)




class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

@receiver(post_save, sender=User)
def _post_save_receiver(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])




