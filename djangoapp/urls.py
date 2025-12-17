from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *



urlpatterns = [
    # later your api urls here
    path('products/', product_list),
    path('products/<int:id>/', product_detail),
    path('auth/signup/', register_user),
    path('auth/login/', login_user),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
