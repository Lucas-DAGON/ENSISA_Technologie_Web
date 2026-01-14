from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from .models import Question
from django.template import loader

def welcome(request):
    latest_question_list = Question.objects.order_by('-publication_date')[:3]
    template = loader.get_template ('polls/index.html')
    context = {'latest_question_list': latest_question_list ,}
    return HttpResponse(template.render(context, request))

def test_filter(request):
    template = Template('Bonjour {{name | capfirst}} !')
    name = 'lucas'
    context = Context ({'name': name })
    return HttpResponse(template.render(context))

def test_list(request):
    template = Template ('<ul>{% for person in persons %} <li>{{person}}</li>{% endfor %} </ul>')
    persons = ['Maxime', 'Malika', 'Nour']
    context = Context ({'persons' : persons})
    return HttpResponse(template.render(context))

def test_cond_list(request):
    template = Template ('{% if persons %} <ul>{% for person in persons %} <li>{{person}}</li> {% endfor %} </ul> {% else %} La liste est vide. {% endif %}')
    persons = []
    context = Context ({'persons' : persons})
    return HttpResponse(template.render(context))

def detail (request, question_id):
    return HttpResponse("Voici la question %s." % question_id)

def results (request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render (request, 'polls/results.html', {'question':question})

def vote (request, question_id):
    question = get_object_or_404 (Question, pk = question_id)
    try :
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist ):
        # Redisplay the question voting form .
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice." ,
    })
    else :
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))