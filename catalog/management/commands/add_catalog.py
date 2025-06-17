from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(title='Выпечка', description='Мучные кондитерские изделия')

        product = [
            {'name': 'Печенье', 'description': 'Овсяное с шоколадом', 'price': '250', 'created_at': '2025-01-01', 'updated_at': '2025-11-01', 'category': 'category'},
            {'name': 'Пряники', 'description': 'Ванильные с джемом', 'price': '300', 'created_at': '2025-01-01',
             'updated_at': '2025-11-01', 'category': 'category'},
        ]

        for product_data in product:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'product already exists: {product.name}'))
