from modeltranslation.translator import register, TranslationOptions
from .models import Items, Fakultet
@register(Items)
class  ItemTranslation(TranslationOptions):
    fields = ('name', 'text', 'fakultet')

@register(Fakultet)
class FakultetTranslation(TranslationOptions):
    fields = ('name',)