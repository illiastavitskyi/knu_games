from django.test import TestCase
from .models import Game


class GameTests(TestCase):

    def test_game_creation(self):

        game = Game.objects.create(
            title='CS2',
            description='Shooter game',
            price=500,
            release_date='2024-01-01',
            developer='Valve'
        )

        self.assertEqual(game.title, 'CS2')


    def test_home_page_opens(self):

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)