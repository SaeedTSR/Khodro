from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'khodro'

urlpatterns = [
    path('', views.KhodroListCreateView.as_view(), name="list-create"),
    path('<int:pk>/', views.KhodroRetrieveUpdateDestroyView.as_view(), name="get-update-delete"),
]

# router = SimpleRouter()

# router.register("", views.KhodroViewSet)

# urlpatterns += router.urls