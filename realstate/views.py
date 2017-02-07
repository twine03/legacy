from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from realstate.models import *
from realstate.send_email import send


def inicio(request):
    return HttpResponseRedirect("/app")


class index(TemplateView):
    template_name = "propiedades.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()

        page = request.GET.get('page', 1)

        propiedades_list = Propiedad.objects.all()

        for k,vals in request.GET.lists():
            for v in vals:
                if not k == 'page':
                    propiedades_list = propiedades_list.filter(**{k: v})

        paginator = Paginator(propiedades_list, 3)
        try:
            propiedades = paginator.page(page)
        except PageNotAnInteger:
            propiedades = paginator.page(1)
        except EmptyPage:
            propiedades = paginator.page(paginator.num_pages)

        context['propiedades'] = propiedades
        return super(index, self).render_to_response(context)


class show_propiedad(TemplateView):
    template_name = "propiedad.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()

        propiedad = Propiedad.objects.get(id=request.GET.get('id'))
        context['propiedad'] = propiedad
        return super(show_propiedad, self).render_to_response(context)

class enviar_mail(TemplateView):
    def post(self, request, *args, **kwargs):
        subject = '%s Informacion de casa %s' % (request.POST.get('name', ''), request.POST.get('property_title', ''))

        message = '%s Nombre: %s Telefono Contacto: %s Email: %s' % (request.POST.get('message', ''),
                                                                     request.POST.get('name', ''),
                                                                     request.POST.get('from_email', ''),
                                                                     request.POST.get('contact-number', ''))
        from_email = request.POST.get('from_email', '')
        to_email = 'jwgarcia003@gmail.com'
        return send(request, subject, message, from_email, to_email)
