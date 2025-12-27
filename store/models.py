from email.mime import image
from random import choice
from django.db import models

# Create your models her
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    Choices = [
        ('mobile_phone', 'Mobile Phone'),
        ('tablet', 'Tablet'),
        ('laptop', 'Laptop'),
        ('ipad', 'iPad'),
        ('tv', 'TV'),
        ('speaker', 'Speaker'),
        ('camera', 'Camera'),
        ('watch', 'Watch'),
        ('gadget', 'Gadget'),
    ]
    name = models.CharField(max_length=100, choices=Choices, unique=True)

    def __str__(self):
        return self.name

class SubCategory(BaseModel):
    choices = [
        ('Microsoft', 'Microsoft'),
        ('Samsung', 'Samsung'),
        ('Sony', 'Sony'),
        ('LG', 'LG'),
        ('Dell', 'Dell'),
        ('HP', 'HP'),
        ('Apple', 'Apple'),
        ('Lenovo', 'Lenovo'),
        ('Asus', 'Asus'),
        ('HTC', 'HTC'),
        ('Nokia', 'Nokia'),
        ('BlackBerry', 'BlackBerry'),
        ('Micromax', 'Micromax'),
        ('Karbonn', 'Karbonn'),
        ('Lenovo','Lenovo'),
        ('All Brand', 'All Brand'),
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100 , choices=choices)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    name = models.CharField(max_length=255)
    warranty = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    image = models.URLField(max_length=500)
    avaliabilty = models.CharField(max_length=50, choices=[('in_stock', 'In Stock'), ('out_of_stock', 'Out of Stock')], default='in_stock')
    discount_percentage = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return f"Image for {self.product.name}"