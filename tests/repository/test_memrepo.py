import pytest

import pytest

from rentomatic.domain import room as r
from rentomatic.repository import memrepo

@pytest.fixture
def room_dicts():
    return [
        {
            'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
            'size': 215,
            'price': 39,
            'longitude': -0.09998975,
            'latitude': 51.75436293,
        },
        {
            'code': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
            'size': 405,
            'price': 66,
            'longitude': 0.18228006,
            'latitude': 51.74640997,
        },
        {
            'code': '913694c6-435a-4366-ba0d-da5334a611b2',
            'size': 56,
            'price': 60,
            'longitude': 0.27891577,
            'latitude': 51.45994069,
        },
        {
            'code': 'eed76e77-55c1-41ce-985d-ca49bf6c0585',
            'size': 93,
            'price': 48,
            'longitude': 0.33894476,
            'latitude': 51.39916678,
        }
    ]

def test_repo_list_without_parameters(room_dicts):
    repo = memrepo.MemRepo(room_dicts)
    rooms = [r.Room.from_dict(i) for i in room_dicts]
    assert repo.list() == rooms

def test_repo_list_with_code_equal_filter(room_dicts):
    repo = memrepo.MemRepo(room_dicts)

    repo_rooms = repo.list(
            filters = {'code__eq': 'eed76e77-55c1-41ce-985d-ca49bf6c0585',}
            )
    assert len(repo_rooms) == 1
    assert repo_rooms[0].code == 'eed76e77-55c1-41ce-985d-ca49bf6c0585'

def test_repo_list_with_price_equal_filter(room_dicts):
    repo = memrepo.MemRepo(room_dicts)

    repo_rooms = repo.list(
            filters = {'price__eq':60}
            )
    assert len(repo_rooms) == 1
    assert repo_rooms[0].code == '913694c6-435a-4366-ba0d-da5334a611b2'

def test_repo_list_with_price__lt_filter(room_dicts):
    repo = memrepo.MemRepo(room_dicts)

    repo_rooms = repo.list(
            filters = {'price__lt':60 }
            )
    assert len(repo_rooms) == 2
    assert set([r.code for r in repo_rooms]) == {
                'f853578c-fc0f-4e65-81b8-566c5dffa35a',
                'eed76e77-55c1-41ce-985d-ca49bf6c0585',
            }

def test_repo_list_with_price__gt_filter(room_dicts):
    repo = memrepo.MemRepo(room_dicts)

    repo_rooms = repo.list(
            filters = {'price__gt':48 }
            )
    assert len(repo_rooms) == 2
    assert set([r.code for r in repo_rooms]) == {
                'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
                '913694c6-435a-4366-ba0d-da5334a611b2'
            }

def test_repo_list_with_price_between(room_dicts):
    repo = memrepo.MemRepo(room_dicts)

    repo_rooms = repo.list(
            filters = {
                'price__gt':48,
                'price__lt':66,
                }
            )
    assert len(repo_rooms) == 1
    assert set([r.code for r in repo_rooms]) == {
                '913694c6-435a-4366-ba0d-da5334a611b2'
           }