from rest_framework import serializers

from .models import UserProfile, SubCategory, Category, CommentModel, PostModel


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'profile_picture']


class FilePathSerializer(serializers.Serializer):
    file_path = serializers.CharField(max_length=255)


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategories']

    def create(self, validated_data):
        subcategories_data = validated_data.pop('subcategories', [])
        category = Category.objects.create(**validated_data)
        for subcategory_data in subcategories_data:
            SubCategory.objects.create(category=category, **subcategory_data)
        return category


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    total_comments = serializers.SerializerMethodField()

    def get_total_comments(self, obj):
        return obj.comments.count()

    class Meta:
        model = PostModel
        fields = ['id', 'title', 'author', 'created_at', 'comments', 'total_comments']
