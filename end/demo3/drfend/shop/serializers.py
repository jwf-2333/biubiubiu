from rest_framework import serializers
from .models import *







class GoodSerizlizer1(serializers.ModelSerializer):
    # 在序列化时指定字段   在多方  使用source = 模型名.字段名   read_only=True表示不能更改
    category = serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model = Good
        # fields = "__all__"
        fields = ('id','name','desc','category')

class CustomSerializer(serializers.RelatedField):
    """
    自定义序列化类
    """
    def to_representation(self, value):
        return str(value.id) + "--" + value.name + "--" + value.desc







class CategorySerizlizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10,min_length=2,error_messages={
        "max_length":"最多10个字",
        "min_length":"最少2个字"
    })

    def create(self, validated_data):
        instance = Category.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):

        instance.name = validated_data.get("name")
        instance.save()
        return instance


class GoodImgsSerializer(serializers.Serializer):
    img = serializers.ImageField()
    good = serializers.CharField(source='good.name')

    def validate(self, attrs):
        try:
            g = Good.objects.get(name = attrs["good"]["name"])
            attrs["good"] = g
        except:
            raise serializers.ValidationError("商品不存在")
        return attrs

    def create(self, validated_data):
        instance = GoodImgs.objects.create(**validated_data)
        return instance


class GoodSerizlizer(serializers.Serializer):
    name = serializers.CharField(max_length=20,min_length=2,error_messages={
        "max_length":"最多20个字",
        "min_length":"最少2个字"
    })

    category = CategorySerizlizer(label="分类")
    imgs = GoodImgsSerializer(label="图片",many=True,read_only=True)


    def validate_category(self, category):
        try:
            Category.objects.get(name = category["name"])
        except:
            raise serializers.ValidationError("输入的分类名不存在")
        return category

    def validate(self, attrs):

        try:
            c = Category.objects.get(name=attrs["category"]["name"])
        except:
            c = Category.objects.create(name=attrs["category"]["name"])
        attrs["category"] = c
        return attrs

    def create(self, validated_data):
        instance = Good.objects.create(**validated_data)
        return instance

class CategorySerizlizer1(serializers.ModelSerializer):
    """
    编写针对Category的序列化类
    本类指明了Category的序列化细节
    需要继承ModelSerializer才可以针对模型进行序列化
    在Meta类中 model指明序列化的模型 fields指明序列化的字段
    """
    goods = serializers.StringRelatedField(many=True)
    # goods = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # goods = serializers.HyperlinkedIdentityField(many=True,read_only=True,view_name='good-detail')
    class Meta:
        model = Category
        fields = ('name','goods')


