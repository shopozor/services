from fixtures_faker import FakeDataFactory

import json_helpers
import settings

import argparse
import os


variants = {
    'tiny': {
        '#consumers': 1,
        '#producers': 1,
        '#managers': 1,
        '#rex': 1,
        '#softozor': 1,
        '#products': 1,
        '#shops': 1,
        '#max(variants/product)': 1,
        '#max(producers/shop)': 1,
        '#max(products/producer)': 1
    },
    'small': {
        '#consumers': 50,
        '#producers': 16,
        '#managers': 2,
        '#rex': 1,
        '#softozor': 1,
        '#shops': 2,
        '#max(variants/product)': 5,
        '#max(producers/shop)': 8,
        '#max(products/producer)': 10
    },
    'medium': {
        '#consumers': 100,
        '#producers': 30,
        '#managers': 5,
        '#rex': 1,
        '#softozor': 1,
        '#shops': 5,
        '#max(variants/product)': 5,
        '#max(producers/shop)': 6,
        '#max(products/producer)': 10
    },
    'large': {
        '#consumers': 1000,
        '#producers': 150,
        '#managers': 20,
        '#rex': 1,
        '#softozor': 1,
        '#shops': 20,
        '#max(variants/product)': 7,
        '#max(producers/shop)': 7,
        '#max(products/producer)': 25
    }
}


def generate_variant(variant_name, output_folder):

    print('#############################################')
    print('Generating data for %s variant' % variant_name)

    variant = variants[variant_name]
    os.makedirs(os.path.join(output_folder, variant_name), exist_ok=True)
    os.makedirs(os.path.join(output_folder,
                             variant_name, 'Users'), exist_ok=True)

    factory = FakeDataFactory(
        variant['#max(products/producer)'], variant['#max(producers/shop)'], variant['#max(variants/product)'])

    nb_of_consumers = variant['#consumers']
    start_index = 1
    consumers = factory.create_consumers(
        start_index, nb_of_consumers)
    json_helpers.dump(consumers, os.path.join(
        output_folder, variant_name, 'Users', 'consumers.json'))

    nb_of_producers = variant['#producers']
    start_index += nb_of_consumers
    producers = factory.create_producers(
        start_index, nb_of_producers)
    json_helpers.dump(producers, os.path.join(
        output_folder, variant_name, 'Users', 'producers.json'))

    nb_of_managers = variant['#managers']
    start_index += nb_of_producers
    managers = factory.create_managers(start_index, nb_of_managers)
    json_helpers.dump(managers, os.path.join(
        output_folder, variant_name, 'Users', 'managers.json'))

    nb_of_reges = variant['#rex']
    start_index += nb_of_managers
    rex = factory.create_reges(start_index, nb_of_reges)
    json_helpers.dump(rex, os.path.join(
        output_folder, variant_name, 'Users', 'rex.json'))

    nb_of_softozors = variant['#softozor']
    start_index += nb_of_reges
    softozor = factory.create_softozors(start_index, nb_of_softozors)
    json_helpers.dump(softozor, os.path.join(
        output_folder, variant_name, 'Users', 'softozor.json'))

    shopozor = {}

    addresses = factory.create_addresses(producers, managers, rex, softozor)
    shopozor.update(addresses)

    shops = factory.create_shops(variant['#shops'])
    shopozor.update(shops)

    categories = factory.create_categories()
    shopozor.update(categories)

    nb_images = variant['#shops'] * \
        variant['#max(producers/shop)'] * variant['#max(products/producer)']
    productimages = factory.create_productimages(nb_images)
    shopozor.update(productimages)

    products = factory.create_products(categories, producers, productimages)
    shopozor.update(products)

    productvariants = factory.create_productvariants(products)
    shopozor.update(productvariants)

    shop_productvariant = factory.create_shop_productvariant(
        shops, producers, products, productvariants)
    shopozor.update(shop_productvariant)

    vat = factory.create_vat()
    shopozor.update(vat)

    margin_defns = factory.create_margindefns()
    shopozor.update(margin_defns)

    json_helpers.dump(shopozor, os.path.join(
        output_folder, variant_name, 'Shopozor.json'), sort_keys=False)

    print('#############################################')


def main(output_folder, fixture_variant):
    if fixture_variant == 'all':
        for variant in 'tiny', 'small', 'medium', 'large':
            generate_variant(variant, output_folder)
    else:
        generate_variant(fixture_variant, output_folder)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate json fixtures')
    parser.add_argument('-o', '--output-folder', type=str, default=settings.FIXTURE_DIR,
                        help='Folder where to output the JSON files containing the users and passwords')
    parser.add_argument('--fixture-variant', type=str, default='all',
                        help='Fixture variant: tiny, small, medium, large, or all')
    args = parser.parse_args()

    main(args.output_folder, args.fixture_variant)
