from catalog.models import Product


class CategoryService:

    @staticmethod
    def get_products_by_category(product_id):
        """Возвращает все продукты указанной категории"""
        category = Product.object.filter(product_id=product_id)
        return f"{category.title} {category.description}"
