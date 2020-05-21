from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from django.http import Http404
from .models import Board, User, Topic, Post
from .forms import NewTopicForm

# Create your views here.
def home(request):
    # return HttpResponse('Hello, World!')
    # boards = Board.objects.all()
    # boards_names = list()

    # for board in boards:
    #     boards_names.append(board.name)

    # response_html =  '<br>'.join(boards_names)
    # return HttpResponse(response_html)

    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    # option 1
    # board = Board.objects.get(pk=pk)
    # return render(request, 'topics.html', {'board': board})

    # option 2
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    # return render(request, 'topics.html', {'board': board})

    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()

    if request.method == 'POST':
        # option 1: before using NewTopicForm
        # subject = request.POST['subject']
        # message = request.POST['message']

        # # TODO: get the currently logged in user
        # user = User.objects.first()

        # topic = Topic.objects.create(
        #     subject=subject,
        #     board=board,
        #     starter=user
        # )

        # post = Post.objects.create(
        #     message=message,
        #     topic=topic,
        #     created_by=user
        # )

        # # TODO: redirected to the created topic page
        # return redirect('board_topics', pk=board.pk)

        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()

            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                created_by = user
            )

            return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})

