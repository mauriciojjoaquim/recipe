from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase

   
class RecipeViewTest(RecipeTestBase):
    def test_recipe_view_home_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
        
    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
        
    def test_recipe_home_view_load_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
             
    def test_recipe_home_template_shows_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here</h1>',
            response.content.decode('utf-8')
        )
        
    def test_recipe_home_template_dont_loads_recipes_bot_published(self):
        
        # Need a recipe for this teste
        self.make_recipe(is_published=False)
        
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        
         # check if ome recipe exists
        self.assertIn(
            '<h1>No recipes found here</h1>',
            response.content.decode('utf-8')
        )
        
    def test_recipe_category_template_loads_recipes(self):
        needed_title ='this is a category test'
        # Need a recipe for this teste
        self.make_recipe(title=needed_title)
        
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        content = response.content.decode('utf-8')
        
        # check if ome recipe exists
        self.assertIn(needed_title, content)       
        
    def test_recipe_view_category_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
        
    def test_recipe_category_view_returns_404_if_no_recipe_found(self):
        response = self.client.get(
                reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404) 
    
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
    
    def test_recipe_view_detail_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 100000}))
        self.assertIs(view.func, views.recipe)              
        
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
        
    def test_recipe_search_user_correct_view_function(self):
        resolved = resolve(reverse('recipes:search')) 
        self.assertIs(resolved.func, views.search)
        
    def test_recipee_swarch_load_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=teste') 
        self.assertTemplateUsed(response, 'recipes/pages/search.html') 
        
    def test_recipe_search_404_if_no_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)