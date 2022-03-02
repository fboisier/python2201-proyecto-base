from datetime import date

from django import forms

from acceso.models import Usuario

CIERTA_EDAD = 18

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


class UsuarioForm(forms.ModelForm):

    confirmar_password = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))


    def clean_birthday(self):
        birthday = self.cleaned_data['birthday']
        edad = calculate_age(birthday)

        if birthday > date.today():
            raise forms.ValidationError(
                    f"solo fechas en pasado."
                )

        if edad < CIERTA_EDAD:
            raise forms.ValidationError(
                    f"La edad es menor a {CIERTA_EDAD}, porque tiene {edad} años."
                )
        return birthday

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if nombre == "PANCHO": 
            self.add_error('nombre', "El nombre es PANCHO")
        return nombre

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)

        if cleaned_data.get('password') != cleaned_data.get('confirmar_password'):
            raise forms.ValidationError(
                    "Las contraseñas no coinciden"
                )

    class Meta:
        model = Usuario
        fields  = ['nombre','apellido','username','email','birthday','password']

        labels = {
            'nombre':'Nombre: ',
            'apellido':'Apellido: ',
            'username':'Nombre Usuario: ',
            'email':'Correo: ',
            'birthday': 'Cumpleaños:',
            'password':'Contraseña: ',
            'description': 'Descripción'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type':'email'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type':'date', 'max':date.today().strftime('%Y-%m-%d')}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
