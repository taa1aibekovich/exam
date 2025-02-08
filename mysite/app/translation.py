from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Car)
class ProductTranslationOptions(TranslationOptions):
    fields = ('brand', 'model', 'transmission', 'description')



@register(Feedback)
class ProductTranslationOptions(TranslationOptions):
    fields = ('comment',)
