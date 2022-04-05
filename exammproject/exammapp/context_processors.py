from  .models import Place

def menu_links(request):


    link=Place.objects.all()


    return dict(link=link)
