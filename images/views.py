from django.shortcuts import render
from .models import Image_Location, Image, Categories
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def welcome(request):
    images = Image.all_images()
    return render(request, 'all-images.html',{'images': images})

def search_results(request):

    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        print(search_term)
        searched_images = Image.search_by_category(search_term)
        print(searched_images)
        message = f'{search_term}'
        params = {
            'searched_images': searched_images,
            'message': message,
        }

        return render(request, 'search.html',params)

    else:
        
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})