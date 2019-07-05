from django.urls import path
from .views import listPerson, newPerson, updatePerson, deletePerson

urlpatterns = [
    path('list/', listPerson, name="personList"),
    path('new/', newPerson, name="personNew"),
    path('update/<int:id>/', updatePerson, name="personUpdate"),
    path('delete/<int:id>/', deletePerson, name="personDelete"),
]
