from rest_framework import serializers
from .models import Department, Item


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        view_name='item_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Department
        fields = ('id', 'name', 'image', 'items')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    department_url = serializers.HyperlinkedRelatedField(
        view_name='department_detail',
        read_only=True)
            
    department = serializers.PrimaryKeyRelatedField(
        queryset = Department.objects.all(),
    )

    class Meta:
        model = Item
        fields = ('id', 'name', 'department', 'department_url', 'description', 'image', 'price', 'quantity', 'size')
