from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, TemplateView
from cities.models import City, City_Detail
from cities.forms import City_Detail_Form


class CitiesDetailView(DetailView):
    template_name = 'cities/city-detail.html'
    model = City


class CitiesListView(ListView):
    context_object_name = 'cities'
    model = City
    template_name = 'cities/city-search.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        result = City.objects.filter(Q(name=query))
        return result

class IndexView(TemplateView):
    template_name = 'cities/city-search.html'

class CreateCityDetail(CreateView):
    template_name = 'cities/city-detail.html'
    model = City_Detail
    fields = ['city', 'city_detail', 'geometry']


def add_detail(request,pk):
    city =  get_object_or_404(City,pk=pk)
    if request.method == 'POST':
        form = City_Detail_Form(request.POST)
        if form.is_valid():
            city_detail = form.save(commit=False)
            city_detail.city = city
            city_detail.save()
            return redirect('cities:create-detail-view',pk=city.pk)
    else:
        form = City_Detail_Form()
    return render(request,'cities/city-detail.html',{'form':form})
