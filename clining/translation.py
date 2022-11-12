from modeltranslation.translator import TranslationOptions, register
from .forms import (CaruselImage, CaruselDetail, GallaryCategory,
                    GallaryDetail, SubServices, CardServices, ServiceType, RoomCategory)


@register(CaruselImage)
class CaruselImageTranslation(TranslationOptions):
    fields = ('name',)

@register(CaruselDetail)
class CaruselDetailTranslation(TranslationOptions):
    fields = ('title', 'description')

@register(GallaryCategory)
class GallaryCategoryTranslation(TranslationOptions):
    fields = ('name',)

@register(GallaryDetail)
class GallaryDetailTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(SubServices)
class SubServicesTranslation(TranslationOptions):
    fields = ('name',)


@register(CardServices)
class CardServicesTranslation(TranslationOptions):
    fields = ('name', 'detail')

@register(ServiceType)
class ServiceTypeTranslation(TranslationOptions):
    fields = ('name',)


@register(RoomCategory)
class RoomCategoryTranslation(TranslationOptions):
    fields = ('name',)