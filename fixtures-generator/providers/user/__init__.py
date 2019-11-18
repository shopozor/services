from faker.providers import BaseProvider

import collections


class Provider(BaseProvider):

    def is_active(self):
        distro = collections.OrderedDict([(True, 0.75), (False, 0.25)])
        return self.random_element(distro)
