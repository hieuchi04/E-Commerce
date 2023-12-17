from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/categories/', include('apps.category.urls')),
    path('api/product/', include('apps.product.urls')),
    path('api/cart/', include('apps.cart.urls')),
    path('api/shipping/', include('apps.shipping.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)