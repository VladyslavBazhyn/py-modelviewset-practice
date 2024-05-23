from rest_framework import viewsets

from author.models import Author
from author.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# from rest_framework import viewsets, status
# from rest_framework.generics import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from author.models import Author
# from author.serializers import AuthorSerializer
#
#
# class AuthorList(APIView):
#     def get(self, request):
#         genres = Author.objects.all()
#         serializer = AuthorSerializer(genres, many=True)
#         return Response(
#             serializer.data,
#             status=status.HTTP_200_OK
#         )
#
#     def post(self, request):
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(
#             serializer.data,
#             status=status.HTTP_201_CREATED
#         )
#
#
# class AuthorDetail(APIView):
#     def get_object(self, pk: int):
#         genre = get_object_or_404(Author, pk=pk)
#         return genre
#
#     def get(self, request, pk: int):
#         serializer = AuthorSerializer(self.get_object(pk=pk))
#         return Response(
#             serializer.data,
#             status=status.HTTP_200_OK
#         )
#
#     def put(self, request, pk: int):
#         serializer = AuthorSerializer(
#             self.get_object(pk=pk),
#             data=request.data
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def patch(self, request, pk: int):
#         genre = self.get_object(pk=pk)
#         serializer = AuthorSerializer(
#             genre,
#             data=request.data,
#             partial=True
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk: int):
#         self.get_object(pk=pk).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

