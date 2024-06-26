from django.db import models


class Product(models.Model):
    """Описывает продукт."""

    name = models.CharField(
        max_length=50, verbose_name="Наименование продукта"
    )
    description = models.TextField(verbose_name="Описание продукта")
    preview = models.ImageField(
        upload_to="products/", verbose_name="Фото продукта"
    )
    category = models.ForeignKey(
        "Category",
        verbose_name="Категория",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    price = models.FloatField(verbose_name="Стоимость покупки")
    created_at = models.DateTimeField(
        verbose_name="Дата создания записи", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата изменения записи", auto_now_add=True
    )
    manufactured_at = models.DateTimeField(
        verbose_name="дата производства продукта", blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("name",)


class Category(models.Model):
    """Описывает категории продуктов."""

    name = models.CharField(
        max_length=50, verbose_name="Наименование категории"
    )
    description = models.TextField(verbose_name="Описание категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
