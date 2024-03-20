from django.http import Http404
from django.shortcuts import render

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море\n
                страшным штормом, потерпел крушение.\n
                Весь экипаж, кроме меня, утонул; я же,\n
                несчастный Робинзон Крузо, был выброшен\n
                полумёртвым на берег этого проклятого острова,\n
                который назвал островом Отчаяния.'''
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло\n
                с мели приливом и пригнало гораздо ближе к берегу.\n
                Это подало мне надежду, что, когда ветер стихнет,\n
                мне удастся добраться до корабля и запастись едой и\n
                другими необходимыми вещами. Я немного приободрился,\n
                хотя печаль о погибших товарищах не покидала меня.\n
                Мне всё думалось, что, останься мы на корабле, мы\n
                непременно спаслись бы. Теперь из его обломков мы могли бы\n
                построить баркас, на котором и выбрались бы из этого\n
                гиблого места.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный\n
                порывистый ветер. 25 октября.  Корабль за ночь разбило\n
                в щепки; на том месте, где он стоял, торчат какие-то\n
                жалкие обломки,  да и те видны только во время отлива.\n
                Весь этот день я хлопотал  около вещей: укрывал и\n
                укутывал их, чтобы не испортились от дождя.''',
    },
]

def lines(id):
    post = next((post_dict for post_dict in posts
                 if post_dict['id'] == id), None)
    context = {'post': post}
    for post in posts:
        plain_text = post['text'] 
        lines = plain_text.splitlines()
        for line in lines:
            print(line)
            

def index(request):
    template = 'blog/index.html'
    reversed_posts = posts[::-1]
    context = {'posts': reversed_posts}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = next((post_dict for post_dict in posts
                 if post_dict['id'] == id), None)
    if post is None:
        raise Http404
    context = {'post': post}
    for post in posts:
        lines(id)
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    for post in posts:
        post['category'] = category_slug
    context = {'post': post}
    return render(request, template, context)
