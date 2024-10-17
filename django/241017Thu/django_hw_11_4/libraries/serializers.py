from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class BookSerializer(serializers.ModelSerializer):
    class ReviewDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('content', 'score',)
    
    review_set = ReviewDetailSerializer(read_only=True, many=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class BookTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ('isbn',)

    book = BookTitleSerializer(read_only=True)
    class Meta:
        model = Review
        # fields = '__all__'
        # exclude = ('created_at', 'update_at')
        fields = ('book', 'content', 'score',)

class ReviewSerializer(serializers.ModelSerializer):


    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',)