from django.db import models
from django.conf import settings

class CourseManager(models.Manager):
    # funcao search recebe um comando de consulta e retorna dados da outra classe referenciada
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontais=query) |
            models.Q(description__icontains=query)
        )

class Courses(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Atalho')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre o curso', blank=True)
    start_date = models.DateField('Data de Inicio', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    # AUTO NOW = VAI SER ATUALIZADO TODA VEZ Q FOR MODIFICADO
    # AUTO NOW ADD = SO VAI SER CRIADO QUANDO FOR INICIALIZADA UMA NOVA LINHA EM COURSES
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    # instancia o objects para ser o manager e executar funcao seach para consulta no banco.
    # facilita pq ai é so executar a funcao e nao precisa chamar o Manager toda vez para cada tabela.
    objects = CourseManager

    # RETORNA O NOME DO CURSO NO DJANGO ADMIN.
    def __str__(self):
        return self.name

    # CRIA O METODO PARA SER USADO NO FRONT. É USADO PARA CRIAR UM LINK, NESSE CASO ELE RETORNA REFERENTE AO SLUG DO CURSO CLICADO.
    def get_absolute_url(self):
        return "/cursos/%s" % self.slug

    # ADICIONA UMA MASCARA PRA MOSTRAR O VERBOSE AO INVES DO NOME DA CLASSE EM SI. Q QSERIA COURSES POR EXEMPLO.
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        # ORDENAGEM DE CONTEUDOS DA TABELA no caso ele vai nomear pelo 'name'
        ordering = ['name']

class Enrollment(models.Model):
    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado'),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='enrrolments', on_delete=models.CASCADE)
    course = models.ForeignKey(
        Courses, verbose_name='Curso', related_name='enrrolments',on_delete=models.CASCADE)
    status = models.IntegerField('Situação', choices = STATUS_CHOICES, default=1,blank=True)
    create_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = CourseManager

    def active(self):
        self.status = 1
        self.save()

    def is_approved(self):
        return self.status == 1

    class Meta:
        verbose_name= 'Inscrição'
        verbose_name_plural = 'Inscrições'
        # unicidade, ele s╩ deixa criar um model de user para cada course. evita repetição
        unique_together = (('user', 'course'),)