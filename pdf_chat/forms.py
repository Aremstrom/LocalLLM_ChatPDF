from django import forms


class PDFForm(forms.Form):
    pdf_file = forms.FileField(
        label='Select a PDF file', help_text='max. 10 MB', required=True)
