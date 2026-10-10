from django.shortcuts import render, redirect, get_object_or_404
from tour.models import Tour,Comment

def tour_list_view(request):
    tours = Tour.objects.all()
    return render(request, 'tour_list.html', {'tours': tours})

def tour_detail_view(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    comments = Comment.objects.filter(tour=tour)

    context = {
        'tour' : tour,
        'comments' : comments,
    }
    return render(request,'tour_detail.html', context)


                  
    
