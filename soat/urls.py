from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('watches/', WatchView.as_view()),
    path('', HomeView.as_view()),
    path('watch/<int:id>/', OneWatchView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
    path('buylist/', BuyListView.as_view()),
    path('buylistadd/<int:id>/', AddBuyList.as_view()),
    path('deletebuylist/<int:id>/', DeleteBuyList.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)