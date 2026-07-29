from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
price = models.IntegerField(help_text="Price in cents (e.g., 50 = $0.50, 3300 = $33.00). Stripe minimum is 50.")
    currency = models.CharField(max_length=3, default='usd')

    def __str__(self):
        return self.name

    @property
    def price_display(self):
        return f"{self.price / 100:.2f}"

class Discount(models.Model):
    name = models.CharField(max_length=100)
    percent_off = models.IntegerField(help_text="Percentage off (0-100)", null=True, blank=True)
    amount_off = models.IntegerField(help_text="Amount off in cents", null=True, blank=True)

    def __str__(self):
        return self.name

class Tax(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Tax percentage")

    def __str__(self):
        return self.name

class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)
    tax = models.ForeignKey(Tax, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"