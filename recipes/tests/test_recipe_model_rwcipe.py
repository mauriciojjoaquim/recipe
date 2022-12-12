from .test_recipe_base import RecipeTestBase, Recipe
from parameterized import parameterized

from django.core.exceptions import ValidationError

class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def make_recipe_default(self):
        recipe = Recipe(
        category=self.make_category(name='test default category'),
        author=self.make_author(username='Newuser'),
        title ='Recipe title',
        description ='Recipe description',
        slug ='recipe_slug',
        preparation_time =10,
        preparation_time_unit ='Minutos',
        servings =2,
        servings_unit ='Formas',
        preparation_steps ='Recipe prepatation steps',
        is_published =False,
        preparation_steps_is_html =False,
        )
        recipe.full_clean()
        recipe.save()
        return recipe
    
    @parameterized.expand([
           ('title', 65),
           ('description', 165),
           ('preparation_time_unit', 65),
           ('servings_unit', 65),
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
            
    def test_recipe_preparation_steps_is_html_is_flase_by_default(self):
        recipe = self.make_recipe_default()
        self.assertFalse(
            recipe.preparation_steps_is_html, 
            msg='preparation_steps_is_html is not False'
        )
    def test_recipe_is_published_is_flase_by_default(self):
        recipe = self.make_recipe_default()
        self.assertFalse(
            recipe.is_published, 
            msg='is_published is not False'
        )