from django.contrib import admin
from biblioteca.models import Author, Book, CreatedUpdated, Place, PublishingCompany

class CreatedUpdated(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at')
    class Meta:
        abstract = True

class PublishingCompanies(CreatedUpdated):
    list_display = ('name', 'state_or_city')

admin.site.register(PublishingCompany, PublishingCompanies)

class Authors(CreatedUpdated):
    list_display = ('name',)

admin.site.register(Author, Authors)

class Places(admin.ModelAdmin):
    list_display = ('number', 'letter')

admin.site.register(Place, Places)

class Books(CreatedUpdated):
    list_display = ('title', 'publication_year', 'pages', 'subject')
    list_per_page = 20

admin.site.register(Book, Books)
