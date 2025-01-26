from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from main_app.models import Score
from django.contrib.auth.views import LoginView

class Home(LoginView):
    template_name = 'home.html'

def score_index(request):
    score_list = Score.objects.all()
    return render(request, 'scores/index.html', {'scores': score_list})

def score_detail(request, score_id):
    print(score_id, "this is the ScoreID")
    score = Score.objects.get(id=score_id)
    print(score, "this is the object")
    return render(request, 'scores/detail.html', {'score':score})
# Create your views here.

# class ScoreList(ListView):
#     model = Score
#     template_name = 'scores/index.html'

class ScoreCreate(CreateView):
    model = Score
    fields = '__all__'
    
    
class ScoreUpdate(UpdateView):
    model = Score
    fields = ['genre','book','page']

class ScoreDelete(DeleteView):
    model = Score
    success_url = '/scores/'
