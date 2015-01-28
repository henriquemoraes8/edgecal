from django.views import generic
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader, Context

class IndexView(generic.View):
    template_name = 'EdgeCalApp/index.html'
    context_object_name = 'index_page'
    
    def get(self, request):
        return HttpResponse('Welcome to the home page!')
    
def error404(request):
    
    template = loader.get_template('EdgeCalApp/404.html')
    context = Context({
        'message': 'All: %s' % request,
        })
    
    return HttpResponse(content=template.render(context), content_type='text/html; charset=utf-8', status=404)