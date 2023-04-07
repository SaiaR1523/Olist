from django.db import models

# Create your models here.

class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=50, blank=True, null=True)
    location = models.ForeignKey('Location', models.DO_NOTHING)

    class Meta:
        
        db_table = 'city'


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=50)
    location = models.ForeignKey('Location', models.DO_NOTHING)

    class Meta:
        
        db_table = 'customer'


class DetailOrder(models.Model):
    order = models.OneToOneField('Orders', models.DO_NOTHING, primary_key=True)  # The composite primary key (order_id, product_id) found, that is not supported. The first column is selected.
    product = models.ForeignKey('Product', models.DO_NOTHING)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    freight_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'detail_order'
        unique_together = (('order', 'product'),)


class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)

    class Meta:
        
        db_table = 'location'


class Orders(models.Model):
    order_id = models.CharField(primary_key=True, max_length=50)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    order_purchase_timestamp = models.DateField(blank=True, null=True)
    order_approved_at = models.DateField(blank=True, null=True)
    order_delivered_carrier_date = models.DateField(blank=True, null=True)
    order_delivered_customer_date = models.DateField(blank=True, null=True)
    order_estimated_delivery_date = models.DateField(blank=True, null=True)
    shipping_limit_date = models.DateField(blank=True, null=True)
    seller = models.ForeignKey('Seller', models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)

    class Meta:
        
        db_table = 'orders'


class Payment(models.Model):
    payment_id = models.CharField(primary_key=True, max_length=50)
    payment_sequential = models.CharField(max_length=50, blank=True, null=True)
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    payment_installments = models.IntegerField(blank=True, null=True)
    payment_value = models.IntegerField(blank=True, null=True)
    order = models.ForeignKey(Orders, models.DO_NOTHING)

    class Meta:
        
        db_table = 'payment'


class Product(models.Model):
    product_id = models.CharField(primary_key=True, max_length=50)
    product_category_name = models.CharField(max_length=50, blank=True, null=True)
    product_name_lenght = models.IntegerField(blank=True, null=True)
    product_description_lenght = models.IntegerField(blank=True, null=True)
    product_photos_qty = models.IntegerField(blank=True, null=True)
    product_length_cm = models.IntegerField(blank=True, null=True)
    product_height_cm = models.IntegerField(blank=True, null=True)
    product_width_cm = models.IntegerField(blank=True, null=True)
    product_weight_g = models.IntegerField(blank=True, null=True)
    seller = models.ForeignKey('Seller', models.DO_NOTHING)

    class Meta:
        
        db_table = 'product'


class Review(models.Model):
    review_id = models.CharField(primary_key=True, max_length=50)
    review_score = models.IntegerField(blank=True, null=True)
    review_comment_title = models.CharField(max_length=50, blank=True, null=True)
    review_comment_message = models.CharField(max_length=50, blank=True, null=True)
    review_creation_date = models.DateField(blank=True, null=True)
    review_answer_timestamp = models.DateField(blank=True, null=True)
    order = models.OneToOneField(Orders, models.DO_NOTHING)

    class Meta:
        
        db_table = 'review'


class Seller(models.Model):
    seller_id = models.CharField(primary_key=True, max_length=50)
    location = models.ForeignKey(Location, models.DO_NOTHING)

    class Meta:
        
        db_table = 'seller'


class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50, blank=True, null=True)
    location = models.ForeignKey(Location, models.DO_NOTHING)

    class Meta:
        
        db_table = 'state'
        
    def __str__(self):
        return self.state_id


class ZipCode(models.Model):
    zip_code_id = models.IntegerField(primary_key=True)
    zip_code_name = models.IntegerField(blank=True, null=True)
    location = models.ForeignKey(Location, models.DO_NOTHING)

    class Meta:
        
        db_table = 'zip_code'