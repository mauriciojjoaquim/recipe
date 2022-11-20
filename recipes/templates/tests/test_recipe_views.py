from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


# Create your tests here.  

class RecipeViewTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view  = resolve(reverse('recipes:home'))
        self.assertIs(view.func,views.home)

    def test_recipe_home_views_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(reponse.status_code, 200)
        
    def test_recipe_home_views_loads_correct_template(self):
       response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(reponse, 'recipes/pages/home.html')
        
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
       response = self.client.get(reverse('recipes:home'))
       self.assertIn(
            <h1>No recipes found here</h1>
            response.content.decode('utf-8')
       )    

    def test_recipe_category_views_function_is_correct(self):
        view  = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func,views.category) 

     def test_recipe_category_views_returns_404_if_no_found(self):
          response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
            )
        self.assertEqual(response.status_code, 404)     

    def test_recipe_datail_views_function_is_correct(self):
        view  = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func,views.recipe)  
        
    def test_recipe_datail_views_views_returns_404_if_no_found(self):
         response = self.client.get(
        reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)    


      
    