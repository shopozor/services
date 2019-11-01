from dateutil.relativedelta import relativedelta
from faker.providers.date_time import Provider as DateTimeProvider


class Provider(DateTimeProvider):

    def publication_date(self):
        return self.date_between_dates().isoformat()

    def updated_at(self, start_date):
        end_date = start_date + relativedelta(years=1)
        return self.date_between_dates(date_start=start_date, date_end=end_date).isoformat()