from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance
# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

# if you want the fields vertical put them in a tuple () if you want them in horizontal then add them in a list [].

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Author, AuthorAdmin)

#this is calle TabularInline it will put the book instance copys with the book to give you a view of instances associated with the book.
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]



    

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')


    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')

        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
