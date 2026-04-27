try:
    import pytest
except ImportError:
    # Fallback for editors/linters that cannot resolve pytest
    # Provide a minimal no-op parametrize decorator so static analysis doesn't fail
    from types import SimpleNamespace

    def _parametrize(*_args, **_kwargs):
        def _decorator(func):
            return func
        return _decorator

    pytest = SimpleNamespace(mark=SimpleNamespace(parametrize=_parametrize))
from django.db.models import BooleanField, CharField, DateTimeField

from blog.models import Location
from tests.conftest import _TestModelAttrs


@pytest.mark.parametrize(('field', 'type', 'params'), [
    ('name', CharField, {'max_length': 256}),
    ('is_published', BooleanField, {'default': True}),
    ('created_at', DateTimeField, {'auto_now_add': True}),
])
class TestLocationModelAttrs(_TestModelAttrs):

    @property
    def model(self):
        return Location
