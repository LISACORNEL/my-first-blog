from django.shortcuts import render
def problem_list(request):
    return render(request, 'problem/problem_list.html', {})

# Create your views here.
