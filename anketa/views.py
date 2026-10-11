from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

#CRUD

#CREATE
def create_anketa_view(request):
    if request.method == 'POST':
        form_anketa = forms.AnketaForm(request.POST,request.FILES)
        if form_anketa.is_valid():
            form_anketa.save()
            return redirect('/anketa_list/')
    else:
        form_anketa = forms.AnketaForm()
    return render(request, 'create_anketa.html', {'form_anketa': form_anketa})


#READ
def read_anketa_view(request):
    if request.method == 'GET':
        anketa_list = models.Anketa.objects.all().order_by('-id')
    return render(request, 'anketa_list.html', {'anketa_list': anketa_list})

#UPDATE
def update_anketa_view(request):
    anketa_id = get_object_or_404(models.Anketa, id=id)
    if request.method == 'POST':
        form_anketa = forms.AnketaForm(request.POST, instance=anketa_id)
        if form_anketa.is_valid():
            form_anketa.save()
            return redirect('/anketa_list/')
    else:
        form_anketa = forms.AnketaForm(instance=anketa_id)
    return render(request, 'update_anketa.html', {'form': form_anketa})



# DELETE
def delete_anketa_view(request, id):
    anketa_id =get_object_or_404(models.Anketa, id=id)
    anketa_id.delete()
    return redirect('/anketa_list/')


  



