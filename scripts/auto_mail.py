from django.conf import settings
# from django.core.mail import send_mail  # I think this is right.
from django.core.mail import EmailMessage
import weasyprint
from io import BytesIO
from django.template.loader import render_to_string

from APP.models import Letter
from APP.views import letter_PDF



def run():
     for lett in Letter.objects.all():
        # Create Message
        subject = "Message de Tonton Jean-Luc {}".format(lett.id)
        message = "Votre lettre est en pièce jointe"
        email = EmailMessage(subject,
                             message,
                             'jl062705@sfr.fr',
                             [lett.email,],
                             )
        # generate pdf
        html = render_to_string('APP/pdf.html',
                                {'letter': lett})
        # enregistre pdf en mémoire                        
        out = BytesIO()
        weasyprint.HTML(string=html).write_pdf(out)

        # attach PDF file
        email.attach('letter_{}.pdf'.format(lett.numerofact),
                     out.getvalue(),
                     'application/pdf')

        # send email
        email.send()
        