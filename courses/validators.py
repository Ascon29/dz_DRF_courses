from rest_framework.serializers import ValidationError


class YoutubeOnly:
    """ Проверка, что ссылка ведет только на youtube.com """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        valid = 'youtube.com'
        tmp_val = dict(value).get(self.field)
        if tmp_val and valid not in tmp_val:
            raise ValidationError('Ссылка может быть только на Ютуб канал')
