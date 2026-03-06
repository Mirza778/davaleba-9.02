from django.urls import path
from . import views

urlpatterns = [
    # Director endpoints
    path('directors/', views.DirectorListCreateView.as_view(), name='director-list-create'),
    path('directors/<int:pk>/', views.DirectorDetailView.as_view(), name='director-detail'),

    # Movie endpoints
    path('movies/', views.MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),

    # Review endpoints
    path('reviews/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
]
