from django.shortcuts import render, get_object_or_404, redirect
from Games.models import Game, Engine, Publisher, Developer, Plattform


redirectStr = {
    'Game': "/search/{0}",
}

# Create your views here.
def home_view(request):
    query = request.GET.get('Search', '')
    selection = request.GET.get('Dropdown', '')
    print(selection)
    if query and selection != "AllGames":
        return redirect("/search/{0}/{1}".format(selection, query))
    elif selection == "AllGames":
        return redirect("/search/AllGames/Alle Spiele")
    else:
        return render(request, "home.html", {'query': '/'})


def detail_game_view(request, id):
    obj = get_object_or_404(Game, id=id)
    if(obj.cover):
        coverUrl = obj.cover.url[10:len(obj.cover.url)]
    else:
        coverUrl = "/static/Images/NotFound.png"
    context = {
        "obj": obj,
        "cover": coverUrl
    }
    return render(request, "detail_game.html", context)


def detail_engine_view(request, id):
    obj = get_object_or_404(Engine, id=id)
    return render(request, "detail_eng.html", {"obj": obj})


def detail_publisher_view(request, id):
    obj = get_object_or_404(Engine, id=id)
    return render(request, "detail_pub.html", {"obj": obj})


def detail_publisher_view(request, id):
    obj = get_object_or_404(Publisher, id=id)
    context = {"obj": obj}
    return render(request, "detail_pub.html", context)


def detail_developer_view(request, id):
    obj = get_object_or_404(Developer, id=id)
    context = {"obj": obj}
    return render(request, "detail_dev.html", context)


def detail_plattform_view(request, id):
    obj = get_object_or_404(Plattform, id=id)
    return render(request, "detail_platt.html", {"obj": obj})


def search_view(request, option, searchStr):
    corrSearch = searchStr#[8:len(searchStr)]
    if option == "Game":
        filter = Game.objects.filter(name__contains= corrSearch).order_by('name')

    elif option == "Engine":
        filter = Engine.objects.filter(name__contains= corrSearch).order_by('name')

    elif option == "Publisher":
        filter = Publisher.objects.filter(name__contains= corrSearch).order_by('name')

    elif option == "Developer":
        filter = Developer.objects.filter(name__contains= corrSearch).order_by('name')

    elif option == "Plattform":
        filter = Plattform.objects.filter(name__contains= corrSearch).order_by('name')

    elif option == "AllGames":
        filter = Game.objects.order_by('name')
        option = "game"

    if filter:
        obj = filter.all()
    else:
        obj = ""


    context = {
        'searchStr': corrSearch,
        'obj': obj,
        'url': option.lower()
    }
    return render(request, 'search.html', context)

#Engine, Publisher, Developer, Plattform

def similar_view(request, option, id):

    if option == "Engine":
        filter = Game.objects.filter(engine__exact= id).order_by('name')
    elif option == "Publisher":
        filter = Game.objects.filter(publisher__exact= id)
    elif option == "Developer":
        filter = Game.objects.filter(developer__exact= id)
    elif option == "Plattform":
        filter = Game.objects.filter(plattform__exact= id)
    elif option == "Genre":
        filter = Game.objects.filter(genre__exact= id)

    if filter:
        obj = filter.all()
    else:
        obj = ""

    context = {
        "obj": obj
    }

    return render(request, 'similar.html', context)

def impressum_view(request):
    return render(request, 'impressum.html', {})
