from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404

from .models import KirrURL

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
	obj = get_object_or_404(KirrURL, shortcode = shortcode)
	return HttpResponseRedirect(obj.url)

class KirrClassBasedView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		print('kwargs: ', kwargs)
		print('shortcode: ', shortcode)
		obj = KirrURL.objects.get(shortcode=shortcode)
		return HttpResponse('Hello Again, url[{}]. You hit B.'.format(obj.url))
