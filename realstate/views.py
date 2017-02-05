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
        # pr_location = request.GET.get('location', 'any')
        # pr_type = request.GET.get('type', 'any')
        # pr_status = request.GET.get('status', 'any')
        # pr_bedrooms = request.GET.get('bedrooms', 'any')
        # pr_bathrooms = request.GET.get('bathrooms', 'any')
        # pr_min_price = request.GET.get('min-price', 'any')
        # pr_max_price = request.GET.get('max-price', 'any')
        # pr_keyword = request.GET.get('keyword')
        #
        # location = Departamento.objects.filter(nombre__contains=pr_location)
        #
        # if location and not type=='any' and not pr_status=='any' and not pr_bedrooms=='any' and not pr_bathrooms=='any' and not pr_min_price=='any' and not pr_max_price=='any' and pr_keyword:
        #     propiedades_list = Propiedad.objects.filter(localidad__municipio__departamento=location,
        #                                                 estado_negocio=pr_status,
        #                                                 habitaciones=pr_bedrooms,
        #                                                 banios=pr_bathrooms,
        #                                                 valor_gte=pr_min_price,
        #                                                 valor__lte=pr_max_price,
        #                                                 nombre__contains=pr_keyword)
        # elif location and not type=='any' and not pr_status=='any' and not pr_bedrooms=='any' and not pr_bathrooms=='any' and not pr_min_price=='any' and not pr_max_price=='any':
        #     propiedades_list = Propiedad.objects.filter(localidad__municipio__departamento=location,
        #                                                 estado_negocio=pr_status,
        #                                                 habitaciones=pr_bedrooms,
        #                                                 banios=pr_bathrooms,
        #                                                 valor_gte=pr_min_price,
        #                                                 valor__lte=pr_max_price,)
        # elif location and not type == 'any' and not pr_status == 'any' and not pr_bedrooms == 'any' and not pr_bathrooms == 'any' and not pr_min_price == 'any':
        #     propiedades_list = Propiedad.objects.filter(localidad__municipio__departamento=location,
        #                                                 estado_negocio=pr_status,
        #                                                 habitaciones=pr_bedrooms,
        #                                                 banios=pr_bathrooms,
        #                                                 valor_gte=pr_min_price,)
        # elif location and not type == 'any' and not pr_status == 'any' and not pr_bedrooms == 'any' and not pr_bathrooms == 'any':
        #     propiedades_list = Propiedad.objects.filter(localidad__municipio__departamento=location,
        #                                                 estado_negocio=pr_status,
        #                                                 habitaciones=pr_bedrooms,
        #                                                 banios=pr_bathrooms,)
        # elif location and not type == 'any' and not pr_status == 'any' and not pr_bedrooms == 'any':
        #     propiedades_list = Propiedad.objects.filter(localidad__municipio__departamento=location,
        #                                                 estado_negocio=pr_status,
        #                                                 habitaciones=pr_bedrooms,)
        # elif location and not type == 'any' and not pr_status == 'any':
        #     propiedades_list = Propiedad.objects.filter(localidad__municipio__departamento=location,
        #                                                 estado_negocio=pr_status,)
        # elif location and not type == 'any' and not pr_status == 'any':
        #     propiedades_list = Propiedad.objects.filter(localidad__municipio__departamento=location,)

        propiedades_list = Propiedad.objects.all()

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
