from django.db import models
import datetime

# one-indexed for the sake of the UI
PERIOD_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)]
QUARTER_CHOICES = [(1, 1), (2, 2), (3, 3), (4, 4)]


class SubmissionWindowSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    broker_id = models.IntegerField(unique=True)
    reporting_start = models.DateTimeField()
    reporting_end = models.DateTimeField()
    submission_start_date = models.DateTimeField()
    submission_end_date = models.DateTimeField()
    submission_fiscal_year = models.DateTimeField()
    submission_fiscal_quarter = models.IntegerField(choices=QUARTER_CHOICES)
    submission_fiscal_period = models.IntegerField(choices=PERIOD_CHOICES)
    is_quarterly = models.BooleanField()

    class Meta:
        managed = True
        db_table = "submission_window_schedule"

    def __str__(self):
        return f"Submission window Schedule {self.broker_id}"

    def is_closed(self):
        return datetime.now() > self.reporting_end

    def submission_reveal_date(self):
        return self.reporting_end + datetime.timedelta(days=1)
