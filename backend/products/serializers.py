from rest_framework import serializers
from .models import Product, Sizes, Ingredients

class SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizes
        fields = ['size', 'grams', 'price']

class IngredientsSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(IngredientsSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            # for multiple fields in a list
            for field_name in remove_fields:
                self.fields.pop(field_name)
    class Meta:
        model = Ingredients
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(read_only=True, slug_field='name')
    sizes = serializers.SerializerMethodField()
    ingredients = serializers.SerializerMethodField()

    def get_sizes(self, obj):
        selected_options = Sizes.objects.filter(name__name=obj.name)
        return SizesSerializer(selected_options, many=True).data
    
    def get_ingredients(self, obj):
        return IngredientsSerializer(obj.ingredients, many=True).data
    
    class Meta:
        model = Product
        fields = '__all__'


class ProductGroupSerializer(serializers.ModelSerializer):
    snacks = serializers.SerializerMethodField()
    # beverages = serializers.SerializerMethodField()
    # cocktails = serializers.SerializerMethodField()
    # cofe = serializers.SerializerMethodField()
    # deserts = serializers.SerializerMethodField()
    # sauces = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('snacks', )

    def _build_account_list(self, product_type):
        get_product = Product.objects.filter(product_type=product_type)
        serializer = ProductSerializer(get_product, many=True)
        return serializer.data

    def get_snacks(self, obj):
        return self._build_account_list(Product.SNACKS)
    
    # def get_beverages(self, obj):
    #     return self._build_account_list(Product.BEVERAGES)
    
    # def get_cocktails(self, obj):
    #     return self._build_account_list(Product.COCKTAILS)
    
    # def get_cofe(self, obj):
    #     return self._build_account_list(Product.COFE)
    
    # def get_deserts(self, obj):
    #     return self._build_account_list(Product.DESERTS)
    
    # def get_sauces(self, obj):
    #     return self._build_account_list(Product.SAUCES)
    

