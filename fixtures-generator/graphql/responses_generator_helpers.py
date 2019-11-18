from test_utils import json_helpers

import settings

from copy import deepcopy

import math
import os
import urllib.parse


MEDIA_URL = '/media/'
STATIC_URL = '/static/'
PRODUCT_THUMBNAIL_SIZE = 500
CATEGORY_THUMBNAIL_SIZE = 250


def shop_node(shop):
    return {
        'node': {
            'id': shop['id'],
            'name': shop['name'],
            'description': shop['description'],
            'geocoordinates': {
                'latitude': shop['latitude'],
                'longitude': shop['longitude']
            }
        }
    }


def category_node(category):
    return {
        'node': {
            'id': category['id'],
            'name': category['name'],
            'description': category['description'],
            'backgroundImage': {
                'alt': category['background_image_alt'],
                'url': urllib.parse.urljoin(MEDIA_URL, '%s-thumbnail-%dx%d.%s' % (category['background_image'].split('.')[0], CATEGORY_THUMBNAIL_SIZE, CATEGORY_THUMBNAIL_SIZE, category['background_image'].split('.')[1]))
            }
        }
    }


def set_page_info(query, totalCount=None):
    query['totalCount'] = totalCount if totalCount is not None else len(
        query['edges'])
    query['pageInfo'] = {
        'startCursor': 0,
        'endCursor': query['totalCount'] - 1
    }


def get_users_fixture(input_dir):
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
        'url': urllib.parse.urljoin(STATIC_URL, 'images/placeholder%dx%d.png' % (PRODUCT_THUMBNAIL_SIZE, PRODUCT_THUMBNAIL_SIZE))
    }


def product_thumbnail(associated_images):
    return {
        'alt': associated_images[0]['alt'],
        'url': urllib.parse.urljoin(MEDIA_URL, '%s-thumbnail-%dx%d.%s' % (associated_images[0]['url'].split('.')[0], PRODUCT_THUMBNAIL_SIZE, PRODUCT_THUMBNAIL_SIZE, associated_images[0]['url'].split('.')[1]))
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


def create_new_product_with_variant(product, variant, new_variant, users_fixture, shops_fixture):
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
        'url': urllib.parse.urljoin(MEDIA_URL, item['url']),
    } for item in shops_fixture['product_images'] if item['id'] == product['image_id']]
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
