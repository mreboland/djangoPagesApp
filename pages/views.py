from django.views.generic import TemplateView


# Capitalizing our view HomePageView, tells python it's a class. The TemplateView contains all the logic needed to display our template, we just need to specifythe template's name.
class HomePageView(TemplateView):
    template_name = "home.html"
    
class AboutPageView(TemplateView):
    template_name = "about.html"