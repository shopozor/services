from faker.providers.lorem.la import Provider as LoremProvider

import collections
import os


class Provider(LoremProvider):

    conservation_modes = ('au frigo', 'à la cave', 'au soleil', 'au congélateur',
                          'à température ambiante', 'dans du papier alu', 'abri de la lumière')

    variant_names = (
        '1l', '2l', '2.5l', '5l', '250ml', '500ml', '45cm x 45cm', '55cm x 55cm', 'XS', 'S', 'M', 'L', 'XL', '100g', '200g', '250g', '500g', '1kg'
    )

    def __random_bool(self):
        return bool(self.generator.random.getrandbits(1))

    def __random_money_amount(self, min, max):
        return round(self.generator.random.uniform(min, max) * 2, 1) / 2

    def category_image_url(self):
        return os.path.join('category-backgrounds', '%s.png' % ''.join(self.random_letters()))

    def conservation_days(self):
        return self.random_int(min=0, max=360)

    def conservation_mode(self):
        return self.word(ext_word_list=self.conservation_modes)

    def description(self):
        return self.text(max_nb_chars=200)

    def image_alt(self):
        return self.text(max_nb_chars=50)

    def pricing_mode(self):
        distro = collections.OrderedDict(
            [('FREE', 0.25), ('AUTO_UNIT', 0.25), ('AUTO_PRICE', 0.25), ('BULK', 0.25)])
        return self.random_element(distro)

    def product_image_url(self):
        return os.path.join('products', '%s.png' % ''.join(self.random_letters()))

    def product_name(self):
        return self.sentence(nb_words=3, variable_nb_words=True)

    def product_state(self):
        distro = collections.OrderedDict(
            [('VISIBLE', 0.75), ('INVISIBLE', 0.15), ('DELETED', 0.1)])
        return self.random_element(distro)

    def productvariant_state(self):
        distro = collections.OrderedDict(
            [('VISIBLE', 0.70), ('INVISIBLE', 0.15), ('DELETED', 0.05), ('CHANGE_ASAP', 0.1)])
        return self.random_element(distro)

    def quantity(self):
        return self.random_int(min=0, max=1000)

    def quantity_allocated(self, quantity):
        return self.random_int(min=0, max=quantity)

    def variant_cost_price(self, max_amount=100):
        return self.__random_money_amount(0, max_amount)

    def variant_name(self):
        return self.word(ext_word_list=self.variant_names)

    def __has_vat_rate(self):
        return self.__random_bool()

    def vat_rate(self, vat_products_rate):
        return vat_products_rate if self.__has_vat_rate() else 0
