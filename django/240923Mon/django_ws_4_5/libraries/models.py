from django.db import models
import requests

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        API_KEY = 'ttbghgghg961120001'
        params = {
            'ttbkey': API_KEY,
            'QueryType': 'ItemNewAll',
            'MaxResults': 10,
            'start': 1,
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': '20131101',
        }
        response = requests.get('http://www.aladin.co.kr/ttb/api/ItemList.aspx', params=params)
        data = response.json()
        # 데이터를 모델 인스턴스로 변환하여 저장한다
        for item in data['item']:
            params = {
                'isbn': item['isbn'],
                'author': item['author'],
                'title': item['title'],
                'category_name': item['categoryName'],
                'category_id': item['categoryId'],
                'price': item['priceStandard'],
                'fixed_price': item['fixedPrice'],
                'pub_date': item['pubDate'],
            }
            my_model = cls(**params)
            my_model.save()