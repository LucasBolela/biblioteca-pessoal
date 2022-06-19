from rest_framework import viewsets, generics
from biblioteca.models import Author, Book, Place, PublishingCompany
from biblioteca.serializer import AuthorSerializer, BookSerializer, ListAuthorsOfBookSerializer, ListBooksFromAuthorSerializer, PlaceSerializer, PublishingCompanySerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AuthorViewSet(viewsets.ModelViewSet):
    """List all the Authors"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    """List all the books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class PlaceViewSet(viewsets.ModelViewSet):
    """List all the places"""
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class PublishingCompanyViewSet(viewsets.ModelViewSet):
    """List all the Publishing Companies"""
    queryset = PublishingCompany.objects.all()
    serializer_class = PublishingCompanySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListBooksFromAuthors(generics.ListAPIView):
    """List all the books from an Author"""
    def get_queryset(self):
        queryset = Book.objects.filter(author_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListBooksFromAuthorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListAuthorsOfBook(generics.ListAPIView):
    """List all the authors of a book"""
    def get_queryset(self):
        queryset = Author.objects.filter(book=self.kwargs['pk'])
        return queryset
    serializer_class = ListAuthorsOfBookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]