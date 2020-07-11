from django.db import models
from django.contrib.auth.models import User

class Inquiry(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    inquirystatus = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="inquiries")
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'inquiries'
        db_table = 'inquiries'

    def __str__(self):
        return self.title
