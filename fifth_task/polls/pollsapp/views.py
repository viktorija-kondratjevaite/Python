from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, OpenQuestion
from django.template import loader
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
import matplotlib.pyplot as plt
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
import datetime
import random
import django

class IndexView(generic.ListView):
    template_name = 'pollsapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'pollsapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'pollsapp/results.html'
    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if question.is_open:
      written_answer = OpenQuestion()
      written_answer.answer_text = request.POST['openQuestion']
      written_answer.question = question
      written_answer.save()   
      return HttpResponseRedirect(reverse('pollsapp:results', args=(question.id,)))
    else:
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'pollsapp/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('pollsapp:results', args=(question.id,)))

def chart(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    fig=Figure()
    canvas = FigureCanvas(fig)
    x=[]
    y=[]
    choices=[]
    k = 0
    for choice in question.choice_set.all():
        y.append(int(choice.votes))
        x.append(k)
        choices.append(choice.choice_text)
        k= k+1
        print (choice.votes)
        print (choice.choice_text)
    plt.clf()
    plt.bar(x, y, align='center')
    plt.ylabel('Votes')
    plt.xlabel('Choices')
    plt.xticks(x, choices)
    plt.title('Bar chart')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    response=HttpResponse(buf.getvalue(), content_type='image/png')
    return response
	