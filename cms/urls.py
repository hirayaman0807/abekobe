from django.urls import path

from . import views
from django.urls import path

from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.UserCreate.as_view(), name='signup'),
<<<<<<< HEAD
]
=======
]
>>>>>>> f0f4cc87bc06bbf7c394f704da06bf204c731eac
