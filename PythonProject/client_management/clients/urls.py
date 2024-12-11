from django.urls import path
from .views import ClientListCreateView, ClientDetailView, ProjectListCreateView, ProjectDetailView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='clients'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('projects/', ProjectListCreateView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

]
