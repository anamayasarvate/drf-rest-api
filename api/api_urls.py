from django.urls import path, include
from rest_framework import routers
import api.views as views

router = routers.DefaultRouter()

router.register('library', views.LibraryView, basename="library")

urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.library_list_view, name="libraries_list"),
    path('create/', views.library_create_view, name="libraries_list"),
    path('detail/<int:pk>/', views.library_detail_view, name="library_detail"),
    path('update/<int:pk>/', views.library_update_view, name="library_update"),
    path('delete/<int:pk>/', views.library_delete_view, name="library_delete"),

    path('class/list/', views.LibraryListView.as_view(), name="class_libraries_list"),

]