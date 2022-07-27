from rest_framework import serializers

class officeserializer(serializers.Modelserializer):
    class Meta:
        model = office
        fields = ['id','company_name','email','company_code','website']