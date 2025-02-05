from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from main_app.models import Score
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginView):
    template_name = 'home.html'

@login_required
def score_index(request):
    score_list = Score.objects.filter(author=request.user)
    return render(request, 'scores/index.html', {'scores': score_list})

@login_required
def score_detail(request, score_id):
    print(score_id, "this is the ScoreID")
    score = Score.objects.get(id=score_id)
    print(score, "this is the object")
    return render(request, 'scores/detail.html', {'score':score})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('score-index')
        else:
            error_message = 'Invalid signup - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


# Create your views here.

# class ScoreList(ListView):
#     model = Score
#     template_name = 'scores/index.html'

class ScoreCreate(LoginRequiredMixin, CreateView):
    model = Score
    fields = '__all__'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class ScoreUpdate(LoginRequiredMixin, UpdateView):
    model = Score
    fields = ['genre','book','page']

class ScoreDelete(LoginRequiredMixin, DeleteView):
    model = Score
    success_url = '/scores/'
