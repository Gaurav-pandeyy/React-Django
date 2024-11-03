from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializer import BookSerialzer


@api_view(['GET'])
def get_books(request):
    Book.objects.all()
    serializedData = BookSerialzer()
# Create your views here.
