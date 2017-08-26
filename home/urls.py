
from django.conf.urls import url, include
from rest_framework import routers
# from compounding_dashboard.home import views
from rest_framework.authtoken import views as auth_views
from home import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^api/api-token-auth/', auth_views.obtain_auth_token),
    url(r'^api/timeout_options/', views.TimeoutOptionView.as_view()),
]