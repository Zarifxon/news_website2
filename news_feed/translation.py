


from modeltranslation.translator import register, TranslationOptions, translator
from .models import News, Category

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields= ("title", "body")


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", )


# 2-usul
# translator.register(News, NewsTranslationOptions)
# translator.register(Category, CategoryTranslationOptions)