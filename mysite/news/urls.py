from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('Category/<int:Category_id>/', get_category, name='Category'),

]
