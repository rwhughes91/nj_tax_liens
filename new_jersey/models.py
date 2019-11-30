from django.db import models
from decimal import Decimal
from django.urls import reverse

from . import choices


class Lien(models.Model):
    lien_id = models.IntegerField(unique=True)
    county = models.CharField(max_length=255, choices=choices.COUNTY_CHOICES)
    year = models.IntegerField()
    llc = models.CharField(max_length=255)
    block = models.CharField(max_length=255)
    lot = models.CharField(max_length=255)
    qualifier = models.CharField(max_length=255, default="", blank=True)
    advertisement_number = models.IntegerField(blank=True, null=True)
    mua_number = models.CharField(max_length=255, blank=True, default='')
    certificate_number = models.CharField(max_length=255, default="")
    lien_type = models.CharField(max_length=255, blank=True, default='')
    list_item = models.CharField(max_length=255, blank=True, default='')
    current_owner = models.CharField(max_length=255, blank=True, default='')
    longitude = models.DecimalField(default=Decimal(0), max_digits=19, decimal_places=10)
    latitude = models.DecimalField(default=Decimal(0), max_digits=19, decimal_places=10)
    assessed_value = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    tax_amount = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    status = models.CharField(default="", blank=True, max_length=255, choices=choices.STATUS_CHOICES)
    address = models.CharField(max_length=255, blank=True, default='')
    certificate_face_value = models.DecimalField(max_digits=11, decimal_places=2)
    winning_bid_percentage = models.DecimalField(max_digits=13, decimal_places=4)
    premium = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    sale_date = models.DateField(null=True, blank=True)
    recording_fee = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    recording_date = models.DateField(null=True, blank=True)
    search_fee = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    year_end_penalty = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    flat_rate = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    cert_int = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    total_subs_paid = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    total_cash_out = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    total_cash_received = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    total_principal_paid = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    total_actual_interest = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    total_legal_fees = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    total_principal_balance = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2)
    notes = models.TextField(blank=True, default='', max_length=255)
    redemption_date = models.DateField(blank=True, null=True)
    redemption_amount = models.DecimalField(default=Decimal(0), max_digits=11, decimal_places=2, blank=True)

    class Meta:
        ordering = ["county", "lien_id"]

    def __str__(self):
        return f"{self.block}-{self.lot}-{self.qualifier}, {self.county}, {self.lien_id}"

    def get_absolute_url(self):
        return reverse("new_jersey:lien_detail", kwargs={
            "lien_id": self.lien_id
        })


class Sub(models.Model):
    sub_type = models.CharField(max_length=255, choices=choices.SUB_TYPE_CHOICES)
    sub_date = models.DateField()
    total = models.DecimalField(max_digits=11, decimal_places=2)
    lien = models.ForeignKey(Lien, on_delete=models.CASCADE)

    class Meta:
        order_with_respect_to = 'lien'

    def __str__(self):
        return "{}: sub type: {} sub date: {} sub amount: {}".format(
            self.lien_id, self.sub_type, self.sub_date, self.total
            )

    def get_absolute_url(self):
        return reverse("new_jersey:lien_detail", kwargs={
            "lien_id": self.lien_id
        })
