"""GameDatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from pages.views import home_view, detail_game_view, search_view, detail_engine_view, detail_publisher_view, detail_developer_view, detail_plattform_view, impressum_view, similar_view
#from Games.views import

urlpatterns = [
    path('', home_view),
    path('game/<int:id>/', detail_game_view, name="detailGame"),
    path('engine/<int:id>/', detail_engine_view, name="detailEng"),
    path('publisher/<int:id>/', detail_publisher_view, name="detailPub"),
    path('developer/<int:id>/', detail_developer_view, name="detailDev"),
    path('plattform/<int:id>/', detail_plattform_view, name="detailPlatt"),

    #path('search/<str:searchStr>', search_view, name="search"),
    path('search/<str:option>/<str:searchStr>', search_view, name="search"),
    path('similar/<str:option>/<int:id>', similar_view, name="similar"),

    path("impressum", impressum_view, name="impressum"),
    path('admin/', admin.site.urls),
]
