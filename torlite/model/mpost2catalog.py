# -*- coding:utf-8 -*-
# import tornpg
import peewee
import uuid
from torlite.core.base_model import BaseModel

from torlite.model.core_tab import CabPost2Catalog
from torlite.model.core_tab import CabCatalog
from torlite.model.core_tab import CabPost


class MPost2Catalog():
    def __init__(self):
        try:
            CabPost2Catalog.create_table()
        except:
            pass

    def query_all(self):
        recs = CabPost2Catalog.select().order_by(CabPost2Catalog.order)
        return (recs)

    def get_by_slug(self, slug):
        return CabPost2Catalog.get(slug=slug)

    def get_by_id(self, idd):
        return CabPost2Catalog.select().join(CabCatalog).where(CabPost2Catalog.post == idd)

    def get_by_info(self, post_id, catalog_id):
        if CabPost2Catalog.select().where((CabPost2Catalog.post == post_id) & (CabPost2Catalog.catalog == catalog_id)).count() == 1:
            return CabPost2Catalog.get((CabPost2Catalog.post == post_id) & (CabPost2Catalog.catalog == catalog_id))
        else:
            return False

    def query_count(self):
        recs = CabPost2Catalog.select(CabPost2Catalog.catalog, peewee.fn.COUNT(CabPost2Catalog.catalog).alias('num')).group_by(CabPost2Catalog.catalog)
        return (recs)

    def add_record(self, post_id, catalog_id, order=1):

        tt = self.get_by_info(post_id, catalog_id)
        if tt == False:
            print('a')
            entry = CabPost2Catalog.create(
                uid=str(uuid.uuid1()),
                post=post_id,
                catalog=catalog_id,
                order=order,
                # catalog_name = self.mtabtag.get_by_id(catalog_id).name,
                # slug = self.mtabtag.get_by_id(catalog_id).slug,
            )
            # entry.execute()
        else:
            entry = CabPost2Catalog.update(
                order=order,
                # catalog_name = self.mtabtag.get_by_id(catalog_id).name,
                # slug = self.mtabtag.get_by_id(catalog_id).slug,
            ).where(CabPost2Catalog.uid == tt.uid)
            entry.execute()
    def delete_by_id(self, uid):
        entry = CabPost2Catalog.delete().where( CabPost2Catalog.uid == uid)
        entry.execute()
    def get_num_by_cat(self, cat_id):
        return CabPost2Catalog.select(CabPost2Catalog.uid == cat_id).count()
        # return CabPost.select().where( CabPost.).count()
    def query_slug_by_pager(self, slug, cureent= 1):
        return CabPost2Catalog.select().join(CabCatalog).where(CabCatalog.slug == slug)