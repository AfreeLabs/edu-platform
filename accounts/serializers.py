from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from .models import Account


# Serialize User Credentials
class AccountSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = (
            'url','id', 'email', 'first_name', 'last_name', 'created_at', 'updated_at',
            'password', 'confirm_password'
        )
        read_only_fields = ('created_at', 'updated_at')

        def create(self, validated_data):
            return Account.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.first_name = validated_data.get(
                            'first_name', instance.first_name
                            )
            instance.last_name = validated_data.get(
                            'last_name', instance.last_name
                            )
            instance.save()

            password = validated_data.get('password', None)
            confirm_pass = validated_data.get(
                              'confirm_password', None
                            )
            if password and confirm_pass and password == confirm_pass:
                instance.set_password(password)
                instance.save()

            update_session_auth_hash(
                self.context.get('request'), instance
            )

            return instance
