from django.shortcuts import render, redirect
from .forms import ImageForm
from IMGUpLoader.models import Image

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'IMGUpLoader/upload.html', {'form': form})

def success(request):
    images = Image.objects.all().order_by('-pk')
    return render(request, 'IMGUpLoader/success.html', {'images': images})



