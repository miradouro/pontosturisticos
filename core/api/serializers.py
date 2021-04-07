from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from atracoes.models import Atracao
from enderecos.models import Endereco


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    enderecos = EnderecoSerializer()
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    descricao_completa = SerializerMethodField(read_only=True)

    class Meta:
        model = PontoTuristico
        # read_only_fields = ('comentarios', 'atracoes')
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentarios', 'avaliacoes', 'enderecos',
                  'descricao_completa', 'descricao_completa2')

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        enderecos = validated_data['enderecos']
        del validated_data['enderecos']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**enderecos)
        ponto.enderecos = end

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)

