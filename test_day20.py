from day20 import get_post_by_id, get_posts_by_user_id, get_post_by_id_with_validation
import unittest
from unittest.mock import patch, Mock


class TestDay20(unittest.TestCase):
    @patch('day20.http_get')
    def test_get_post_by_id(self, mock_get):
        mock_api = Mock()
        mock_api.json.return_value = {
            'userId': 1,
            'id': 1,
            'title': 'sunt aut facere repellat provident',
            'body': 'quia et suscipit suscipit recusanda'
        }
        mock_get.return_value = mock_api
        result = get_post_by_id(1)
        self.assertEqual(result['id'], 1)
        self.assertEqual(result['title'], 'sunt aut facere repellat provident')
        self.assertEqual(result['body'], 'quia et suscipit suscipit recusanda')

    @patch('day20.http_get')
    def test_get_posts_by_user_id(self, mock_get):
        mock_api = Mock()
        mock_api.return_value.json.return_value = [{
            'userId': 1,
            'id': 2,
            'title': 'sunt aut facere repellat provident',
            'body': 'quia et suscipit suscipit recusanda'
        }, {
            'userId': 1,
            'id': 3,
            'title': 'sunt aut facere repellat provident',
            'body': 'quia et suscipit suscipit recusanda'
        }]
        mock_get.return_value = mock_api
        result1 = get_posts_by_user_id(1)
        result2 = get_post_by_id_with_validation(1)
        self.assertEqual(result1, mock_get.return_value.json.return_value)
        self.assertEqual(result2, mock_get.return_value.json.return_value)

    def test_get_post_by_id_with_validation(self):
        with self.assertRaises(ValueError) as context:
            get_post_by_id_with_validation(-1)
        self.assertEqual(str(context.exception),
                         'post_id must be greater than 0'
                         )


if __name__ == '__main__':
    unittest.main()
