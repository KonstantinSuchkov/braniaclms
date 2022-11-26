from mainapp import views
from mainapp.apps import MainappConfig
from django.urls import path, include


app_name = MainappConfig.name


urlpatterns = [
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('docsite/', views.DocSiteView.as_view(), name='docsite'),
    path('', views.IndexViewView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path("news/", views.NewsListView.as_view(), name="news"),
    path("news/create/", views.NewsCreateView.as_view(), name="news_create"),
    path("news/<int:pk>/detail", views.NewsDetailView.as_view(), name="news_detail",),
    path("news/<int:pk>/update", views.NewsUpdateView.as_view(), name="news_update",),
    path("news/<int:pk>/delete", views.NewsDeleteView.as_view(), name="news_delete",),
    path("courses/", views.CoursesListView.as_view(), name="courses"),
    path("courses/<int:pk>/", views.CoursesDetailView.as_view(), name="courses_detail",),
    path("course_feedback/", views.CourseFeedbackFormProcessView.as_view(), name="course_feedback",),
]
