from django.urls import path

from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
<<<<<<< HEAD
]
=======
]
>>>>>>> f0f4cc87bc06bbf7c394f704da06bf204c731eac
