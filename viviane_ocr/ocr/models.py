from django.db import models
from viviane_ocr.users.models import User

class File(models.Model):
    
    file_name = models.CharField(max_length=200)
    
    extension = models.CharField(max_length=10)

    length = models.BigIntegerField()

    content = models.TextField(null=True,blank=True)

    upload_by = models.ForeignKey(User, on_delete=models.CASCADE)

    done = models.BooleanField(default=False)

    class Meta:

        db_table = 'files'
    
    def __str__(self):
        return self.file_name


