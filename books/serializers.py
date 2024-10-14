from django.template.defaultfilters import title
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate(self,data):
        title_obj = data.get('title',None)
        author_obj = data.get('author',None)
        # check title if it only alphabetical
        if not title_obj.isalpha():
            raise ValidationError({
                "message": "Title must be alphanumeric"
            })
        # chech title and author from database existence
        if Book.objects.filter(title=title_obj,author = author_obj).exists():
            raise ValidationError({
                "message": "Sarlavha va Avtor bir xil bo'lolmaydi"
            })
        return data

    def validate_price(self,price):
        if price <= 0:
            raise ValidationError({
                "message": "Narx noto'g'ri kiritilgan"
            })
        return price