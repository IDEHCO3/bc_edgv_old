from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
[]
from .models import UnidadeFederacao, Municipio, OutrasUnidProtegidas, OutrosLimitesOficiais, Pais, TerraIndigena, \
    UnidadeConservacaoNaoSnuc, UnidadeProtecaoIntegral, UnidadeUsoSustentavel, AglomeradoRuralDeExtensaoUrbana, \
    AglomeradoRuralIsolado, AldeiaIndigena, AreaEdificada, Capital, Cidade, Vila, CurvaBatimetrica, CurvaNivel, Duna, \
    ElementoFisiograficoNatural, Pico, PontoCotadoAltimetrico, PontoCotadoBatimetrico, Eclusa, EdifConstPortuaria, \
    EdifConstrAeroportuaria, EdifMetroFerroviaria, Fundeadouro, PistaPontoPouso, Ponte, Sinalizacao, Travessia, TrechoDuto, \
    TrechoFerroviario, TrechoHidroviario, TrechoRodoviario, Tunel, BrejoPantano, Mangue, VegRestinga, EdifPubMilitar, \
    PostoFiscal, EdifAgropecExtVegetalPesca, EdifIndustrial, ExtMineral, EdifReligiosa, EstGeradEnergiaEletrica, Hidreletrica, \
    Termeletrica, TorreEnergia, BancoAreia, Barragem, Corredeira, FozMaritima, Ilha, MassaDagua, QuedaDagua, Recife, \
    RochaEmAgua, SumidouroVertedouro, TerrenoSujeitoInundacao, TrechoDrenagem, TrechoMassaDagua, AreaDesenvolvimentoControle, \
    MarcoDeLimite, PontosExibicaoWgs84


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        fields = self.context['request'].QUERY_PARAMS.get('fields')
        if fields:
            fields = fields.split(',')
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UnidadeFederacaoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = UnidadeFederacao
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'sigla', 'geocodigo']
        identifiers = ['id_objeto', 'nome', 'nomeabrev', 'sigla', 'geocodigo']


class MunicipioSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Municipio
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev',  'geocodigo']

class OutrasUnidProtegidasSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = OutrasUnidProtegidas
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev',  'geometriaaproximada', 'sigla', 'areaoficial','administracao', 'tipooutunidprot', 'historicomodificacao']
        # 'anocriacao'

class OutrosLimitesOficiaisSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = OutrosLimitesOficiais
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'coincidecomdentrode', 'obssituacao', 'tipooutlimofic']
        # 'extensao'

class PaisSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Pais
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'sigla', 'geometriaaproximada', 'codiso3166' ]

class TerraIndigenaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TerraIndigena
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'grupoetnico', 'datasituacaojuridica', 'situacaojuridica', 'nometi', 'codigofunai']
        # 'perimetrooficial', 'areaoficialha'

class UnidadeConservacaoNaoSnucSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = UnidadeConservacaoNaoSnuc
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'sigla', 'areaoficial', 'administracao', 'classificacao', 'atolegal']
        # 'anocriacao'

class UnidadeProtecaoIntegralSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = UnidadeProtecaoIntegral
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'sigla', 'areaoficial', 'administracao', 'tipounidprotinteg', 'atolegal']
        # 'anocriacao'

class UnidadeUsoSustentavelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = UnidadeUsoSustentavel
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'sigla', 'areaoficial', 'administracao', 'tipounidusosust', 'atolegal']
        # 'anocriacao'

class AglomeradoRuralDeExtensaoUrbanaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AglomeradoRuralDeExtensaoUrbana
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada']

class AglomeradoRuralIsoladoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AglomeradoRuralIsolado
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipoaglomrurisol']

class AldeiaIndigenaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AldeiaIndigena
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'codigofunai', 'terraindigena', 'etnia']

class AreaEdificadaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AreaEdificada
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'geocodigo']

class CapitalSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Capital
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipocapital']

class CidadeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Cidade
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada']

class VilaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Vila
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada']

class CurvaBatimetricaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CurvaBatimetrica
        geo_field = 'geom'
        fields = ['id_objeto', 'profundidade']

class CurvaNivelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = CurvaNivel
        geo_field = 'geom'
        fields = ['id_objeto', 'cota', 'depressao', 'geometriaaproximada', 'indice']

class DunaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Duna
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'fixa']

class ElementoFisiograficoNaturalSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ElementoFisiograficoNatural
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipoelemnat']

class PicoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Pico
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada']

class PontoCotadoAltimetricoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PontoCotadoAltimetrico
        geo_field = 'geom'
        fields = ['id_objeto', 'geometriaaproximada', 'cota', 'cotacomprovada']

class PontoCotadoBatimetricoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PontoCotadoBatimetrico
        geo_field = 'geom'
        fields = ['id_objeto', 'profundidade']

class EclusaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Eclusa
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'desnivel', 'matconstr', 'operacional', 'situacaofisica', 'extensao', 'largura']
        # 'calado'

class EdifConstPortuariaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EdifConstPortuaria
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipoedifport', 'administracao', 'matconstr', 'operacional', 'situacaofisica']

class EdifConstrAeroportuariaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EdifConstrAeroportuaria
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'operacional', 'situacaofisica', 'administracao', 'matconstr', 'tipoedifaero']

class EdifMetroFerroviariaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EdifMetroFerroviaria
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'multimodal', 'funcaoedifmetroferrov', 'operacional', 'situacaofisica', 'administracao', 'matconstr']

class FundeadouroSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Fundeadouro
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'administracao', 'destinacaofundeadouro']

class PistaPontoPousoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PistaPontoPouso
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'operacional', 'situacaofisica', 'homologacao', 'tipopista', 'usopista', 'revestimento']
        # 'extensao', 'largura'

class PonteSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Ponte
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'modaluso', 'tipoponte', 'situacaofisica', 'operacional', 'matconstr', 'posicaopista']
        # 'extensao', 'largura', 'vaolivrehoriz', 'vaovertical', 'cargasuportmaxima', 'nrpistas', 'nrfaixas'

class SinalizacaoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Sinalizacao
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'situacaofisica', 'operacional', 'tiposinal']

class TravessiaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Travessia
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipotravessia']

class TrechoDutoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TrechoDuto
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'situacaofisica', 'operacional', 'matconstr', 'tipotrechoduto', 'mattransp', 'setor', 'posicaorelativa', 'situacaoespacial']
        # 'nrdutos'

class TrechoFerroviarioSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TrechoFerroviario
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'situacaofisica', 'operacional', 'codtrechoferrov', 'posicaorelativa', 'tipotrechoferrov', 'bitola', 'eletrificada', 'emarruamento', 'jurisdicao', 'administracao', 'concessionaria', 'nrlinhas']
        # 'cargasuportmaxima'

class TrechoHidroviarioSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TrechoHidroviario
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'situacaofisica', 'operacional', 'regime']
        # 'caladomaxseca', 'extensaotrecho'

class TrechoRodoviarioSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TrechoRodoviario
        geo_field = 'geom'
        fields = ['id_objeto', 'codtrechorodov', 'tipotrechorod', 'revestimento', 'situacaofisica', 'operacional', 'nrpistas', 'nrfaixas', 'trafego', 'canteirodivisorio', 'capaccarga', 'jurisdicao', 'administracao', 'concessionaria']

class TunelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Tunel
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'modaluso', 'situacaofisica', 'operacional', 'posicaopista', 'matconstr', 'tipotunel']
        # 'extensao', 'largura', 'altura', 'nrpistas', 'nrfaixas'

class BrejoPantanoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BrejoPantano
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'antropizada', 'denso', 'tipobrejopantano', 'classificacaoporte']
        # 'alturamediaindividuos'

class MangueSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Mangue
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'antropizada', 'denso', 'classificacaoporte']
        # 'alturamediaindividuos'

class VegRestingaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = VegRestinga
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'antropizada', 'denso', 'classificacaoporte']
        # 'alturamediaindividuos'

class EdifPubMilitarSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EdifPubMilitar
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipoedifmil', 'tipousoedif', 'situacaofisica', 'operacional', 'matconstr']

class PostoFiscalSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PostoFiscal
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipopostofisc', 'situacaofisica', 'operacional']

class EdifAgropecExtVegetalPescaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EdifAgropecExtVegetalPesca
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipoedifagropec', 'situacaofisica', 'operacional', 'matconstr']

class EdifIndustrialSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EdifIndustrial
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipodivisaocnae', 'situacaofisica', 'operacional', 'matconstr', 'chamine']

class ExtMineralSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ExtMineral
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tiposecaocnae', 'situacaofisica', 'operacional', 'tipoextmin', 'tipoprodutoresiduo', 'tipopocomina', 'procextracao', 'formaextracao', 'atividade']

class EdifReligiosaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EdifReligiosa
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'religiao', 'situacaofisica', 'operacional', 'tipoedifrelig', 'ensino', 'matconstr']

class EstGeradEnergiaEletricaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EstGeradEnergiaEletrica
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'codigoestacao', 'situacaofisica', 'operacional', 'destenergelet', 'tipoestgerad']
        # 'potenciaoutorgada', 'potenciafiscalizada'

class HidreletricaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Hidreletrica
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'codigohidreletrica', 'situacaofisica', 'operacional']
        # 'potenciaoutorgada', 'potenciafiscalizada'

class TermeletricaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Termeletrica
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'combrenovavel', 'situacaofisica', 'operacional', 'tipomaqtermica', 'geracao', 'tipocombustivel']
        # 'potenciaoutorgada', 'potenciafiscalizada'

class TorreEnergiaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TorreEnergia
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'situacaofisica', 'operacional', 'arranjofases', 'ovgd', 'tipotorre']
        # 'alturaestimada'

class BancoAreiaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BancoAreia
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipobanco', 'situacaoemagua', 'materialpredominante']

class BarragemSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Barragem
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'usoprincipal', 'situacaofisica', 'operacional', 'matconstr']

class CorredeiraSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Corredeira
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada']

class FozMaritimaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = FozMaritima
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada']

class IlhaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Ilha
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipoilha']

class MassaDaguaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MassaDagua
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipomassadagua', 'salinidade', 'regime']

class QuedaDaguaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = QuedaDagua
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipoqueda']
        # 'altura'

class RecifeSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Recife
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tiporecife', 'situamare', 'situacaocosta']

class RochaEmAguaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RochaEmAgua
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'situacaoemagua']
        # 'alturalamina'

class SumidouroVertedouroSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SumidouroVertedouro
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'causa', 'tiposumvert']

class TerrenoSujeitoInundacaoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TerrenoSujeitoInundacao
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'periodicidadeinunda']

class TrechoDrenagemSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TrechoDrenagem
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'pronfudidademedia', 'coincidecomdentrode', 'compartilhado', 'eixoprincipal', 'navegabilidade', 'regime', 'caladomax', 'larguramedia', 'velocidademedcorrente', 'dentrodepoligono']


class TrechoMassaDaguaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = TrechoMassaDagua
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipotrechomassa', 'salinidade', 'regime']

class AreaDesenvolvimentoControleSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AreaDesenvolvimentoControle
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'classificacao']

class MarcoDeLimiteSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = MarcoDeLimite
        geo_field = 'geom'
        fields = ['id_objeto', 'nome', 'nomeabrev', 'geometriaaproximada', 'tipomarcolim', 'latitude', 'longitude', 'orgresp', 'sistemageodesico', 'outrarefplan', 'outrarefalt', 'referencialaltim']
        # 'altitudeortometrica'


class PontosExibicaoWgs84Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = PontosExibicaoWgs84
        geo_field = 'geom'
        fields = [ 'id_gps', 'long_decimal', 'lat_decimal', 'sistema_geodesico']