from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    image_url = models.URLField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Note(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    image_url = models.URLField(blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title
