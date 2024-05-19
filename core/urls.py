from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('category/<int:category_id>', CategoryView.as_view(), name='category'),
    path('redirect/', RedirectView.as_view(), name='redirect'),
    path('form/', SimpleForm.as_view(), name='form'),
]
