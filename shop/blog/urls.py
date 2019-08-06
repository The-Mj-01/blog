from django.urls import path , register_converter

from .extensions import converters
from . import views


register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    #ex: hostname/blog
    path('' , views.index , name='index'),

    # ex: hostname/blog/5
    path('<int:post_id>' , views.detail , name='detail'),
    path('archive/<yyyy:year>/' , views.archive_year , name='archive')
]