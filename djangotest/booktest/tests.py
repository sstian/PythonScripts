from django.test import TestCase
import pytest

# Create your tests here.

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangotest.settings")
django.setup()

from booktest.models import BookInfo, HeroInfo
# from booktest.models import BookInfoManager
from datetime import date
from django.http.request import QueryDict


class Test:

    def test_crud(self):
        # insert
        b = BookInfo()
        b.title = "Python Core"
        b.pub_date = date(1990, 1, 1)
        b.save()
        h = HeroInfo()
        h.name = "duan"
        h.sex = False
        h.comment = "shen jian"
        h.book = b
        h.save()
        # query
        b2 = BookInfo.objects.get(id=1)
        b2.title
        b2.pub_date
        b2.heroinfo_set.all()
        # update
        b2.pub_date = date(2020, 9, 3)
        b2.save()
        # delete
        b2.delete()
    # def test_manage(self):
    #     # 类名.objets
    #     BookInfo.objects2.create_book("test3", "1900-1-1")

    def test_query(self):
        q = QueryDict("a=1&b=2&c=3")
        print(q["a"])           # 1
        q2 = QueryDict("a=1&a=2&c=3")
        print(q2.get("a"))      # 2
        print(q2.getlist("a"))  # ['1', '2']


if __name__ == "__main__":
    # Test().test_query()
    pass
