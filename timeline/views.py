from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from normaluser.models import NormalUser, Board


@login_required
def show_timeline(request):
    return render(request, 'timeline.html', {'currUser': request.user})


@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def show_profile(request):
    currUser = get_object_or_404(NormalUser, user=request.user)
    return render(request, 'profile.html', {'currUser': currUser, 'user': currUser})

@login_required
def show_board(request, board_id):
    currUser = get_object_or_404(NormalUser, user=request.user)
    return render(request, 'board.html', {'board': Board.objects.get(id=board_id), 'currUser': currUser})