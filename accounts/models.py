from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.forms import forms
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save


# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    pincode = models.DecimalField(max_digits=6 , decimal_places=0)
    website = models.URLField(verbose_name="website")
    photo = models.FileField(upload_to="college" , blank=True)
    slug = models.SlugField(max_length=50 , unique=True , default=slugify(name))
    def __str__(self):
        return self.name


    # def _get_unique_slug(self):
    #     slug = slugify(self.name)
    #     unique_slug = slug
    #     num = 1
    #     while College.objects.filter(slug=unique_slug).exists():
    #         unique_slug = '{}-{}'.format(slug, num)
    #         num += 1
    #     return unique_slug
    #
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = self._get_unique_slug()
    #     super().save()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50,  default="hel" )
    ch = College.objects.values('name')
    tup = []
    for a in ch:
        tup.append([a['name'],a['name']])
    college_name = models.CharField(max_length=30, blank=True , choices = tup)
    def __str__(self):
        return self.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    #instance.profile.username = User.objects.get('username')
    instance.profile.save()


def pre_post_college(sender , instance , *args , **kwargs):
    slug = slugify(instance.name)
    unique_slug = slug
    num = 1
    while College.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    instance.slug = unique_slug


pre_save.connect(pre_post_college , sender=College)