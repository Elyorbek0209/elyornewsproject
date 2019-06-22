from django.shortcuts import render


import datetime



# Create your views here.

def test_news_view(request):

    dt = datetime.datetime.now()

    my_dict = {'date': dt}

    return render(request, 'testapp/home.html', my_dict)



def home_page_view(request):

    return render(request, 'testapp/home.html')


def sport_news_view(request):

    news1 = 'Womens WorldCup is not Interesting'

    news2 = 'Champions League was boring this year'

    news3 = 'Euro 2020 preparation going on'

    news4 = 'Cristiano Ronaldo made huge charity for kids'

    news5 = 'Juventus is a great team in the world'

    my_dict = {'news1': news1, 'news2': news2, 'news3': news3, 'news4': news4, 'news5': news5}


    return render(request, 'testapp/sportnews.html', my_dict)


def music_news_view(request):

    news1 = 'Shohjakhon Juraev has new amazing songs'

    news2 = 'Uzbek singers can not sing'

    news3 = 'Classic music are popular in Tashkent'

    news4 = 'Xurshid Rasulov has an unique talent'

    news5 = 'Uzbekistan has amazing music history'

    my_dict = {'news1': news1, 'news2': news2, 'news3': news3, 'news4': news4, 'news5': news5}


    return render(request, 'testapp/music.html', my_dict)



def media_news_view(request):

    news1 = 'Shohjakhon Juraev has new amazing songs'

    news2 = 'Uzbek singers can not sing'

    news3 = 'Classic music are popular in Tashkent'

    news4 = 'Xurshid Rasulov has an unique talent'

    news5 = 'Uzbekistan has amazing music history'

    my_dict = {'news1': news1, 'news2': news2, 'news3': news3, 'news4': news4, 'news5': news5}


    return render(request, 'testapp/media.html', my_dict)



