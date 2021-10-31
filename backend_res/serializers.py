from rest_framework import serializers


class CommentSerializer(serializers.Serializer):
    code = serializers.CharField()
    client_id = serializers.CharField(max_length=200)
    client_secret = serializers.CharField()


class Cridential:
    def __init__(self, code, client_id, client_secret):
        self.code = code
        self.client_id = client_id
        self.client_secret = client_secret
