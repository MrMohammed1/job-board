from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)

def image_upload(instance, filename):
    imagename, extension = filename.split('.')
    return f'jobs/{instance.id}.{extension}'


class Job(models.Model):
    title = models.CharField(max_length=50)
    # location
    owner = models.ForeignKey(User,  on_delete=models.CASCADE)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    catogery = models.ForeignKey("Catogery", on_delete=models.CASCADE)
    image = models.ImageField( upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)


    def __str__(self) -> str:
        return self.title
    

class Catogery(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = ("Catogeries")
    

class Apply(models.Model):
    job = models.ForeignKey("Job", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = ("Applies")
    



    




    





    

