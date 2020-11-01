from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Institutions
from  .serializers  import InstitutionsSerializer, ZipcodeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
    return render(request, 'universities/index.html')


class UniversityListView(ListView):
    model = Institutions
    template_name = 'universities/universities.html'
    context_object_name = 'universities'
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(instname__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class UniversityDetailView(DetailView):
    model = Institutions


def search(request):
    return render(request, 'universities/search.html')


def about(request):
    return render(request, 'universities/about.html')


def contact(request):
    return render(request, 'universities/contact.html')


@api_view(['GET'])
def institutionsList(request):
    query = request.GET.get('query')
    institutions = Institutions.objects.filter(instname__icontains=query)[:5]
    serializer = InstitutionsSerializer(institutions, many=True)
    return Response(serializer.data)