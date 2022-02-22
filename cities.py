import csv


def city_list():
    with open('city.csv', 'r', encoding='utf-8') as city:
        fields = ['address']
        reader = csv.DictReader(city, fields, delimiter=',')
        cities_unfiltered = []
        cities_filtered = []

        for row in reader:
            cities_unfiltered.append(row['address'])

    cities_unfiltered.remove('address')

    for city_obj in cities_unfiltered:
        city_filter = city_obj.split('г ')
        cities_filtered.append(city_filter[1])

    cities_filtered.remove('- Югра АО, Сургутский р-н, ')

    item_1 = '- Югра АО, '
    while item_1 in cities_filtered:
        cities_filtered.remove('- Югра АО, ')

    return cities_filtered
