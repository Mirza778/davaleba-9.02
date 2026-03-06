

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer


# ============================================================
# TODO: DirectorListCreateView
#
# GET  → დააბრუნეთ ყველა რეჟისორის სია
#        1. წამოიღეთ ყველა Director ობიექტი
#        2. გადაეცით DirectorSerializer-ს (many=True)
#        3. დააბრუნეთ Response(serializer.data)
#
# POST → შექმენით ახალი რეჟისორი
#        1. შექმენით DirectorSerializer(data=request.data)
#        2. შეამოწმეთ is_valid()
#        3. თუ ვალიდურია - save() და დააბრუნეთ 201
#        4. თუ არა - დააბრუნეთ errors და 400
# ============================================================
class DirectorListCreateView(APIView):

    def get(self, request):
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ============================================================
# TODO: DirectorDetailView
#
# GET    → დააბრუნეთ კონკრეტული რეჟისორი pk-ით
#          1. გამოიყენეთ get_object_or_404(Director, pk=pk)
#          2. სერიალიზაცია და Response
#
# PUT    → განაახლეთ რეჟისორი მთლიანად
#          1. იპოვეთ ობიექტი get_object_or_404-ით
#          2. DirectorSerializer(director, data=request.data)
#          3. is_valid() → save() → Response
#
# DELETE → წაშალეთ რეჟისორი
#          1. იპოვეთ ობიექტი
#          2. object.delete()
#          3. Response(status=204)
# ============================================================
class DirectorDetailView(APIView):
    def get(self, request, pk):
        director = get_object_or_404(Director, pk=pk)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)
    def put(self, request, pk):
        director = get_object_or_404(Director, pk=pk)
        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        director = get_object_or_404(Director, pk=pk)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# ============================================================
# TODO: MovieListCreateView
#
# GET  → დააბრუნეთ ყველა ფილმის სია
# POST → შექმენით ახალი ფილმი
# ============================================================
class MovieListCreateView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ============================================================
# TODO: MovieDetailView
#
# GET    → დააბრუნეთ კონკრეტული ფილმი pk-ით
# PUT    → განაახლეთ ფილმი მთლიანად
# PATCH  → განაახლეთ ფილმი ნაწილობრივ (partial=True)
# DELETE → წაშალეთ ფილმი
# ============================================================
class MovieDetailView(APIView):

    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    def put(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# ============================================================
# TODO: ReviewListCreateView
#
# GET  → დააბრუნეთ ყველა შეფასება
# POST → შექმენით ახალი შეფასება
# ============================================================
class ReviewListCreateView(APIView):

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer,save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ============================================================
# TODO: ReviewDetailView
#
# GET    → დააბრუნეთ კონკრეტული შეფასება pk-ით
# DELETE → წაშალეთ შეფასება
# ============================================================
class ReviewDetailView(APIView):
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    def delete(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

