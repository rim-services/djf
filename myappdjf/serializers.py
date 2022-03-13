from rest_framework import serializers
from myappdjf.models import *


class C_emploiSerializer(serializers.ModelSerializer):
    class Meta:
        model = C_emploi
        fields = '__all__'


class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = '__all__'

class TravailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travail
        fields = '__all__'

class DeposerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposer
        fields = '__all__'

class VisiteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visiteur
        fields = '__all__'

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'

class LangueSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Langue
        fields = '__all__'
    

class LangueMaitriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LangueMaitrise
        fields = '__all__'
