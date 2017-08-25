
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
    url(r'^api-token-auth/', auth_views.obtain_auth_token),
    url(r'^timeout_options/', views.TimeoutOptionView),
]