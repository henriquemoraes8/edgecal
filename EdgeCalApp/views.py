from django.views import generic
from codetools.util.cbook import Null

class IndexView(generic.ListView):
    template_name = 'EdgeCalApp/index.html'
    context_object_name = 'index_page'
    
    def get_queryset(self):
        return Null