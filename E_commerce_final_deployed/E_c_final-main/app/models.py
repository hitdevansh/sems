from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinLengthValidator

STATE_CHOICES = (
    ('ANDAMAN AND NICOBAR ISLANDS', 'PORT BLAIR'),
    ('ANDHRA PRADESH', 'AMARAVATI'),
    ('ARUNACHAL PRADESH', 'ITANAGAR'),
    ('ASSAM', 'DISPUR'),
    ('BIHAR', 'PATNA'),
    ('CHANDIGARH', 'CHANDIGARH'),
    ('CHHATTISGARH', 'RAIPUR'),
    ('DADRA AND NAGAR HAVELI AND DAMAN AND DIU', 'DAMAN'),
    ('DELHI', 'NEW DELHI'),
    ('GOA', 'PANAJI'),
    ('GUJARAT', 'GANDHINAGAR'),
    ('HARYANA', 'CHANDIGARH'),
    ('HIMACHAL PRADESH', 'SHIMLA'),
    ('JHARKHAND', 'RANCHI'),
    ('KARNATAKA', 'BANGALORE'),
    ('KERALA', 'THIRUVANANTHAPURAM'),
    ('LAKSHADWEEP', 'KAVARATTI'),
    ('MADHYA PRADESH', 'BHOPAL'),
    ('MAHARASHTRA', 'MUMBAI'),
    ('MANIPUR', 'IMPHAL'),
    ('MEGHALAYA', 'SHILLONG'),
    ('MIZORAM', 'AIZAWL'),
    ('NAGALAND', 'KOHIMA'),
    ('ODISHA', 'BHUBANESWAR'),
    ('PUDUCHERRY', 'PUDUCHERRY'),
    ('PUNJAB', 'CHANDIGARH'),
    ('RAJASTHAN', 'JAIPUR'),
    ('SIKKIM', 'GANGTOK'),
    ('TAMIL NADU', 'CHENNAI'),
    ('TELANGANA', 'HYDERABAD'),
    ('TRIPURA', 'AGARTALA'),
    ('UTTAR PRADESH', 'LUCKNOW'),
    ('UTTARAKHAND', 'DEHRADUN'),
    ('WEST BENGAL', 'KOLKATA'),
)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=250)

    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICE=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('N', 'Other'),
]

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    product_image = models.ImageField(upload_to="")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity*self.product.discounted_price

STATUS_CHOICE = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICE,default='Pending')
    @property
    def total_cost(self):
        return self.quantity*self.product.discounted_price

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class PasswordResetToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Token for {self.user.username}"

    @classmethod
    def create_token(cls, user):
        return cls.objects.create(user=user)

    @classmethod
    def get_token(cls, token):
        try:
            return cls.objects.get(token=token)
        except cls.DoesNotExist:
            return None

    @classmethod
    def delete_token(cls, token):
        cls.objects.filter(token=token).delete()

       