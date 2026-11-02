from django.db import models


class Post(models.Model):
    title_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts')
    def __str__(self):
        return self.title