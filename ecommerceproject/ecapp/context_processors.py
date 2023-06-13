from . models import Category ,Product
def menu_links(request):
    #links=Category.objects.all()
    links = Product.objects.all()
    return dict(links=links)