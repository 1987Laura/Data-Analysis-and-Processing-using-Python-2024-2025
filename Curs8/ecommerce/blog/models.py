from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

#MakeMigrations
#create table BlogPost(id INT, title)

#Migrate
#executia
