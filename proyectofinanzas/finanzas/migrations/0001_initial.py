# Generated by Django 2.1.7 on 2019-03-16 04:09

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('cedula', models.CharField(blank=True, max_length=13)),
                ('tipoPersona', models.CharField(choices=[('F', 'Fisica'), ('J', 'Juridica')], default='F', max_length=3)),
                ('limite', models.IntegerField(default='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Corte',
            fields=[
                ('id', models.AutoField(help_text='ID Corte', primary_key=True, serialize=False)),
                ('Ano', models.IntegerField(default=2019, help_text='Ano', validators=[django.core.validators.MinValueValidator(2000)])),
                ('Mes', models.CharField(choices=[('Ene', 'Enero'), ('Feb', 'Febrero'), ('Mar', 'Marzo'), ('Abr', 'Abril'), ('May', 'Mayo'), ('Jun', 'Junio'), ('Jul', 'Julio'), ('Ago', 'Agosto'), ('Sep', 'Septiembre'), ('Oct', 'Octubre'), ('Nov', 'Noviembre'), ('Dic', 'Diciembre')], default='', max_length=3)),
                ('FechaCorte', models.DateField(auto_now=True)),
                ('BalanceInicial', models.IntegerField(default=0)),
                ('TotalIngresos', models.IntegerField(default=0)),
                ('TotalEgresos', models.IntegerField(default=0)),
                ('BalanceCorte', models.IntegerField(default=0)),
                ('Comentario', models.TextField(default='')),
                ('EstadoActivo', models.BooleanField(default=1)),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id', models.AutoField(help_text='ID  de Egreso', primary_key=True, serialize=False)),
                ('TipoEgreso', models.CharField(help_text='Tipo de egreso', max_length=50)),
                ('Descripcion', models.CharField(help_text='Descripcion', max_length=50)),
                ('EstadoActivo', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Fuente',
            fields=[
                ('id', models.AutoField(help_text='ID Gestion de Ingreso', primary_key=True, serialize=False)),
                ('Nombre', models.CharField(help_text='Fuente Ingreso', max_length=50)),
                ('Institucion', models.CharField(max_length=35)),
                ('EstadoActivo', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='GestionEgreso',
            fields=[
                ('id', models.AutoField(help_text='ID Gestion de Ingreso', primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(help_text='Descripcion', max_length=50)),
                ('EstadoActivo', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(help_text='ID de Ingreso', primary_key=True, serialize=False)),
                ('TipoIngreso', models.CharField(help_text='Tipo de ingreso', max_length=50)),
                ('Descripcion', models.CharField(help_text='Descripcion', max_length=50)),
                ('EstadoActivo', models.BooleanField(default=1)),
                ('Fuente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzas.Fuente')),
            ],
        ),
        migrations.CreateModel(
            name='RenglonEgreso',
            fields=[
                ('id', models.AutoField(help_text='ID Gestion de Ingreso', primary_key=True, serialize=False)),
                ('Nombre', models.CharField(help_text='Tipo de ingreso', max_length=50)),
                ('Descripcion', models.CharField(help_text='Descripcion', max_length=50)),
                ('Institucion', models.CharField(help_text='Institucion, empleador o cliente', max_length=35)),
                ('EstadoActivo', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.AutoField(help_text='ID Gestion de Ingreso', primary_key=True, serialize=False)),
                ('Nombre', models.CharField(help_text='Tipo de de pago (Tarjeta, efectivo, etc).', max_length=50)),
                ('EstadoActivo', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('id', models.AutoField(help_text='ID Transaccion', primary_key=True, serialize=False)),
                ('TipoTransaccion', models.CharField(choices=[('I', 'Ingreso'), ('E', 'Egreso')], default='', max_length=1)),
                ('FechaRegistro', models.DateField(auto_now=True)),
                ('Monto', models.CharField(help_text='Monto Transaccion', max_length=12)),
                ('Descripcion', models.CharField(help_text='Descripcion', max_length=50)),
                ('EstadoActivo', models.BooleanField(default=1)),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gestionegreso',
            name='Renglon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzas.RenglonEgreso'),
        ),
        migrations.AddField(
            model_name='gestionegreso',
            name='TipoIngreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzas.Egreso'),
        ),
        migrations.AddField(
            model_name='gestionegreso',
            name='TipoPago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzas.TipoPago'),
        ),
    ]
