"""myfinance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


SCHEMA_VIEW = get_schema_view(title='myfinance API',
                              renderer_classes=[OpenAPIRenderer,
                                                SwaggerUIRenderer])

urlpatterns = [
    path('', RedirectView.as_view(url="/admin/")),
    path('admin/', admin.site.urls),
    path('payroll/', include('payroll.urls', namespace='payroll')),
    path('api-token-auth/', obtain_jwt_token),
    path('docs/', SCHEMA_VIEW),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
