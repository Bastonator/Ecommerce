from datetime import datetime
from unicodedata import category
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.db.models.signals import post_save
from mptt.models import MPTTModel, TreeForeignKey


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, password, **other_fields)

    def create_user(self, email, username, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.email


'''
 cd storefront
  npm start
'''

'''
class Document(models.Model):
    name =
    user =
    date_created =
    date_updated =
    '''


class Category(MPTTModel):
    name = models.CharField(verbose_name=_("Category Name"), help_text=_("Required"), max_length=250, unique=True)
    slug = models.SlugField(verbose_name=_("Category URL"), max_length=250, unique=True, primary_key=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        #return reverse("Products:category", kwargs={"pk": self.pk})
        return reverse("Products:category", args=[self.slug])

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.TextField(verbose_name=_("Product Name"), help_text=_("Required"), max_length=355)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_("Name"), help_text=_("Required"), max_length=355)

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.TextField(verbose_name=_("Product Name"), help_text=_("Required"), max_length=355, null=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    description = models.TextField(verbose_name=_("Description"), help_text=_("Required"), max_length=355, blank=True)
    slug = models.SlugField(max_length=255, unique=True, primary_key=True)
    regular_price = models.DecimalField(verbose_name=_("Regular Price"), help_text=_("Maximum 99999.9"), error_messages={
        "name": {
            "max_length": _("The price must be between 0 and 99999.9"),
        },
    }, max_digits=7, decimal_places=1)
    discount_price = models.DecimalField(verbose_name=_("Discount Price"), help_text=_("Maximum 99999.9"),
                                        error_messages={
                                            "name": {
                                                "max_length": _("The price must be between 0 and 99999.9"),
                                            },
                                        }, max_digits=7, decimal_places=1)
    image = models.ImageField(verbose_name=_("image1"), help_text=_('upload image'), null=True, blank=True)
    image_first = models.ImageField(verbose_name=_("image2"), help_text=_('upload image'), null=True, blank=True)
    image_second = models.ImageField(verbose_name=_("image3"), help_text=_('upload image'), null=True, blank=True)
    image_third = models.ImageField(verbose_name=_("image4"), help_text=_('upload image'), null=True, blank=True)
    is_active = models.BooleanField(verbose_name=_("Product Visibility"), help_text=_("Set Product Visibility"), default=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        # return reverse("Products:category", kwargs={"pk": self.pk})
        return reverse("Products:product", args=[self.slug])

    def __str__(self):
        return self.name


class ProductSpecificationValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(verbose_name=_("Value"), help_text=_("Maximum of 200 characters"), max_length=200)

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value


class Order(models.Model):
    order_email = models.TextField(_('email address'), blank=True, null=True)
    phone = models.TextField(max_length=16, blank=True, null=True)
    address = models.TextField(max_length=2555, help_text=_(""), blank=True, null=True)
    ordered_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.order_email


class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=100)
    total_price = models.DecimalField(max_digits=7, decimal_places=1)
    ordered_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)