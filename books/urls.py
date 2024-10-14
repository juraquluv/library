from django.urls import path

from rest_framework.routers import SimpleRouter
from .views import BookListAPIView, BookDetailAPIView, BookUpdateAPIView, BookDeleteAPIView, BookCreteAPIView,BookListCreateAPIView,BookRetrieveUpdateAPIView,BookViewSet


router = SimpleRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns =[
    # path('books/', BookListAPIView.as_view(), name='book-list'),
    # path('bookListCreate/',BookListCreateAPIView.as_view(), name='book-list-create'),
    # path('bookRetrievUpdateDelete/<int:pk>',BookRetrieveUpdateAPIView.as_view(), name='book-retrieve-update'),
    # path('books/create/',BookCreteAPIView.as_view(), name='book-create'),
    # # path('books/',book_list_views),
    # path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    # path('books/<int:pk>/delete/', BookDeleteAPIView.as_view(), name='book-delete'),
    # path('books/<int:pk>/update/', BookUpdateAPIView.as_view(), name='book-update'),
]

urlpatterns += router.urls