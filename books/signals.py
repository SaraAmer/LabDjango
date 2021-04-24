from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ISBN , Book
@receiver(post_save , sender=Book)
def after_book_creation(sender , instance, created, *args, **kwargs):
    if created:
        isbn_create=ISBN(Author_name=instance.Author.username)
        isbn_create.save()
        instance.isbn_number=isbn_create
        instance.save()


