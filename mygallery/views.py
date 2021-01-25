from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Location,Category

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    categorys = Category.get_categorys()
    print(locations)
    print(categorys)
    return render(request, 'index.html', {'images': images[::-1], 'locations': locations ,'categorys': categorys})


def location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'location.html', {'location_images': images})
def category(request, category):
    images= Image.filter_by_category(category)
    print(images)
    return render(request,'category.html', {'category_images': images })

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'search.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html', {"message": message})