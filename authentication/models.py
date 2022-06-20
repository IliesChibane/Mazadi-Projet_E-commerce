from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime, jwt

class MyUserManager(BaseUserManager):
	def create_user(self, email, username, age, localisation, password = None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')
		if not age:
			raise ValueError('User age is requirred')
		if not localisation:
			raise ValueError('User localisation is requirred')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			age=age,
			localisation=localisation,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, age, localisation, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
			age=age,
			localisation=localisation,
		)
		user.is_active = True
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True

		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30)
	age  				    = models.IntegerField()
	localisation 		    = models.CharField(max_length=200)

	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=False)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username','age','localisation']

	objects = MyUserManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True

	@classmethod
	def register(cls, email, username, password, re_passwod, age, localisation):

		errors = []

		if password != re_passwod:
			errors.append('Passwords do not match')

		if len(password) < 8:
			errors.append('Password must be at least 8 characters long')
		
		if cls.objects.filter(email=email).exists():
			errors.append('Email already exists')

		if int(age) < 16:
			errors.append('You are under age for creating an account')

		if errors:
			raise Exception(errors)

		return cls.objects.create_user(email, username, age, localisation, password)

	@classmethod
	def get_token(cls, email, password):

		user = cls.objects.filter(email=email).first()

		if not(user and user.check_password(password)):
			return None

		playload = {
			'id': user.id,
			'iat': datetime.datetime.utcnow(),
			'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
		}

		return jwt.encode(playload, 'SECRET_KEY', algorithm='HS256')

	@classmethod
	def get_user_from_token(cls, token):
		try:
			playload = jwt.decode(token, 'SECRET_KEY', algorithms=['HS256'])
		except:
			return None

		return cls.objects.get(pk=playload['id'])

