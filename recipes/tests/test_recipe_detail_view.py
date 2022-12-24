from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase

   
class RecipeDetailViewTest(RecipeTestBase):       
    def test_recipe_view_detail_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 100000}))
        self.assertIs(view.func, views.recipe)
        
    def test_recipe_detail_view_returns_404_if_no_recipe_found(self):
        response = self.client.get(
                reverse('recipes:recipe', kwargs={'id': 10000})
        )
        self.assertEqual(response.status_code, 404)
        
    def test_recipe_detail_template_loads_the_correct_recipes(self):
        needed_title ='this is a detail page - is load one recipe'
        # Need a recipe for this teste
        self.make_recipe(title=needed_title)
        
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')
        
        # check if ome recipe exists
        self.assertIn(needed_title, content) 
        
    def test_recipe_detail_template_dont__loads_recipes_bot_published(self):
        
        # Need a recipe for this teste
        self.make_recipe(is_published=False)
        
        response = self.client.get(
                reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertEqual(response.status_code, 404)