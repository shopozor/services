from test_utils import json_helpers

import settings

from copy import deepcopy

import itertools
import math
import os
import urllib.parse


def image_item(object, images):
    image = [{
        'alt': item['alt'],
        'url': item['url']
    } for item in images if item['id'] == object['image_id']]
    return image[0]


def shop_item(shop, image):
    return {
        'id': shop['id'],
        'name': shop['name'],
        'description': shop['description'],
        'image': image,
        'latitude': shop['latitude'],
        'longitude': shop['longitude']
    }


def category_item(category, images):
    associated_image = [{
        'alt': item['alt'],
        'url': item['url'],
    } for item in images if item['id'] == category['image_id']][0]

    return {
        'id': category['id'],
        'name': category['name'],
        'description': category['description'],
        'image': associated_image
    }


def set_page_info(query, totalCount=None):
    query['totalCount'] = totalCount if totalCount is not None else len(
        query['edges'])
    query['pageInfo'] = {
        'startCursor': 0,
        'endCursor': query['totalCount'] - 1
    }


def get_users_fixture(input_dir, personas=tuple()):
    users_fixture = []
    if personas:
        users_fixture = list(itertools.chain.from_iterable([json_helpers.load(os.path.join(
            input_dir, 'Users', f'{persona}.json'))['users'] for persona in personas]))
    else:
        users_fixture = json_helpers.load(os.path.join(
            input_dir, 'Users', 'producers.json'))['users']
        users_fixture.extend(json_helpers.load(os.path.join(
            input_dir, 'Users', 'managers.json'))['users'])
        users_fixture.extend(json_helpers.load(os.path.join(
            input_dir, 'Users', 'rex.json'))['users'])
        users_fixture.extend(json_helpers.load(os.path.join(
            input_dir, 'Users', 'softozor.json'))['users'])
    return users_fixture


def get_shopozor_fixture(input_dir):
    return json_helpers.load(os.path.join(
        input_dir, 'Shopozor.json'))


def get_images_fixture(input_dir):
    return json_helpers.load(os.path.join(
        input_dir, 'Images.json'))


def variant_node(variant):
    return {
        'id': variant['id'],
        'name': variant['name'],
        'state': variant['state'],
        'stockQuantity': max(variant['quantity'] - variant['quantity_allocated'], 0),
        'grossCostPrice': variant['gross_cost_price']
    }


def price_range(start, stop):
    return {
        'priceRange': {
            'start': start,
            'stop': stop
        }
    }


def placeholder_product_thumbnail():
    return {
        'alt': None,
        'url': 'images/placeholder.png'
    }


def product_thumbnail(associated_images):
    return {
        'alt': associated_images[0]['alt'],
        'url': associated_images[0]['url']
    }


def product_node(product, variant, new_variant, associated_image, associated_producer, thumbnail):
    return {
        'node': {
            'id': product['id'],
            'conservation': {
                'mode': product['conservation_mode'],
                'days': product['conservation_days']
            },
            'description': product['description'],
            'image': associated_image,
            'name': product['name'],
            'producer': associated_producer,
            'thumbnail': thumbnail,
            'variants': [new_variant],
            'vatRate': product['vat_rate']
        }
    }


def create_new_product_with_variant(product, variant, new_variant, users_fixture, shops_fixture, images_fixture):
    staff_id = product['producer_id']
    user = [item for item in users_fixture if item['id'] == staff_id][0]
    address = [item for item in shops_fixture['addresses']
               if item['user_id'] == user['id']][0]
    associated_producer = {
        'id': user['id'],
        'description': user['description'],
        'firstName': user['first_name'],
        'lastName': user['last_name'],
        'address': {
            'streetAddress': address['street_address'],
            'city': address['city'],
            'postalCode': address['postal_code']
        }
    }
    associated_image = [{
        'alt': item['alt'],
        'url': item['url'],
    } for item in images_fixture['images'] if item['id'] == product['image_id']]
    # TODO: delete those images from the shops_fixture
    thumbnail = product_thumbnail(
        associated_image) if associated_image else placeholder_product_thumbnail()
    return product_node(product, variant, new_variant, associated_image, associated_producer, thumbnail)


def extract_products_from_catalogues(catalogues):
    my_catalogues = deepcopy(catalogues)
    result = []
    for shop in my_catalogues:
        for category in my_catalogues[shop]:
            for edge in my_catalogues[shop][category]['data']['products']['edges']:
                product = {
                    'data': {
                        'product': {}
                    }
                }
                node = edge['node']
                product_id = node['id']
                product_already_exists = [
                    item for item in result if item['data']['product']['id'] == product_id]
                if not product_already_exists:
                    node.pop('thumbnail', None)
                    product['data']['product'] = node
                    result.append(product)
    return result


def extract_catalogues(catalogues):
    my_catalogues = deepcopy(catalogues)
    for shop in my_catalogues:
        for category in my_catalogues[shop]:
            for edge in my_catalogues[shop][category]['data']['products']['edges']:
                node = edge['node']
                # TODO: remove it if is_published == False
                node.pop('conservation', None)
                node.pop('description', None)
                node.pop('images', None)
                node['producer'].pop('description', None)
                node['producer'].pop('address', None)
                for variant in node['variants']:
                    variant.pop('grossCostPrice', None)
                node.pop('vatRate', None)
    return my_catalogues