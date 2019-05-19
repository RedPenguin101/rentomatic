from rentomatic.domain import room as r

class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self, filters = None):
        result = [r.Room.from_dict(i) for i in self.data]

        if filters is None:
            return result

        if 'code__eq' in filters:
            result = [r for r in result if r.code == filters['code__eq']]

        if 'price__eq' in filters:
            price_filter = float(filters['price__eq'])
            result = [r for r in result if r.price == price_filter]

        if 'price__lt' in filters:
            price_filter = float(filters['price__lt'])
            result = [r for r in result if r.price < price_filter]

        if 'price__gt' in filters:
            price_filter = float(filters['price__gt'])
            result = [r for r in result if r.price > price_filter]

        return result
