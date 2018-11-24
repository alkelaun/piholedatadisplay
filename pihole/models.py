from django.db import models
import time

# Create your models here.

# pihole records an integer value for 'Status', this provides the translation key
# Originally, I put the definition inside the function. I moved it outside so it doesn't re-create the dictionary upon
# each function call. I'm not sure that happens. It could also be ALL CAPS per convention.
d_status_lookup = {1: 'Blocked', 2: 'Forwarded', 3: 'Cached'}

class FTL(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    timestamp = models.IntegerField(db_column='timestamp')
    type = models.IntegerField(db_column='type')
    status = models.IntegerField(db_column='status')
    domain = models.TextField(db_column='domain')
    client = models.TextField(db_column='client')
    forward = models.TextField(db_column='forward')

    def _change_timestamp_to_datetime(self):
        return time.ctime(self.timestamp)

    time = property(_change_timestamp_to_datetime)

    def _status_change_to_human_readable(self):
        return d_status_lookup[self.status]

    new_status = property(_status_change_to_human_readable)

    class Meta:
        managed = False
        app_label = 'pihole'
        db_table = 'queries'

