import peewee


database = peewee.SqliteDatabase('maps.db')


class BaseTable(peewee.Model):

    class Meta:
        database = database


class SiteName(BaseTable):
    name = peewee.CharField()


class SiteUrl(BaseTable):
    urls = peewee.CharField()
    url_names = peewee.ForeignKeyField(SiteName, on_delete='CASCADE')


created = database.create_tables([SiteName, SiteUrl])