from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    # id = serializers.IntegerField(read_only=True)
    # first_name = serializers.CharField(max_length=64)
    # last_name = serializers.CharField(max_length=64)
    # pseudonym = serializers.CharField(max_length=64, allow_null=True, allow_blank=True)
    # age = serializers.IntegerField()
    # retired = serializers.BooleanField()
