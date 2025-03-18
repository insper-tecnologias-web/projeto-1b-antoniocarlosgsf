from django.db import models

class Tag(models.Model):
    tag_name = models.CharField(max_length=200)

    def __str__(self):
        name = self.tag_name
        return f"{name}"
    
class Note(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{str(self.id)}. {str(self.title)}"
    


    

# Create your models here.
