from django.views.generic.base import TemplateView


class MapIndexView(TemplateView):
    template_name = 'map/index.html'
