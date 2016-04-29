from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'bc_edgv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^idehco3/bcedgv/ibge/bcim/', include('bcim.urls', namespace='bcim_v1')),


]
urlpatterns += [
    url(r'^idehco3/bcedgv/api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]