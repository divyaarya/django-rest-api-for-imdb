from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response

from movies.models import Movies
from movies.serializers import MovieSerializer


@api_view(['GET'])
@permission_classes((AllowAny,))
def movie_get(request):
    pk = request.GET.get('pk', None)
    if pk is None or pk == '':
        movie_list = Movies.objects.all()
        serialize = MovieSerializer(movie_list, many=True)
        return Response(serialize.data)
    else:
        try:
            movie = Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialize = MovieSerializer(movie)
        return Response(serialize.data)


@api_view(['GET', 'POST'])
def movie_create(request):
    if request.method == 'GET':
        movie_list = Movies.objects.all()
        serialize = MovieSerializer(movie_list, many=True)
        return Response(serialize.data)
    if request.method == 'POST':
        if request.data != {}:
            serialize = MovieSerializer(data=request.data)
            if serialize.is_valid():
                serialize.save()
            # try:
                return Response(serialize.data, status=status.HTTP_201_CREATED)
            # except Exception as e:
            #     print(e)
            else:
                return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_edit(request, pk):
    # if request.method == 'GET':
    try:
        movie = Movies.objects.get(pk=pk)
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = MovieSerializer(movie)
        return Response(serialize.data)
    if request.method == 'PUT':
        if request.data != {}:
            serialize = MovieSerializer(movie, data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data)
            else:
                return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)