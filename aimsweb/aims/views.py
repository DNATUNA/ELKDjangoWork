from django.contrib import messages
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView

# 향후 인증도 추가 필요
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import LogInfo
from aims.es.search import Getdata

class IndexView(ListView):
    template_name = 'aims/list_systems.html'
    context_object_name = 'latest_systems_list'

    def get_queryset(self):
        return LogInfo.objects.all().order_by('-pk')  # 내림차순으로 pk 높은거부터 정렬
        # return RheedInfo.objects.all()


class DetailInferenceView(DetailView):
    model = LogInfo
    template_name = 'aims/log_detail_inference.html'

    # def get_queryset(self):
    #     return RheedInfo.objects.get()  # 내림차순으로 pk 높은거부터 정렬

class DetailDetailsView(DetailView):
    model = LogInfo
    template_name = 'aims/log_detail_details.html'

      # def get_queryset(self):
     #     return RheedInfo.objects.get()  # 내림차순으로 pk 높은거부터 정렬



def search(request):

    template_name = 'aims/search.html'

    q = request.GET.get('q')

    if q:
        Getdata.search = Getdata.search[0:Getdata.total]
        s = Getdata.search.query("match", message=q)
        s = s.sort('Day')
        res = s.execute()
    else:
        Getdata.search = Getdata.search[0:10]
        s = Getdata.search.query("match_all")
        s = s.sort('Day')
        res = s.execute()

    return render(request, 'aims/search.html', {'q': q, 's': s, 'res': res})