from django.contrib import admin
from .models import Book , Tag, ISBN ,Category 
from .forms import BookForm , CategoryForm
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ("title", "Author", "Description")
    list_filter = ("Category", )

class BookInline(admin.StackedInline):
    model = Book
    max_num = 3
    extra = 1

class TagAdmin(admin.ModelAdmin):
    inlines = [BookInline]
class CategoryAdmin(admin.ModelAdmin):
     form = CategoryForm
     

admin.site.register(Book , BookAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ISBN)
admin.site.register(Category , CategoryAdmin)    