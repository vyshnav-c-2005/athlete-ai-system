from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WorkoutLog
from .forms import WorkoutForm

@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('list_workouts')
    else:
        form = WorkoutForm()

    return render(request, 'workouts/add_workout.html', {'form': form})


@login_required
def list_workouts(request):
    logs = WorkoutLog.objects.filter(user=request.user).order_by('-date')
    return render(request, 'workouts/list_workouts.html', {'logs': logs})
