from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"


class HelpView(TemplateView):
    template_name = "help.html"
