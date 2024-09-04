from django.urls import path, re_path
from app_register import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from app_register.views import RegisterView, LoginView, UserListView, UserDetailView, UserUpdateView, UserDeleteView

schema_view = get_schema_view(
    openapi.Info(
        title= "api",
        default_version= 'v1',
        description= "Documentação",
    ),
    public= True, 
    permission_classes= (permissions.AllowAny,),
)

urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    re_path(r'^swagger(?P<format>.json|.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login')
]

