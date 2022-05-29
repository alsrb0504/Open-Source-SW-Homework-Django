from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from django.utils import timezone

from .models import Choice, Question_2


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question_2.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question_2
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question_2
    template_name = 'polls/results.html'

def QuestionView(request):
    return render( request, 'polls/question.html')

def RecieveQuestion(request):
    if request.method == 'POST':
        var = request.POST
        title = var['title']
        select_1 = var['select_1']
        select_2 = var['select_2']
        select_3 = var['select_3']
        correct = var['answer']
        
        model = Question_2(question_text=title, pub_date=timezone.now(), answer=correct)

        model.save()

        Selected_title = Question_2.objects.get(question_text=title)

        choice_model_1 = Choice(question=Selected_title, choice_text=select_1, votes=0)
        choice_model_2 = Choice(question=Selected_title, choice_text=select_2, votes=0)
        choice_model_3 = Choice(question=Selected_title, choice_text=select_3, votes=0)

        choice_model_1.save()
        choice_model_2.save()
        choice_model_3.save()

        return redirect('http://localhost:8000/polls')
        # question = models.ForeignKey(Question, on_delete=models.CASCADE)
        # choice_text = models.CharField(max_length=200)
        # votes = models.IntegerField(default=0)



def vote(request, question_id):
    question = get_object_or_404(Question_2, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

        # 질문 선택창으로
        # return HttpResponseRedirect(reverse('polls:index'))

        # 다음 질문으로, 근데 마지막 질문이면 결과창으로 이동해야 하는데 그걸 못 함.
        # return HttpResponseRedirect(reverse('polls:detail', args=(question.id + 1,)))

