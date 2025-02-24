import unittest
from typing import Dict, List
from unittest.mock import Mock, patch

from day20 import (get_post_by_id, get_post_by_id_with_validation,
                   get_posts_by_user_id)

demo: Dict[str, str | int] = {
    'userId': 1,
    'id': 1,
    'title': 'sunt aut facere repellat provident',
    'body': 'quia et suscipit suscipit recusanda'
}

demo2: List[Dict[str, str | int]] = [
    {
        'userId': 1,
        'id': 2,
        'title': 'sunt aut facere repellat provident',
        'body': 'quia et suscipit suscipit recusanda'
    },
    {
        'userId': 1,
        'id': 3,
        'title': 'sunt aut facere repellat provident',
        'body': 'quia et suscipit suscipit recusanda'
    }
]


class TestDay20(unittest.TestCase):
    @patch('day20.http_get')
    def test_get_post_by_id(self, mock_get: Mock) -> None:
        mock_get.return_value.json.return_value = demo
        result = get_post_by_id(1)
        self.assertEqual(result['id'], demo['id'])
        self.assertEqual(result['title'], demo['title'])
        self.assertEqual(result['body'], demo['body'])

    @patch('day20.http_get')
    def test_get_posts_by_user_id(self, mock_get: Mock) -> None:
        mock_get.return_value.json.return_value = demo2
        result1 = get_posts_by_user_id(1)
        self.assertEqual(result1, demo2)

    def test_get_post_by_id_with_validation(self) -> None:
        with self.assertRaises(ValueError) as context:
            get_post_by_id_with_validation(-1)
        self.assertEqual(str(context.exception),
                         'post_id must be greater than 0'
                         )
