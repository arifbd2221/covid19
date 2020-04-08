from rest_framework import serializers


class ReportSerializer(serializers.Serializer):
    country = serializers.CharField()
    states = serializers.IntegerField()
    confirmed = serializers.IntegerField()
    deaths = serializers.IntegerField()
    recovered = serializers.IntegerField()