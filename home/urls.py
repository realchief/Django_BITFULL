
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
    url(r'^api/account_name/crud', views.AccountNameOptionView.as_view()),
    url(r'^api/account_name/all', views.AccountNameDisplayView.as_view()),
    # url(r'^api/retrieve_data/timeout_options', views.RetrieveDataTimeFrameView.as_view()),
    url(r'^api/retrieve_data/five_min/.*?$', views.RetrieveDataViewFiveMin.as_view()),
    url(r'^api/retrieve_data/fifteen_min/.*?$', views.RetrieveDataViewFifteenMin.as_view()),
    url(r'^api/retrieve_data/one_hour/.*?$', views.RetrieveDataViewOneHour.as_view()),
    url(r'^api/retrieve_data/four_hours/.*?$', views.RetrieveDataViewFourHours.as_view()),
    url(r'^api/retrieve_data/one_day/.*?$', views.RetrieveDataViewOneDay.as_view()),
    url(r'^api/retrieve_data/one_week/.*?$', views.RetrieveDataViewOneWeek.as_view()),
    url(r'^api/retrieve_data/one_month/.*?$', views.RetrieveDataViewOneMonth.as_view()),
    url(r'^api/retrieve_latest_data/', views.RetrieveLatestDataView.as_view()),
]