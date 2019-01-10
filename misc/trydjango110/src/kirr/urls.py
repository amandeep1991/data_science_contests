"""kirr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin
# from shortner.views import KirrClassBasedView, kirr_function_based_view

# urlpatterns = [
#     url(r'^admin/', admin.site.urls), # This is what we have typed as admin as suffix post simple url shown on server start on console
#     # url(r'^view-1/$', kirr_function_based_view),
#     # url(r'^view-2/$', KirrClassBasedView.as_view()),

#     url(r'^a/(?P<shortcode>[\w-]+){6,15}/$', kirr_function_based_view),
#     url(r'^b/(?P<shortcode>[\w-]+)/$', KirrClassBasedView.as_view()),
# ]


from django.conf.urls import url
from django.contrib import admin
from shortner.views import KirrClassBasedView, HomeView, URLRedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls), # This is what we have typed as admin as suffix post simple url shown on server start on console
    url(r'^$', HomeView.as_view()),
    # url(r'^(?P<shortcode>[\w-]{6,15})/$', KirrClassBasedView.as_view(), 'shortcode_url'),
    url(r'^(?P<shortcode>[\w-]{6,15})/$', URLRedirectView.as_view(), 'shortcode_url'),
]