from django.db import models

class CreatedUpdated(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class PublishingCompany(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    city = models.CharField(max_length=15, default="")
    state = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.name

class Author(CreatedUpdated):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name

class Place(models.Model):
    number = models.PositiveIntegerField(blank=False, null=False)
    letter = models.CharField(max_length=1, blank=False, null=False)

    def __str__(self):
        return f"{self.number} - {self.letter}"

class Book(CreatedUpdated):
    publishing_company = models.ForeignKey(PublishingCompany, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    author_id = models.ManyToManyField(Author)
   
    title = models.CharField(max_length=100, blank=False, null=False)
    publication_year = models.CharField(max_length=4)
    pages = models.PositiveIntegerField()
    subject = models.CharField(max_length=250)

    def __str__(self):
        return self.title