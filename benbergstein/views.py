# Create your views here.
from django.template import Template, Context
from django.template.loader import get_template
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from articles.models import Article
from django.views.decorators.cache import cache_page

