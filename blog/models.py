from django.db import models

<<<<<<< HEAD
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
    def __str__(self):
      return f'[{self.pk}]{self.title}'
=======
# Create your models here.
>>>>>>> 9db7e0f14ca431b9693eaceff4b6023b24bb891c
