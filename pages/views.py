from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

# Create your views here.
#from django.shortcuts import render # here by default
#from django.http import HttpResponse # new
from django.views.generic import TemplateView

# Create your views here.
#def homePageView(request): # new
 #   return HttpResponse('Hello World!') # new

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Your Name",
        })

        return context
    

class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price": "200000"},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": "100000"},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": "5000000"},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": "3000"}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] =  "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        view_data = {}
        try:
            product = Product.products[int(id) - 1]
            view_data["title"] = product["name"] + " - Online Store"
            view_data["subtitle"] = product["name"] + " - Product information"
            view_data["product"] = product
        except IndexError:
            # Si el producto no se encuentra, redirecciona a la documentación de Django
            return redirect('https://docs.djangoproject.com/en/stable/')

        return render(request, self.template_name, view_data)





