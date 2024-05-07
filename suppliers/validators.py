from rest_framework.serializers import ValidationError


class ParentValidator:

    def __init__(self, field_level, field_parent):
        self.field_level = field_level
        self.field_parent = field_parent

    def __call__(self, value):
        field_level_val = dict(value).get(self.field_level)
        field_parent_val = dict(value).get(self.field_parent)
        if field_level_val == 0 and field_parent_val is not None:
            raise ValidationError('Завод не может иметь поставщиков')
