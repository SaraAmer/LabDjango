from ..models import Book 
from .serializer import BookSerializer , UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
@api_view(["GET"])
def index(request):
    book = Book.objects.all()
    serializer = BookSerializer(instance=book , many=True)
    return Response(data=serializer.data , status=status.HTTP_200_OK)
 
@api_view(["POST"])
@permission_classes([IsAuthenticated])   
def create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            'message': "The book has been added successfully"

        }
        , status=status.HTTP_201_CREATED)
    else :
        return Response(data={
            "success": False,
            "error": serializer.errors
        },status=status.HTTP_400_BAD_REQUEST) 
           
@api_view(['GET'])
@permission_classes([IsAuthenticated])   
def show(request , id):
    try:
     book = Book.objects.get(pk=id)
    except:
         return Response(data={
             "message":"This Book is not Found"
         },status=status.HTTP_404_NOT_FOUND)
    serializer = BookSerializer(instance=book)
    return Response(data=serializer.data , status=status.HTTP_200_OK)
@api_view(['GET' , 'DELETE'])
@permission_classes([IsAuthenticated])   
def delete(request , id):
    try:
         book = Book.objects.get(pk=id)
         book.delete()
    except:
         return Response(data={
             "message":"This Book is not Found"
         },status=status.HTTP_404_NOT_FOUND)


   
    return Response(data={
        "success":True,
        "message":"deleted successfully",

    }, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])       
def edit(request , id):
    try:
      book = Book.objects.get(pk=id)
    except:
         return Response(data={
             "message":"This Book is not Found"
         },status=status.HTTP_404_NOT_FOUND)  
    serializer = BookSerializer(book,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            'message': "The book has been updated successfully"

        }
        , status=status.HTTP_201_CREATED)
    else :
        return Response(data={
            "success": False,
            "error": serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,
            "message": "User has been registered successfully"
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

