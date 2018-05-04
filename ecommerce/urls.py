"""ecommerce URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from accounts.views import (LoginView,
                            RegisterView,
                            guest_register_view,
                            logout_view)
from .views import home_page
from contact.views import contact_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('guest/', guest_register_view, name='guest_register'),
    path('contact/', contact_page, name='contact'),
    path('account/', include(('accounts.urls', 'account'))),
    path('settings/', RedirectView.as_view(url='/account')),
    path('products/', include(('products.urls', 'products'))),
    path('search/', include(('search.urls', 'search'))),
    path('cart/', include(('carts.urls', 'carts'))),
    path('billing/', include(('billing.urls', 'billing'))),
    path('accounts/', include('accounts.password.urls')),
    # path('category/', include(('categories.urls', 'category'))),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
