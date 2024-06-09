from datetime import date
from operator import attrgetter
from datetime import date, timedelta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import models
from django.db.models import ExpressionWrapper, F
from . import models
from .models import Book,Customer,Category,BorrowedBook
from .forms import LoginForm,RegisterForm
from django.contrib.auth import logout

def login_view(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            name = loginForm.cleaned_data["username"]
            pswd = loginForm.cleaned_data["password"]
            user = authenticate(request, username=name, password=pswd)
            if user:
                request.session['UserLogIn'] = user.id
                login(request, user)
                return redirect('Home')
            else:
                return redirect("register")
    else:
        loginForm = LoginForm()

    return render(request, "login.html", {"form": loginForm})



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create a new Django User
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            # Create a new Customer
            customer = Customer.objects.create(
                user=user,
                date_of_birth=form.cleaned_data['date_of_birth'],
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone']
            )
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})



def home(request):
    return render(request, 'Home.html')




def logout_view(request):
    logout(request)
    return redirect('Home')


def books(request):
    book_list = Book.objects.all()
    user_id = request.user.id
    if(user_id):
        user = Customer.objects.get(user_id=user_id)
        age = date.today().year - user.date_of_birth.year
        CategoryFilter = Category.objects.filter(from_age__lte=age,to_age__gte=age)
        BookFilter= Book.objects.filter(category__in=CategoryFilter)
        data = {
            "books": BookFilter
        }
    else:
        data = {
            "books": book_list
        }
    return render(request, 'books.html', data)

def borrowedBookFunc(request, bookId):
    book=Book.objects.filter(id=bookId).first()
    if(book.is_borrowed == False):
        book.is_borrowed = True
        book.save()
        user_id = request.user.id
        user = Customer.objects.get(user_id=user_id)
        borrowe = BorrowedBook.objects.create(book=book, user=user, borrow_date=date.today())
        borrowe.save()
        return redirect('books')

def books_borrowed(request):
    user_id = request.user.id
    user = Customer.objects.get(user_id=user_id)
    user_borrowed_list = BorrowedBook.objects.filter(user=user).all()
    context = {
        "borrowed": user_borrowed_list,
        "user":user
    }
    return render(request, 'books_borrowed.html', context)

def return_book(request, id):
    borrowe = BorrowedBook.objects.filter(id=id).first()
    borrowe.book.is_borrowed=False
    borrowe.book.save()
    borrowe.delete()
    return redirect('books_borrowed')




def reports(request):
    today = date.today()
    overdue_books = []

    borrowed_books = BorrowedBook.objects.all()
    for book in borrowed_books:
        loan_period = book.book.category.loan_period
        if book.borrow_date <= (today - timedelta(days=loan_period)):
            overdue_books.append(book)
    return render(request, 'report.html', {'overdue_books': overdue_books})