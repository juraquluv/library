from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer





class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class BookListAPIView(APIView):
#     def get(self,request):
#         books = Book.objects.all()
#         serializer_data = BookSerializer(books, many=True).data
#         return Response(serializer_data)
#









class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class BookDetailAPIView(APIView):
#     def get(self,request,pk):
#         try:
#             book = Book.objects.get(id=pk)
#             serializer = BookSerializer(book)
#             data ={
#                 "status":"Successfull",
#                 "book":serializer.data
#             }
#             return Response(data,status=status.HTTP_200_OK)
#         except Book.DoesNotExist:
#             return Response("Book not found")







class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class BookUpdateAPIView(APIView):
#     def put(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         data = request.data
#         serializer = BookSerializer(instance=book, data=data,partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return Response(serializer.data)



















class BookDeleteAPIView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookDeleteAPIView(APIView):
#     #1-usul
#     def delete(self, request, pk):
#         try:
#             book = Book.objects.get(id=pk)
#             book.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Book.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     #2 - usul
#     def delete(self, request, pk, format=None):
#         # Ob'ektni olish yoki 404 qaytarish
#         your_object = get_object_or_404(Book, pk=pk)   # tayyor get_object_or_404 funksiya borakan
#
#         # Ob'ektni o'chirish
#         your_object.delete()
#
#         # Muvaffaqiyatli o'chirish javobi
#         return Response(status=status.HTTP_204_NO_CONTENT)







class BookCreteAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class BookCreteAPIView(APIView):
#     def post(self, request):
#         data = request.data
#         serializer = BookSerializer(data = data)
#         if serializer.is_valid():
#             serializer.save()
#             data = serializer.data
#             return Response(data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    template_name = 'book_confirm_delete.html'
    serializer_class = BookSerializer


from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import Book

# class BookDeleteView(TemplateView):
#     template_name = 'book_confirm_delete.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         book = get_object_or_404(Book, pk=kwargs['pk'])
#         context['book'] = book
#         return context
#
#     def post(self, request, *args, **kwargs):
#         book = get_object_or_404(Book, pk=kwargs['pk'])
#         book.delete()
#         return HttpResponseRedirect(reverse_lazy('book-list'))
# @api_view(['GET'])
# def book_list_views(request,*args,**kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer