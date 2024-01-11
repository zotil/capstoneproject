from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=200, inventory=50)
        Menu.objects.create(title="Burger", price=100, inventory=150)

    # add another test_getall() instance method to retrieve all the Menu objects added for the test purpose.
    #
    # The retrieved objects must serialized, so make sure the method runs assertions to check if the serialized data equals the response.
    def test_getall(self):
        menu = Menu.objects.all()
        serialized_data = MenuSerializer(menu, many=True)
        response = self.client.get('/restaurant/menu/items/')
        self.assertEqual(response.data, serialized_data.data)



