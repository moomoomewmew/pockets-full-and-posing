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
        fields = ('id', 'name', 'items', 'image')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    department = serializers.HyperlinkedRelatedField(
        view_name='department_detail',
        read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'department', 'description', 'image', 'price', 'quantity', 'size')
