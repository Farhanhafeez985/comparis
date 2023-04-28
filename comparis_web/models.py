from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

from comparis import settings


class Properties(models.Model):
    prop_id = models.CharField(unique=True, max_length=255, null=False)
    title = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, null=True)
    street_number = models.CharField(max_length=255, null=True)
    postalcode = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    price = models.IntegerField(null=True)
    price_type_text = models.CharField(max_length=255, null=True)
    property_type_text = models.CharField(max_length=255, null=True)
    area = models.CharField(max_length=255, null=True)
    image_urls = models.TextField(null=True)
    found_for_the_first_time = models.DateField(blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    online_status = models.CharField(max_length=255, null=True)
    remarks = models.TextField(null=True)
    partner_name = models.CharField(max_length=255, null=True)
    room = models.FloatField(null=True)
    floor = models.CharField(max_length=255, null=True)
    living_space = models.CharField(max_length=255, null=True)
    year_of_construction = models.CharField(max_length=255, null=True)
    available_date = models.CharField(max_length=255, null=True, blank=True)
    is_old_building = models.CharField(max_length=255, null=True)
    vendor_name = models.CharField(max_length=255, null=True)
    vendor_phone = models.CharField(max_length=255, null=True)
    property_url = models.CharField(max_length=255)
    scraped_date = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)


    class Meta:
        db_table = 'properties'
