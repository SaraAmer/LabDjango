from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=25)



class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
   

class ISBN(models.Model):
    isbn_number=models.UUIDField(primary_key=True ,default=uuid.uuid4, editable=False)
    Author_name=models.CharField(max_length=50)
    Book_title=models.CharField(max_length=50)


class Book(models.Model):
    title=models.CharField(max_length=50)
    Description= models.TextField(max_length=2000)
    price=models.IntegerField(blank=True, null=True)
    Publishment_date=models.DateField(blank=True, null=True)
    Author= models.ForeignKey(User, related_name="books", on_delete=models.CASCADE ,blank=True, null=True)
    Category=models.ManyToManyField(Category)
    isbn_number=models.OneToOneField(ISBN, on_delete=models.CASCADE , blank=True, null=True)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)



    def __str__(self):
        return self.title


    