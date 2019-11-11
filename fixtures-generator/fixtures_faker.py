from faker import Faker
from providers.geo import Provider as ShopozorGeoProvider
from providers.product import Provider as ProductProvider
from providers.time import Provider as DateTimeProvider
from providers.user import Provider as UserProvider

import settings

import dateutil.parser
import itertools
import os
import unidecode


class FakeDataFactory:

    category_types = {
        'Fruits': ('Fruit'),
        'Légumes': ('Légume'),
        'Boucherie': ('Boucherie'),
        'Epicerie': ('Epicerie'),
        'Laiterie': ('Laiterie'),
        'Boulangerie': ('Boulangerie'),
        'Boissons': ('Boisson'),
        'Traiteur': ('Traiteur'),
        'Nettoyages': ('Nettoyage'),
        'Soins corporels': ('Soin corporel'),
        'Objets pour la maison': ('Objet pour la maison')
    }

    def __init__(self, max_nb_products_per_producer=10, max_nb_producers_per_shop=10, max_nb_variants_per_product=10, max_nb_images_per_product=10):
        self.__fake = Faker('fr_CH')
        self.__fake.seed('features')
        self.__fake.add_provider(ShopozorGeoProvider)
        self.__fake.add_provider(ProductProvider)
        self.__fake.add_provider(DateTimeProvider)
        self.__fake.add_provider(UserProvider)
        self.__MAX_NB_PRODUCERS_PER_SHOP = max_nb_producers_per_shop
        self.__MAX_NB_PRODUCTS_PER_PRODUCER = max_nb_products_per_producer
        self.__MAX_NB_IMAGES_PER_PRODUCT = max_nb_images_per_product
        self.__MAX_NB_VARIANTS_PER_PRODUCT = max_nb_variants_per_product

    def create_email(self, first_name, last_name):
        domain_name = self.__fake.free_email_domain()
        # get rid of any potential French accent from the first and last name
        return unidecode.unidecode('%s.%s@%s' % (first_name, last_name, domain_name)).lower()

    def __create_consumer(self, id):
        return {
            'id': id,
            'email': self.__fake.email(),
            'is_active': self.__fake.is_active(),
            'is_staff': False,
            'is_superuser': False
        }

    def create_consumers(self, start_index, list_size=1):
        result = [self.__create_consumer(start_index + id)
                  for id in range(0, list_size)]
        return {
            'users': result
        }

    def __create_producer(self, id):
        first_name = self.__fake.first_name()
        last_name = self.__fake.last_name()
        return {
            'id': id,
            'email': self.create_email(first_name, last_name),
            'is_active': True,
            'is_staff': True,
            'is_superuser': False,
            'first_name': first_name,
            'last_name': last_name,
            'description': self.__fake.description()
        }

    def create_producers(self, start_index, list_size=1):
        result = [self.__create_producer(start_index + id)
                  for id in range(0, list_size)]
        return {
            'users': result
        }

    def __create_manager(self, id):
        first_name = self.__fake.first_name()
        last_name = self.__fake.last_name()
        return {
            'id': id,
            'email': self.create_email(first_name, last_name),
            'is_active': True,
            'is_staff': True,
            'is_superuser': False,
            'first_name': first_name,
            'last_name': last_name,
            'description': self.__fake.description(),
        }

    def create_managers(self, start_index, list_size=1):
        result = [self.__create_manager(start_index + id)
                  for id in range(0, list_size)]
        return {
            'users': result
        }

    def __create_rex(self, id):
        first_name = self.__fake.first_name()
        last_name = self.__fake.last_name()
        return {
            'id': id,
            'email': self.create_email(first_name, last_name),
            'is_active': True,
            'is_staff': True,
            'is_superuser': False
        }

    def create_reges(self, start_index, list_size=1):
        result = [self.__create_rex(start_index + id)
                  for id in range(0, list_size)]
        return {
            'users': result
        }

    def create_softozor(self, id):
        first_name = self.__fake.first_name()
        last_name = self.__fake.last_name()
        return {
            'id': id,
            'email': self.create_email(first_name, last_name),
            'is_active': True,
            'is_staff': True,
            'is_superuser': True
        }

    def create_softozors(self, start_index, list_size=1):
        result = [self.create_softozor(start_index + id)
                  for id in range(0, list_size)]
        return {
            'users': result
        }

    def __get_random_elements(self, elements, length):
        return self.__fake.random_elements(
            elements=elements, length=length, unique=True)

    def __address(self, user_id):
        return {
            'user_id': user_id,
            'street_address': self.__fake.street_address(),
            'city': self.__fake.city(),
            'postal_code': self.__fake.postcode()
        }

    def create_addresses(self, producers, managers, reges, softozors):
        users = []
        users.extend(producers['users'])
        users.extend(managers['users'])
        users.extend(reges['users'])
        users.extend(softozors['users'])

        result = [self.__address(user['id']) for user in users]
        return {
            'addresses': result
        }

    def __shop(self, pk):
        return {
            'id': pk,
            'description': self.__fake.description(),
            'name': self.__fake.sentence(nb_words=5, variable_nb_words=True),
            'latitude': float(self.__fake.local_latitude()),
            'longitude': float(self.__fake.local_longitude())
        }

    def create_shops(self, list_size=1):
        result = [self.__shop(pk + 1) for pk in range(0, list_size)]
        return {
            'shops': result
        }

    def __category(self, pk, name):
        return {
            'background_image': self.__fake.category_image_url(),
            'background_image_alt': self.__fake.image_alt(),
            'description': self.__fake.description(),
            'name': name,
            'id': pk
        }

    def create_categories(self):
        start_pk = 1
        result = [self.__category(pk, category) for pk, category in enumerate(
            self.category_types, start_pk)]
        return {
            'product_categories': result
        }

    def __productimage(self, pk):
        return {
            'id': pk,
            'url': self.__fake.product_image_url(),
            'alt': self.__fake.image_alt()
        }

    def create_productimages(self, list_size=1):
        result = [self.__productimage(pk) for pk in range(1, list_size + 1)]
        return {
            'product_images': result
        }

    def __product(self, pk, categories, producer_id, image_id):
        description = self.__fake.description()
        category_name = self.__fake.random_element(
            elements=self.category_types.keys())
        category_id = [category['id']
                       for category in categories if category['name'] == category_name][0]
        publication_date = self.__fake.publication_date()
        return {
            'id': pk,
            'name': self.__fake.product_name(),
            'description': description,
            'publication_date': publication_date,
            'updated_at': self.__fake.updated_at(start_date=dateutil.parser.parse(publication_date)),
            'state': self.__fake.product_state(),
            'category_id': category_id,
            'producer_id': producer_id,
            'conservation_mode': self.__fake.conservation_mode(),
            'conservation_days': self.__fake.conservation_days(),
            'vat_rate': self.__fake.vat_rate(settings.VAT_rates['products']),
            'image_id': image_id
        }

    def create_products(self, categories, producers, images):
        result = []
        nb_visible_products = 0
        product_index = 1
        producer_ids = [item['id'] for item in producers['users']]
        for producer_id in producer_ids:
            nb_products = self.__fake.random.randint(
                1, self.__MAX_NB_PRODUCTS_PER_PRODUCER)
            for i in range(0, nb_products):
                product_id = i + product_index
                image_id = images['product_images'][product_id - 1]['id']
                product = self.__product(
                    product_id, categories['product_categories'], producer_id, image_id)
                nb_visible_products += int(product['state'] == 'VISIBLE')
                result.append(product)
            product_index += nb_products
        print('#visible products: %d out of %d' %
              (nb_visible_products, len(result)))
        return {
            'products': result
        }

    def __productvariant(self, pk, product_id):
        quantity = self.__fake.quantity()
        cost_price = self.__fake.variant_cost_price()
        return {
            'id': pk,
            'state': self.__fake.productvariant_state(),
            'product_id': product_id,
            'quantity': quantity,
            'quantity_allocated': self.__fake.quantity_allocated(quantity),
            'gross_cost_price': cost_price,
            'pricing_mode': self.__fake.pricing_mode(),
            'name': self.__fake.variant_name(),
            # TODO: generate reasonable measure, measure_unit, and gross_cost_price_unit!
            'measure': 0,
            'measure_unit': '',
            'gross_cost_price_unit': ''
        }

    def create_productvariants(self, products):
        result = []
        pk = 1
        for product in products['products']:
            # any product has at least one variant
            nb_variants = self.__fake.random.randint(
                1, self.__MAX_NB_VARIANTS_PER_PRODUCT)
            for _ in range(0, nb_variants):
                result.append(self.__productvariant(pk, product['id']))
                pk += 1
        return {
            'productvariants': result
        }

    def __shop_productvariant(self, variant_id, shop_id):
        return {
            'productvariant_id': variant_id,
            'shop_id': shop_id
        }

    def create_shop_productvariant(self, shops, producers, products, productvariants):
        result = []
        shop_ids = [item['id'] for item in shops['shops']]
        producer_ids = [item['id'] for item in producers['users']]
        total_nb_producers = 0
        for shop_id in shop_ids:
            nb_producers = self.__fake.random.randint(
                1, self.__MAX_NB_PRODUCERS_PER_SHOP)
            shop_producer_ids = self.__get_random_elements(
                producer_ids, nb_producers)
            shop_product_ids = [
                item['id'] for item in products['products'] if item['producer_id'] in shop_producer_ids]
            variant_ids = [variant['id']
                           for variant in productvariants['productvariants'] if variant['product_id'] in shop_product_ids]
            producer_ids = [
                id for id in producer_ids if id not in shop_producer_ids]
            for variant_id in variant_ids:
                result.append(self.__shop_productvariant(variant_id, shop_id))
            total_nb_producers += nb_producers
        print('#producers assigned to shops: %d out of %d' %
              (total_nb_producers, len(producers['users'])))
        return {
            'shop_productvariant': result
        }

    def __vat(self, type, rate):
        return {
            'type': type,
            'rate': rate
        }

    def create_vat(self):
        result = [self.__vat('PRODUCTS', settings.VAT_rates['products']), self.__vat(
            'SERVICES', settings.VAT_rates['services']), self.__vat('SPECIAL', settings.VAT_rates['special'])]
        return {
            'vat': result
        }

    def __margindefinition(self, role, margin):
        return {
            'role': role,
            'margin': margin
        }

    def create_margindefns(self):
        result = [
            self.__margindefinition(
                'MANAGER', settings.margin_rates['manager']),
            self.__margindefinition(
                'REX', settings.margin_rates['rex']),
            self.__margindefinition(
                'SOFTOZOR', settings.margin_rates['softozor'])
        ]
        return {
            'margindefinitions': result
        }
