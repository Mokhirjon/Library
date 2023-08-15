from rest_framework import serializers
class BooksSerializer(serializers.ModelSerializer):
    book_name=serializers.CharField()
    book_cost=serializers.IntegerField()
    book_year=serializers.DateField()

class AvtorsSerializer(serializers.ModelSerializer):
    avtor_name=serializers.CharField()
    avtor_bday=serializers.DateField()
    avtor_books_created_name=serializers.CharField()
    avtor_date_of_die=serializers.DateField()
