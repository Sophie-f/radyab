from django.urls import path

from authentication.views import UserView, UsersView, ClassView

urlpatterns = [
    path('list/', UsersView.as_view()),
    path('list/<int:profile_id>/', UserView.as_view()),
    path('klass/', ClassView.as_view())
 ]
