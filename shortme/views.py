from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import RedirectView, TemplateView
from django.views.generic.edit import CreateView
from random_strings import random_string

from shortme.models import URLData


class HomeFormView(CreateView):
    template_name = "shortme/home.html"
    model = URLData
    fields = ["original_url"]

    def get_success_url(self):
        return reverse("result")

    def form_valid(self, form):
        hash = random_string(5)
        form.instance.hash = hash
        self.request.session["hash"] = hash
        self.request.session.save()
        return super().form_valid(form)


class ResultView(TemplateView):
    template_name = "shortme/result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hash"] = self.request.session["hash"]
        return context


class RedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url = get_object_or_404(URLData, hash=kwargs["hash"])
        url.increase_times_used()
        return url.original_url
