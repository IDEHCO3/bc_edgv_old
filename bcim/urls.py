
from django.conf.urls import include, patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from bcim import views


urlpatterns = format_suffix_patterns([
    url(r'^$', views.APIRoot.as_view(), name='api_root'),

    #Detail estados
    url(r'^estados/(?P<geocodigo>[0-9]{2})/$', views.UnidadeFederacaoDetail.as_view(), name='uf_detail_geocodigo'),
    url(r'^estados/(?P<id_objeto>[0-9]*)/$', views.UnidadeFederacaoDetail.as_view(), name='uf_detail_id_objeto'),
    url(r'^estados/(?P<sigla>[A-Za-z]{2})/$', views.UnidadeFederacaoDetail.as_view(), name='uf_detail_sigla'),
    url(r'^estados/(?P<sigla>[A-Za-z]{2})/(?P<attributes_functions>.*)/$', views.UnidadeFederacaoDetail.as_view(), name='uf_detail_si'),


    #Collection estados
    url(r'^estados/$', views.UnidadeFederacaoListFilteredByQueryParameters.as_view(), name='uf_list'),
    # url(r'^estados/(?P<siglas>\w+(\s*,\s*\w+)*)/$', views.UnidadeFederacaoFiltered.as_view(), name='uf_list_sigla_filtered'),
    # url(r'^estados/(?P<spatial_function>[A-Za-z]+)/(?P<geom>.*)/$', views.UnidadeFederacaoFiltered.as_view(), name='aldeia_uf_spatial_filtered'),

    url(r'^aldeias-indigenas/(?P<id_objeto>[0-9]+)/$', views.AldeiaIndigenaDetail.as_view(), name='uf_detail_aldeia'),
    url(r'^aldeias-indigenas/(?P<id_objeto>[0-9]+)/(?P<attributes_functions>.*)/$', views.AldeiaIndigenaDetail.as_view(), name='uf_detail_si'),
    #url(r'^aldeias-indigenas/(?P<id_objeto>[0-9]+)/(?P<spatial_function_1>[A-Za-z]+)/(?P<param_1>.+)/$', views.AldeiaIndigenaDetail.as_view(), name='aldeia_detail_with_param_sf'),
    #collection
    url(r'^aldeias-indigenas/$', views.AldeiaIndigenaListFilteredByQueryParameters.as_view(), name='aldeia_indigena_list'),
    url(r'^aldeias-indigenas/(?P<spatial_function>[A-Za-z]+)/(?P<geom>.*)/$', views.AldeiaIndigenaListFiltered.as_view(), name='aldeia_indigena_list_filtered'),


    url(r'^municipios/$', views.MunicipioList.as_view(), name='municipio_list'),
    url(r'^municipios/(?P<nome>[A-Za-z]+)/$', views.MunicipioFiltered.as_view(), name='municipio_list_filtered'),
    url(r'^outras-unidades-protegidas/$', views.OutrasUnidProtegidasList.as_view(), name='outras_unid_protegidas_list'),
    url(r'^outros-limites-oficiais/$', views.OutrosLimitesOficiaisList.as_view(), name='outros_limites_oficiais_list'),
    url(r'^paises/$', views.PaisList.as_view(), name='pais_list'),
    url(r'^terras-indigenas/$', views.TerraIndigenaList.as_view(), name='terra_indigena_list'),
    url(r'^unidades-de-conservacao-nao-snuc/$', views.UnidadeConservacaoNaoSnucList.as_view(), name='unidade_conservacao_nao_snuc_list'),
    url(r'^unidades-de-protecao-integral/$', views.UnidadeProtecaoIntegralList.as_view(), name='unidade_protecao_integral_list'),
    url(r'^unidades-de-uso-sustentavel/$', views.UnidadeUsoSustentavelList.as_view(), name='unidade_uso_sustentavel_list'),
    url(r'^aglomerados-rurais-de-extensao-urbana/$', views.AglomeradoRuralDeExtensaoUrbanaList.as_view(), name='aglomerado_rural_de_extensao_urbana_list'),
    url(r'^aglomerados-rurais-isolado/$', views.AglomeradoRuralIsoladoList.as_view(), name='aglomerado_rural_isolado_list'),

    url(r'^areas-edificadas/$', views.AreaEdificadaList.as_view(), name='area_edificada_list'),
    url(r'^capitais/$', views.CapitalList.as_view(), name='capital_list'),
    url(r'^vilas/$', views.VilaList.as_view(), name='vila_list'),
    url(r'^curvas-batimetricas/$', views.CurvaBatimetricaList.as_view(), name='curva_batimetrica_list'),
    #url(r'^curvas-de-nivel/$', views.CurvaNivelList.as_view(), name='curva_nivel_list'), # nao carrega (muita informacao)
    url(r'^dunas/$', views.DunaList.as_view(), name='duna_list'),
    url(r'^elementos-fisiografico-natural/$', views.ElementoFisiograficoNaturalList.as_view(), name='elemento_fisiografico_natural_list'),
    url(r'^picos/$', views.PicoList.as_view(), name='pico_list'),
    url(r'^pontos-cotados-altimetricos/$', views.PontoCotadoAltimetricoList.as_view(), name='ponto_cotado_altimetrico_list'),
    url(r'^pontos-cotados-batimetricos/$', views.PontoCotadoBatimetricoList.as_view(), name='ponto_cotado_batimetrico_list'),
    url(r'^eclusas/$', views.EclusaList.as_view(), name='eclusa_list'),
    url(r'^edificacoes-de-construcao-portuaria/$', views.EdifConstPortuariaList.as_view(), name='edif_const_portuaria_list'),
    url(r'^edificacoes-de-construcao-aeroportuaria/$', views.EdifConstrAeroportuariaList.as_view(), name='edif_const_aeroportuaria_list'),
    url(r'^edificacoes-metro-ferroviaria/$', views.EdifMetroFerroviariaList.as_view(), name='edif_metro_ferroviaria_list'),
    url(r'^fundeadouros/$', views.FundeadouroList.as_view(), name='fundeadouro_list'),
    url(r'^pistas-de-ponto-pouso/$', views.PistaPontoPousoList.as_view(), name='pista_ponto_pouso_list'),
    url(r'^pontes/$', views.PonteList.as_view(), name='ponte_list'),
    url(r'^sinalizacaoes$', views.SinalizacaoList.as_view(), name='sinalizacao_list'),
    url(r'^travessias/$', views.TravessiaList.as_view(), name='travessia_list'),
    url(r'^trechos-dutos/$', views.TrechoDutoList.as_view(), name='trecho_duto_list'),
    #Trecho_ferroviario
    url(r'^trechos-ferroviarios/$', views.TrechoFerroviarioList.as_view(), name='trecho_ferroviario_list'),
    url(r'^trechos-ferroviarios/(?P<id_objeto>[0-9]*)/$', views.TrechoFerroviarioDetail.as_view(), name='tf_detail_id_objeto'),
    url(r'^trechos-ferroviarios/(?P<id_objeto>[0-9]*)/(?P<spatial_function_1>[A-Za-z]+)/$', views.TrechoFerroviarioDetail.as_view(), name='tf_detail_si'),
    url(r'^trechos-ferroviarios/(?P<id_objeto>[0-9]*)/(?P<spatial_function_1>[A-Za-z]+)/(?P<param_1>.+)/$', views.TrechoFerroviarioDetail.as_view(), name='tf_detail_si_par'),

    url(r'^trechos-hidroviarios/$', views.TrechoHidroviarioList.as_view(), name='trecho_hidroviario_list'),
    #url(r'^trechos-rodoviarios/$', views.TrechoRodoviarioList.as_view(), name='trecho_rodoviario_list'),
    url(r'^tuneis/$', views.TunelList.as_view(), name='tunel_list'),
    url(r'^brejos-e-pantanos/$', views.BrejoPantanoList.as_view(), name='brejo_pantano_list'),
    url(r'^mangues/$', views.MangueList.as_view(), name='mangue_list'),
    url(r'^vegetacoes-de-restinga/$', views.VegRestingaList.as_view(), name='veg_restinga_list'),
    url(r'^edificacoes-publica-militar/$', views.EdifPubMilitarList.as_view(), name='edif_pub_militar_list'),
    url(r'^postos-fiscais/$', views.PostoFiscalList.as_view(), name='posto_fiscal_list'),
    url(r'^edificacoes-agropecuarias-de-extracao-vegetal-e-pesca/$', views.EdifAgropecExtVegetalPescaList.as_view(), name='edif_agropec_ext_vegetal_pesca_list'),
    url(r'^edificacoes-industrial/$', views.EdifIndustrialList.as_view(), name='edif_industrial_list'),
    url(r'^extracoes-minerais/$', views.ExtMineralList.as_view(), name='ext_mineral_list'),
    url(r'^edificacoes-religiosa/$', views.EdifReligiosaList.as_view(), name='edif_religiosa_list'),
    url(r'^estacoes-geradoras-de-energia-eletrica/$', views.EstGeradEnergiaEletricaList.as_view(), name='est_gerad_energia_eletrica_list'),
    url(r'^hidreletricas/$', views.HidreletricaList.as_view(), name='hidreletrica_list'),
    url(r'^termeletricas/$', views.TermeletricaList.as_view(), name='termeletrica_list'),
    url(r'^torres-de-energia/$', views.TorreEnergiaList.as_view(), name='torre_energia_list'),
    url(r'^bancos-de-areia/$', views.BancoAreiaList.as_view(), name='banco_areia_list'),
    url(r'^barragens/$', views.BarragemList.as_view(), name='barragem_list'),
    url(r'^corredeiras/$', views.CorredeiraList.as_view(), name='corredeira_list'),
    url(r'^fozes-maritima/$', views.FozMaritimaList.as_view(), name='foz_maritima_list'),
    url(r'^ilhas/$', views.IlhaList.as_view(), name='ilha_list'),
    url(r'^massas-dagua/$', views.MassaDaguaList.as_view(), name='massa_dagua_list'),
    url(r'^quedas-dagua/$', views.QuedaDaguaList.as_view(), name='queda_dagua_list'),
    url(r'^recifes/$', views.RecifeList.as_view(), name='recife_list'),
    url(r'^rochas-em-agua/$', views.RochaEmAguaList.as_view(), name='rocha_em_agua_list'),
    url(r'^sumidouros-vertedouros/$', views.SumidouroVertedouroList.as_view(), name='sumidouro_vertedouro_list'),
    url(r'^terrenos-sujeito-a-inundacao/$', views.TerrenoSujeitoInundacaoList.as_view(), name='terreno_sujeito_inundacao_list'),
    url(r'^trechos-de-drenagem/$', views.TrechoDrenagemList.as_view(), name='trecho_drenagem_list'),
    url(r'^trechos-de-massa-dagua/$', views.TrechoMassaDaguaList.as_view(), name='trecho_massa_dagua_list'),
    url(r'^areas-de-desenvolvimento-de-controle/$', views.AreaDesenvolvimentoControleList.as_view(), name='area_desenvolvimento_controle_list'),
    url(r'^marcos-de-limite/$', views.MarcoDeLimiteList.as_view(), name='marco_de_limite_list'),
    url(r'^pontos-geodesicos/$', views.PontoExibicaoWgs84List.as_view(), name='ponto_exibicao_wgs84_list'),


])

 #Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
