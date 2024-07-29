from django.shortcuts import render,redirect
from .forms import ImageUploadForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('https:www.google.co.in')  # Replace 'success_url' with your desired redirect URL
    else:
        form = ImageUploadForm()
    return render(request, 'app2/index.html', {'form': form})