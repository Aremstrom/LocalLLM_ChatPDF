from django.shortcuts import render, redirect
from .models import UploadedFile
import base64


def upload_file(request):
    if request.method == 'POST':
        uploaded_file = UploadedFile(file=request.FILES['file'])
        uploaded_file.save()
        # Redirect to preview view
        return redirect('preview', pk=uploaded_file.pk)
    else:
        return render(request, 'upload_form.html')


def display_preview(request, pk):
    try:
        file = UploadedFile.objects.get(pk=pk)
        pdf_contents = file.file.read()
        encoded_pdf = base64.b64encode(pdf_contents).decode('utf-8')
        # file_path = r'D:\Code\Research\CDE\Django\UI\media\uploads\9th_I2CT_2024_SCHEDULE_-_PHYSICAL_MODE.pdf'
        # encoded_pdf = base64.b64encode(file_path).decode('utf-8')
        # file_path = encoded_pdf
        return render(request, 'preview.html', {'file': file, 'encoded_pdf': encoded_pdf})
    except UploadedFile.DoesNotExist:
        return render(request, 'error.html', {'message': 'File not found'})
