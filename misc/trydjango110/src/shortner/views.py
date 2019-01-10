from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View

from .forms import SubmitUrlForm
from .models import KirrURL
from .utils import create_shortcode

from analytics.models import ClickEvent
# # Create your views here.
# def kirr_function_based_view(request, shortcode=None, *args, **kwargs):
# 	print('kwargs: ', kwargs)
# 	print('shortcode: ', shortcode)
# 	try:
# 		obj = KirrURL.objects.get(shortcode=shortcode)
# 		url = obj.url
# 	except:
# 		obj = KirrURL.objects.first()
# 		url = obj.url + " (DEFAULT)"
# 	return HttpResponse('helloooooo url[{}]. You hit A.'.format(url))


# # Create your views here.
# def kirr_function_based_view(request, shortcode=None, *args, **kwargs):
# 	print('kwargs: ', kwargs)
# 	print('shortcode: ', shortcode)
# 	url = None
# 	qs = KirrURL.objects.filter(shortcode__iexact = shortcode.upper())
# 	if qs.exists() and qs.count() ==1:
# 		obj = qs.first()
# 		url = obj.url
# 	return HttpResponse('helloooooo url[{}]. You hit A.'.format(url))



# Create your views here.
def kirr_function_based_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)


class KirrClassBasedView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        print('kwargs: ', kwargs)
        print('shortcode: ', shortcode)
        obj = KirrURL.objects.get(shortcode=shortcode)
        return HttpResponse('Hello Again, url[{}]. You hit B.'.format(obj.url))


# Put this 'SubmitUrlForm' code in both method types, as first hit of URL is using get method
class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        if form.is_valid():
            print(form.cleaned_data)
        context = {
            "title": "Submit URL",
            "form" : form,
        }
        return render(request, "shortner/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Submit URL",
            "form" : form,
        }
        if form.is_valid():
            new_url = form.cleaned_data.get('url_1234')
            objects_count = KirrURL.objects.filter(url=new_url).count()
            if objects_count == 0:
                obj, created = KirrURL.objects.get_or_create(url=new_url, shortcode=create_shortcode(KirrURL(new_url)))
            else:
                obj = KirrURL.objects.filter(url=new_url).first()
                created = False
            context = {
                "object" : obj,
                "created": created,
            }
            template = "shortner/home.html"
            if created:
                template = "shortner/success.html"
            else:
                template = "shortner/already-exists.html"
            return render(request, template, context)
        return render(request, "shortner/home.html", context)

class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        print("#######Count#########:: ", ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)