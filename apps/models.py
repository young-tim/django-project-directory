from django.db import models
from django_demo import settings
from datetime import datetime
import uuid, os

# Create your models here.

class CustomManager(models.Manager):
    """自定义manager，以列表形式"""

    # def delete(self):
    #     """
    #     Soft delete objects from queryset (set their ``is_deleted``
    #     field to True)
    #     """
    #     self.update(is_deleted=True)

    def fetch_all(self, *fields, **expressions):
        """
        获取全部数据
        :param fields:
        :param expressions:
        :return: <list>
        """
        # 使用方法：modelName.objects.fetch_all()
        data = []
        arrs = models.Manager.all(self)
        for arr in arrs:
            data.append(arr.to_dict())
        return data
        # return list(models.Manager.all(self).values(*fields, **expressions))

    def get_one(self, **kwargs):
        data = {}
        try:
            data = models.Manager.get(self, **kwargs)
        except:
            data = models.Manager.filter(self, **kwargs).last()
        return data


class BaseModel(models.Model):
    id = models.CharField(default=uuid.uuid4(), primary_key=True, unique=True, max_length=50)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    short = models.IntegerField(default=10, verbose_name="排序码")
    # is_deleted = models.BooleanField(default=False, choices=((False,'否'),(True,'是')), verbose_name="是否删除")

    # 使用方法：modelName.objects.funcName()
    objects = CustomManager()

    def __setitem__(self, k, v):
        self.k = v

    def to_dict(self, fields=None, exclude=None):
        # 使用方法：modelName.to_dict()
        data = {}
        for f in self._meta.concrete_fields + self._meta.many_to_many:
            value = f.value_from_object(self)

            if fields and f.name not in fields:
                continue

            if exclude and f.name in exclude:
                continue

            if isinstance(f, models.ManyToManyField):
                value = [i.id for i in value] if self.pk else None

            if isinstance(f, models.DateTimeField):
                value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None

            if isinstance(f, models.ImageField):
                value = str(value) if value else None

            data[f.name] = value

        return data

    class Meta:
        abstract = True


def upload_directory_path(instance,filename):
    # 重命名上传的文件名
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:20], ext)
    return os.path.join(datetime.now().strftime(str(settings.FILE_URL)), filename)