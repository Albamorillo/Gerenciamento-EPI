# models.py
from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome, password=None):
        if not email:
            raise ValueError('O email deve ser informado')
        if not nome:
            raise ValueError('O nome deve ser informado')
        
        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password=None):
        user = self.create_user(
            email=email,
            nome=nome,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class StatusEquipamento(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
class StatusEmprestimo(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class NivelAcesso(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Colaborador(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=50)
    funcao = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    
    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    quantidade_disponivel = models.IntegerField()
    validade = models.DateField(null=True, blank=True)
    status = models.ForeignKey(StatusEquipamento, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nome

class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True, validators=[validate_email])
    nivel_acesso = models.ForeignKey(NivelAcesso, on_delete=models.CASCADE)
    
    # Adicione estes campos corrigidos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='epi_management_usuarios',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='epi_management_usuarios',
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField()
    status = models.ForeignKey(StatusEmprestimo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Empréstimo para {self.colaborador}"
    
class RelatorioEmprestimo(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    total_emprestimos = models.PositiveIntegerField(default=0)
    total_devolvidos = models.PositiveIntegerField(default=0)
    total_pendentes = models.PositiveIntegerField(default=0)
    ultimo_emprestimo = models.DateField(null=True, blank=True)
    equipamento_mais_frequente = models.ForeignKey(Equipamento, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Relatório de Empréstimo"
        verbose_name_plural = "Relatórios de Empréstimos"

    def __str__(self):
        return f"Relatório de {self.colaborador.nome}"