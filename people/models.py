from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


#  https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id_int = models.IntegerField("Employee Num:", default=0)
    notes_str = models.TextField("notes", max_length=500, blank=True)
    location_str = models.CharField("Location Code", max_length=30, blank=True)
    cust_str = models.CharField("cust ID", max_length=6, blank=True)
    # birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

