from fixtures_generation import json_helpers

import os

filename = os.path.join('fixtures', 'tiny', 'Shopozor.json')

json_data = json_helpers.load(filename)

for table, data in json_data.items():
    for data_item in data:
        columns = ','.join(data_item.keys())
        values = ','.join(map(lambda val: f"'{val}'", data_item.values()))
        print(f'INSERT INTO public.{table} ({columns}) VALUES ({values});')
