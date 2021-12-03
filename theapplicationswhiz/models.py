from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

# Create your models here.

class Application(models.Model):
    title = models.CharField(max_length=255)
    #comes from foreign key from user-aka the super user we created just now but eventually expands to all users
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    job_post = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_website = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    company_size = models.CharField(max_length=255)
    submission_status = models.CharField(max_length=255)
    remote = models.CharField(max_length=255)
    next_steps = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title + ' | ' + str(self.user)

    def get_absolute_url(self):
        return reverse('application-detail', kwargs={'pk': self.id})


class Note(models.Model):
    application = models.ForeignKey(Application, related_name="notes", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.application.body, self.name)

# class Interview(models.Model):
#     date = models.DateField('Interviewing Date')
#     body = models.TextField()
#     location = models.TextField()
#     application = models.ForeignKey(Application,  on_delete=models.CASCADE)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return '%s - %s' % (self.application.body, self.location)

#     class Meta:
#         ordering = ('-date',)