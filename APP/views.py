from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import weasyprint
from io import BytesIO

from .models import Letter

# Create your views here.
def letter_PDF(request, Letter_id):
    letter = get_object_or_404(Letter, id=Letter_id)
    html = render_to_string('APP/pdf.html',
                            {'letter': letter})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\"letter_{}.pdf"'.format(letter.id)                            
    weasyprint.HTML(string=html).write_pdf(response)
    return response

    
