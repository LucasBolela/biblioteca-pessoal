from rest_framework import serializers
from biblioteca.models import Author, Book, Place, PublishingCompany

# Basic Routes
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['title', 'publication_year', 'pages', 'subject', 'publishing_company', 'place', 'author_id', 'authors']

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class PublishingCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = PublishingCompany
        fields = '__all__'

# Joinned routes
class ListBooksFromAuthorSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')
    class Meta:
        model = Book
        fields = '__all__'

class ListAuthorsOfBookSerializer(serializers.ModelSerializer):
    book_title = serializers.ReadOnlyField(source='book.title')
    class Meta:
        model = Book
        fields = '__all__'