from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase

   
class RecipeCategoryViewTest(RecipeTestBase):
    def test_recipe_category_template_loads_recipes(self):
        needed_title ='this is a category test'
        # Need a recipe for this teste
        self.make_recipe(title=needed_title)
        
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')
        
        # check if ome recipe exists
        self.assertIn(needed_title, content) 
        
    def test_recipe_category_template_dont__loads_recipes_bot_published(self):
        
        # Need a recipe for this teste
        self.make_recipe(is_published=False)
        
        response = self.client.get(
                reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertEqual(response.status_code, 404)