from abc import ABC, abstractmethod
from unicodedata import name 
class ProductAbstract(ABC):
    name=""
    description=""
    price=""

    @abstractmethod
    def edit_product(self, product_id):
        pass
    @abstractmethod
    def get_product_by_id(self, product_id):
        pass
    @abstractmethod
    def get_all_products(self, product_id):
        pass
    @abstractmethod
    def upload_product_image(self, product_id):
        pass
    @abstractmethod
    def delete_product(self, product_id):
        pass

class ProductManager (ProductAbstract):
    def edit_product(self, product_id):
        print("Product edited")
    def get_product_by_id(self, product_id):
        print("This is the product")
    def get_all_products(self, product_id):
        print("Here is all the product")





