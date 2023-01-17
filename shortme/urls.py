from django.contrib import admin
from django.urls import path

from shortme.views import HomeFormView, RedirectView, ResultView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeFormView.as_view(), name="home"),
    path("result/", ResultView.as_view(), name="result"),
    path("<str:hash>/", RedirectView.as_view(), name="redirect"),
]
