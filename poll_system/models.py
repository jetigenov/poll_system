from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Poll(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Название'), null=True, blank=True)
    start_date = models.DateField(auto_now_add=True, verbose_name=_('Начало'))
    end_date = models.DateField(verbose_name=_('Конец'))
    description = models.CharField(max_length=255, verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('Опрос')
        verbose_name_plural = _('Опросы')

    def __str__(self):
        return self.name


QUESTION_TYPES = (
    ('text_field', 'Ответ текстом'),
    ('radio', 'Один вариант'),
    ('check_boxes', 'Выбор нескольких вариантов'),)


class Question(models.Model):
    text = models.TextField()
    type_question = models.CharField(max_length=20, choices=QUESTION_TYPES, verbose_name=_('Тип вопроса'))
    poll = models.ForeignKey(Poll, blank=True, on_delete=models.CASCADE, related_name='poll_question')

    class Meta:
        verbose_name = _('Вопрос')
        verbose_name_plural = _('Вопросы')

    def __str__(self):
        return self.text


class Choice(models.Model):
    name = models.TextField(verbose_name=_('Вариант ответа'))
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_choices')

    class Meta:
        verbose_name = _('Вариант')
        verbose_name_plural = _('Варианты')

    def __str__(self):
        return self.name


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    many_choice = models.ManyToManyField(Choice, null=True)
    one_choice = models.ForeignKey(Choice, null=True, on_delete=models.CASCADE, related_name='answers_one_choice')
    self_text = models.TextField(null=True)

    class Meta:
        verbose_name = _('Ответ')
        verbose_name_plural = _('Ответы')

    def __str__(self):
        return {self.author}-{self.question}