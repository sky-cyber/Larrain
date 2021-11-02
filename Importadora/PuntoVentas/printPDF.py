from Importadora.wsgi import *
from django.template.loader import get_template
from weasyprint import HTML, CSS
from Importadora import settings


def printPDF():
    template = get_template("PDF/productPDF.html")
    context = {"name": "soda",
               "rut": "17.984.014-6",
               "Company": "Wykep",
               "address": "Avenida porvenir #679"}
    html_template = template.render(context)
    css_url = os.path.join(settings.BASE_DIR, 'static/admin/css/bootstrap.min.css')
    HTML(string=html_template).write_pdf(target="product.pdf", stylesheets=[CSS(css_url)])

printPDF()
