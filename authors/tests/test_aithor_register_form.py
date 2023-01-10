from unittest import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized

class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('username', 'Your username'),
        ('email', 'Your e-mail'),
        ('first_name', 'Ex.: John'),
        ('last_name', 'Ex.: Doe'),
        ('password', 'Type your password'),
        ('password2', 'Repet your password'),
    ])
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)
        
        
    @parameterized.expand([
        ('username', (
            'Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.'
            )),
        ('email', 'The e-mail must be valid.'),
        ('password', (
            'password must have at least one oppercase, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        )),
        
    ])
    def test_fields_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].help_text
        self.assertEqual(current, needed)
    
    
    @parameterized.expand([
        ('username', 'Usuário'),
        ('email', 'Endereço de email'),
        ('first_name', 'Primeiro nome'),
        ('last_name', 'Último nome'),
        ('password', 'Password'),
        ('password2', 'Password2'),
    ])
    def test_fields_label(self, field, needed):
        form = RegisterForm()
        current = form[field].label
        self.assertEqual(current, needed)
 