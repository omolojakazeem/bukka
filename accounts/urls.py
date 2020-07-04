from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import UserView

urlpatterns = [
    path('',UserView.as_view(), name='account'),
    path('login/',jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]