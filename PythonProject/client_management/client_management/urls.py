# client_management/urls.py
from django.contrib import admin
from django.urls import path, include
from clients import views  # Import views from clients
from django.http import HttpResponse
from clients.views import ClientListCreateView

# Create a simple view to handle the root URL
def home(request):
    return HttpResponse("Welcome to the Client Management System!")

urlpatterns = [
    path('', home, name='home'),  # Root URL pattern
    path('admin/', admin.site.urls),
    path('clients/', views.ClientListCreateView.as_view(), name='client-list-create'),
    path('api/', include('clients.urls')),  # API URLs
]
