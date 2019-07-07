import pytest


@pytest.fixture(params=[11, 12, 13, 14])
def fixture_with_params(request):
    return request.param
