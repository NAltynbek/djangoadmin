# admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
#admin.site.register(Book)
#admin.site.register(BookInstance)
# Register the Admin classes for Book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pa
# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    pass
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'
    class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')