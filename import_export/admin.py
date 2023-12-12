from django.contrib import admin
from .models import Brand


admin.site.register(Brand)


# class BrandAdmin(admin.ModelAdmin):
#     list_display = ('id', 'svg_image_preview')  # Добавьте превью изображения в административный список
#
#     def svg_image_preview(self, obj):
#         return obj.svg_image.url if obj.svg_image else None
#
#     svg_image_preview.short_description = 'SVG Image Preview'
#
#
# admin.site.register(Brand, BrandAdmin)
