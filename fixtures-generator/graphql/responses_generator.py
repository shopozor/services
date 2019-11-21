from test_utils import json_helpers

import graphql.responses_generator_helpers as helpers

import abc
import os


class ResponsesGenerator():

    __metaclass__ = abc.ABCMeta

    def __init__(self, fixtures_dir, output_dir, fixtures_set):
        self._OUTPUT_DIR = output_dir
        self._INPUT_DIR = os.path.join(fixtures_dir, fixtures_set)

    @abc.abstractmethod
    def _produce_data(self):
        pass

    @abc.abstractmethod
    def generate(self):
        pass

    def _to_json(self, object, output_filename):
        fullpath = os.path.join(self._OUTPUT_DIR, output_filename)
        output_dir = os.path.split(fullpath)[0]
        os.makedirs(output_dir, exist_ok=True)
        json_helpers.dump(object, fullpath)


class ShopListsGenerator(ResponsesGenerator):

    def __init__(self, fixtures_dir, output_dir, fixtures_set):
        super().__init__(fixtures_dir, os.path.join(
            output_dir, fixtures_set, 'Consumer'), fixtures_set)
        self.__SHOPS_FIXTURE = helpers.get_shopozor_fixture(self._INPUT_DIR)

    def _produce_data(self):
        return {
            'data': {
                'shops': [helpers.shop_item(shop) for shop in self.__SHOPS_FIXTURE['shops']]
            }
        }

    def generate(self):
        self._to_json(self._produce_data(), 'Shops.json')


class ShopCategoriesGenerator(ResponsesGenerator):

    def __init__(self, fixtures_dir, output_dir, fixtures_set):
        super().__init__(fixtures_dir, os.path.join(
            output_dir, fixtures_set, 'Consumer'), fixtures_set)
        self.__SHOPS_FIXTURE = helpers.get_shopozor_fixture(self._INPUT_DIR)

    def _produce_data(self):
        return {
            'data': {
                'categories': [helpers.category_item(category) for category in self.__SHOPS_FIXTURE['product_categories']]
            }
        }

    def generate(self):
        expected_categories = self._produce_data()
        helpers.set_page_info(expected_categories['data']['categories'])
        self._to_json(expected_categories, 'Categories.json')


class ProductListsGenerator(ResponsesGenerator):

    def __init__(self, fixtures_dir, output_dir, fixtures_set):
        super().__init__(fixtures_dir, os.path.join(
            output_dir, fixtures_set, 'Consumer'), fixtures_set)
        self.__SHOPS_FIXTURE = helpers.get_shopozor_fixture(self._INPUT_DIR)
        self.__USERS_FIXTURE = helpers.get_users_fixture(self._INPUT_DIR)

    def _product_data(self):
        product_catalogues = {}
        for shop in self.__SHOPS_FIXTURE['shops']:
            product_catalogues[shop['id']] = {}
            for category in self.__SHOPS_FIXTURE['product_categories']:
                category_id = category['id']
                product_catalogues[shop['id']][category_id] = {
                    'data': {
                        'products': {
                            'edges': []
                        }
                    }
                }
                totalCount = 0
                catalogue_edges = product_catalogues[shop['id']
                                                     ][category_id]['data']['products']['edges']
                for variant_id in [item['productvariant_id'] for item in self.__SHOPS_FIXTURE['shop_productvariant'] if item['shop_id'] == shop['id']]:
                    variant = [
                        entry for entry in self.__SHOPS_FIXTURE['productvariants'] if entry['id'] == variant_id][0]
                    # TODO: why isn't this working: shops_fixture.remove(variant)?
                    product_in_category = [entry for entry in self.__SHOPS_FIXTURE['products']
                                           if entry['id'] == variant['product_id'] and entry['category_id'] == category_id]
                    if len(product_in_category) == 0:
                        continue
                    product = product_in_category[0]
                    product_state = product['state']
                    # TODO: do the job even if the product isn't published; only increment totalCount if is_published == True
                    if product_state != 'VISIBLE':
                        continue
                    edges_with_product_id = [
                        edge for edge in catalogue_edges if edge['node']['id'] == product['id']]

                    new_variant = helpers.variant_node(variant)

                    if edges_with_product_id:
                        edge = edges_with_product_id[0]
                        edge['node']['variants'].append(new_variant)
                    else:
                        node = helpers.create_new_product_with_variant(
                            product, variant, new_variant, self.__USERS_FIXTURE, self.__SHOPS_FIXTURE)
                        catalogue_edges.append(node)
                        totalCount += 1
                helpers.set_page_info(
                    product_catalogues[shop['id']][category_id]['data']['products'], totalCount)

        return product_catalogues

    def __output_catalogues(self, shop_catalogues):
        for catalogue in shop_catalogues:
            output_dir = os.path.join('Catalogues', 'Shop-%d' % catalogue)
            for category in shop_catalogues[catalogue]:
                output_filename = os.path.join(
                    output_dir, 'Category-%d.json' % category)
                self._to_json(
                    shop_catalogues[catalogue][category], output_filename)

    def __output_product_details(self, product_details):
        for detail in product_details:
            product_id = detail['data']['product']['id']
            output_filename = os.path.join(
                'Products', 'Product-%d.json' % product_id)
            self._to_json(detail, output_filename)

    def generate(self):
        product_catalogues = self._product_data()
        expected_product_details = helpers.extract_products_from_catalogues(
            product_catalogues)
        expected_catalogues = helpers.extract_catalogues(product_catalogues)
        self.__output_catalogues(expected_catalogues)
        self.__output_product_details(expected_product_details)
        # TODO: output unpublished products too
