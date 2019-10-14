import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from words.models import Word
import csv
from django.db.models import Q
from django.db import transaction


# Create your views here.

def main(request):
    return render(request,'home.html')


@transaction.atomic
def index_words():
    with open('word_search.tsv') as input_file:
        input_data = csv.reader(input_file, delimiter="\t")
        for data in input_data:
            print(data[0])
            try:
                word = Word.objects.get(text=data[0])
            except:
                word = Word.objects.create(text=data[0], occurence=data[1])


def autocomplete(request):
    params = request.GET.get('q').lower().strip('\t\n\r')
    queries = [Q(text__startswith=params), Q(text__icontains=params)]
    qs = Q()
    for query in queries:
        qs = qs | query
    words = Word.objects.filter(qs)
    return JsonResponse({"data": list(words.values_list('text',flat=True))})
