from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Choice

def home(request):
    polls = Poll.objects.all()
    return render(request, 'polls/home.html', {'polls': polls})

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/poll_detail.html', {'poll': poll})

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/poll_detail.html', {
            'poll': poll,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', poll_id=poll.id)

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    sum=0
    for choice in poll.choice_set.all():
        sum+=choice.votes
    return render(request, 'polls/results.html', {'poll': poll, 'total_responses': sum})

def add_poll(request):
    if request.method == 'POST':
        question = request.POST['question']
        choices = request.POST.getlist('choice')
        if question and choices:
            poll = Poll.objects.create(question=question)
            for choice in choices:
                if choice:
                    Choice.objects.create(poll=poll, choice_text=choice)
            return redirect('polls:home')
    return render(request, 'polls/add_poll.html')

def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    poll.delete()
    return redirect('polls:home')

def reset_poll(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    for choice in poll.choice_set.all():
        choice.votes=0
        choice.save()
    return redirect('polls:home')

