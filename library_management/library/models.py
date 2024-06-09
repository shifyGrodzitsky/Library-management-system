from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    from_age = models.IntegerField()
    to_age = models.IntegerField()
    loan_period = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    is_borrowed = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='book_pictures')

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

class BorrowedBook(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
