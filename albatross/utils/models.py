# 逻辑删除模型
import django.db
import django.db.models


class SoftDeleteQuerySet(django.db.models.QuerySet):
    def delete(self):
        self.update(is_deleted=True)


class SoftDeleteManager(django.db.models.Manager):
    """
    仅返回未被删除的实例
    """
    _queryset_class = SoftDeleteQuerySet

    def get_queryset(self):
        """
        在这里处理一下QuerySet, 然后返回没被标记位is_deleted的QuerySet
        """
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints

        return self._queryset_class(**kwargs).filter(is_deleted=False)


class SoftDeleteModel(django.db.models.Model):
    """
    抽象类，添加 is_deleted 字段
    """
    is_deleted = django.db.models.BooleanField(default=False, verbose_name='是否删除')

    create_time = django.db.models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = django.db.models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True

    objects = SoftDeleteManager()

    def delete(self, using=None, soft=True, *args, **kwargs):
        """
        这里需要真删除的话soft=False即可
        """
        if soft:
            self.is_deleted = True
            self.save(using=using)
        else:
            return super(SoftDeleteModel, self).delete(using=using, *args, **kwargs)
