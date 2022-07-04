from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class UptimeCheckStat(Model):
    publisher_id = columns.Text(primary_key=True)
    check_id = columns.Integer(primary_key=True)
    check_date = columns.DateTime(primary_key=True)
    avg_response_ms = columns.Integer(default=0)
    total_up_sec = columns.Integer(default=0)
    total_down_sec = columns.Integer(default=0)
    total_unknown_sec = columns.Integer(default=0)
    original_avg_response_ms = columns.Integer(default=0)
    original_total_up_sec = columns.Integer(default=0)
    original_total_down_sec = columns.Integer(default=0)
    original_total_unknown_sec = columns.Integer(default=0)
    override = columns.Boolean()
