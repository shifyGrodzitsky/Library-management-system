from django.urls import path
from .views import home, register_view, login_view, books,logout_view,borrowedBookFunc,books_borrowed,return_book,reports

urlpatterns = [
    path('', home, name='Home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('books/', books, name='books'),
    path('logout/', logout_view, name='logout'),
    path('books_borrowed/', books_borrowed, name='books_borrowed'),
    path('report/', reports, name='report'),
    path('books/borrowe/<int:bookId>/', borrowedBookFunc, name='borrowe'),
    path('books_borrowed/return/<int:id>/', return_book, name='return'),

    # Add other URL patterns for your project's pages here
]

