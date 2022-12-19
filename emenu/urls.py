from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from apps.dishes import views as food_views

schema_view = get_schema_view(
    openapi.Info(
        title="Food API",
        default_version='v1',
        description="API Documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

v1 = [
    path('menu/', include([
        path(
            'foods/', food_views.CategoryWithFoodListView.as_view(),
            name='food-list'
        )
    ]))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(v1))
]

if settings.DEBUG:
    urlpatterns += [
        path(
            'swagger/',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui',
        )
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)