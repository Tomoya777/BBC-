from django.db import models
from markdownx.models import MarkdownxField
from django.utils.safestring import mark_safe
from markdownx.utils import markdownify

class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    text = MarkdownxField(blank=True, max_length=10000)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

