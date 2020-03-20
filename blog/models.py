from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now_add=True)
    # publication date
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title