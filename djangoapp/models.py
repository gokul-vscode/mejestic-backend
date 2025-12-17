from django.db import models

# Create your models here.
# from django.db import models

class Product(models.Model):

    TYPE_CHOICES = [
        ('cat', 'Category'),
        ('premium', 'Premium'),
    ]

    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('football', 'Football'),
        ('cricket', 'Cricket'),
        ('tennis', 'Tennis'),
    ]

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='cat'
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
