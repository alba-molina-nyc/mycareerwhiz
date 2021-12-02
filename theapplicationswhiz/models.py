from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Application(models.Model):
    title = models.CharField(max_length=255)
    #comes from foreign key from user-aka the super user we created just now but eventually expands to all users
    author = models.ForeignKey(User, on_delete=CASCADE)
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
    notes = models.TextField()

    def __str__(self):
        #concatenates self.author aka on admin page allows to see the title of app name and author self.author goes in a string bc it is an object and need to turn into a string
        return self.title + ' | ' + str(self.author)