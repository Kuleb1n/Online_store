from django.db import models


class ProductCategory(models.Model):
    title = models.CharField('Title', max_length=150, unique=True)
    description = models.TextField('Description', blank=True)
    slug = models.SlugField('URL', unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'


class Product(models.Model):
    title = models.CharField('Title', max_length=150)
    image = models.ImageField('Photo', upload_to='products_images/%Y/%m/%d/')
    description = models.TextField('Description', blank=True)
    short_description = models.CharField('Short_description', max_length=64, blank=True)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('Quantity', default=0)
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    slug = models.SlugField('URL', unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
