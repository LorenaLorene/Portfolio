from django.http import HttpResponse
from django.template import loader
from intro.models import Intro
from mini_intro.models import MiniIntro
from my_portfolio.models import Portfolio
from about.models import About
from contact.models import ContactPage
from my_portfolio.models import Project


def index(request):
    # print the introduction of the first intro object introduction in the terminal when I loads page
    print(Intro.objects.all())

    template = loader.get_template('base.html')
    context = {'intro_page_name': Intro.objects.first().introduction,
               'intro_page_description': Intro.objects.first().description,
               'mini_intro_page_name': MiniIntro.objects.first().first_name,
               'mini_intro_page_job': MiniIntro.objects.first().profession,
               'left_intro_page_name': Intro.objects.first().page_name,
               'left_portfolio_page_name': Portfolio.objects.first().name,
               'left_about_me_page_name': About.objects.first().page_name,
               'portfolio_description_field': Portfolio.objects.first().description_field,
               'about_me_page_name': About.objects.first().page_name,
               'about_me_description_field': About.objects.first().description,
               'contact_page_name': ContactPage.objects.first().page_name,
               'contact_page_description_field': ContactPage.objects.first().contact_description,
               'portfolio_button': Intro.objects.first().scroll_button,
               'projects': Project.objects.all(),
               'portfolio_page_name': Portfolio.objects.first().name,
               'portfolio_show': Portfolio.objects.first().show,
               'mini_intro_image': MiniIntro.objects.first().image,
               'about_me_image': About.objects.first().image}
    return HttpResponse(template.render(context, request))