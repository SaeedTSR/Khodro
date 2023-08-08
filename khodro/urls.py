from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'khodro'

urlpatterns = [
    path('', views.KhodroListCreateView.as_view(), name="list"),
    path('<int:pk>/', views.KhodroRetrieveUpdateDestroyView.as_view(), name="detail"),
]

# router = SimpleRouter()

# router.register("", views.KhodroViewSet)

# urlpatterns += router.urls