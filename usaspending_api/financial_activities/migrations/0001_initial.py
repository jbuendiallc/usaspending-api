# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-11 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('references', '0001_initial'),
        ('submissions', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialAccountsByProgramActivityObjectClass',
            fields=[
                ('data_source', models.CharField(choices=[('USA', 'USAspending'), ('DBR', 'DATA Act Broker')], help_text='The source of this entry, either Data Broker (DBR) or USASpending (USA)', max_length=3, null=True)),
                ('financial_accounts_by_program_activity_object_class_id', models.AutoField(primary_key=True, serialize=False)),
                ('ussgl480100_undelivered_orders_obligations_unpaid_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl480100_undelivered_orders_obligations_unpaid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl483100_undelivered_orders_oblig_transferred_unpaid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl488100_upward_adjust_pri_undeliv_order_oblig_unpaid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl490100_delivered_orders_obligations_unpaid_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl490100_delivered_orders_obligations_unpaid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl493100_delivered_orders_oblig_transferred_unpaid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl498100_upward_adjust_pri_deliv_orders_oblig_unpaid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl480200_undelivered_orders_oblig_prepaid_advanced_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl480200_undelivered_orders_oblig_prepaid_advanced_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl483200_undeliv_orders_oblig_transferred_prepaid_adv_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl488200_up_adjust_pri_undeliv_order_oblig_ppaid_adv_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl490200_delivered_orders_obligations_paid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl490800_authority_outlayed_not_yet_disbursed_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl490800_authority_outlayed_not_yet_disbursed_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl498200_upward_adjust_pri_deliv_orders_oblig_paid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('obligations_undelivered_orders_unpaid_total_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('obligations_undelivered_orders_unpaid_total_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('obligations_delivered_orders_unpaid_total_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('obligations_delivered_orders_unpaid_total_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('gross_outlays_undelivered_orders_prepaid_total_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('gross_outlays_undelivered_orders_prepaid_total_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('gross_outlays_delivered_orders_paid_total_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('gross_outlays_delivered_orders_paid_total_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('gross_outlay_amount_by_program_object_class_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('gross_outlay_amount_by_program_object_class_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('obligations_incurred_by_program_object_class_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl487100_down_adj_pri_unpaid_undel_orders_oblig_recov_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl497100_down_adj_pri_unpaid_deliv_orders_oblig_recov_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl487200_down_adj_pri_ppaid_undel_orders_oblig_refund_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl497200_down_adj_pri_paid_deliv_orders_oblig_refund_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('deobligations_recoveries_refund_pri_program_object_class_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('drv_obligations_incurred_by_program_object_class', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('drv_obligations_undelivered_orders_unpaid', models.DecimalField(blank=True, decimal_places=2, max_digits=21, null=True)),
                ('reporting_period_start', models.DateField(blank=True, null=True)),
                ('reporting_period_end', models.DateField(blank=True, null=True)),
                ('last_modified_date', models.DateField(blank=True, null=True)),
                ('certified_date', models.DateField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('final_of_fy', models.BooleanField(db_index=True, default=False)),
                ('object_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='references.ObjectClass')),
                ('program_activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='references.RefProgramActivity')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submissions.SubmissionAttributes')),
                ('treasury_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='program_balances', to='accounts.TreasuryAppropriationAccount')),
            ],
            options={
                'db_table': 'financial_accounts_by_program_activity_object_class',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TasProgramActivityObjectClassQuarterly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_source', models.CharField(choices=[('USA', 'USAspending'), ('DBR', 'DATA Act Broker')], help_text='The source of this entry, either Data Broker (DBR) or USASpending (USA)', max_length=3, null=True)),
                ('ussgl480100_undelivered_orders_obligations_unpaid_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl480100_undelivered_orders_obligations_unpaid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl483100_undelivered_orders_oblig_transferred_unpaid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl488100_upward_adjust_pri_undeliv_order_oblig_unpaid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl490100_delivered_orders_obligations_unpaid_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl490100_delivered_orders_obligations_unpaid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl493100_delivered_orders_oblig_transferred_unpaid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl498100_upward_adjust_pri_deliv_orders_oblig_unpaid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl480200_undelivered_orders_oblig_prepaid_advanced_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl480200_undelivered_orders_oblig_prepaid_advanced_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl483200_undeliv_orders_oblig_transferred_prepaid_adv_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl488200_up_adjust_pri_undeliv_order_oblig_ppaid_adv_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl490200_delivered_orders_obligations_paid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl490800_authority_outlayed_not_yet_disbursed_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl490800_authority_outlayed_not_yet_disbursed_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl498200_upward_adjust_pri_deliv_orders_oblig_paid_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('obligations_undelivered_orders_unpaid_total_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('obligations_undelivered_orders_unpaid_total_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('obligations_delivered_orders_unpaid_total_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('obligations_delivered_orders_unpaid_total_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('gross_outlays_undelivered_orders_prepaid_total_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('gross_outlays_undelivered_orders_prepaid_total_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('gross_outlays_delivered_orders_paid_total_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('gross_outlays_delivered_orders_paid_total_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('gross_outlay_amount_by_program_object_class_fyb', models.DecimalField(decimal_places=2, max_digits=21)),
                ('gross_outlay_amount_by_program_object_class_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('obligations_incurred_by_program_object_class_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl487100_down_adj_pri_unpaid_undel_orders_oblig_recov_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl497100_down_adj_pri_unpaid_deliv_orders_oblig_recov_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl487200_down_adj_pri_ppaid_undel_orders_oblig_refund_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('ussgl497200_down_adj_pri_paid_deliv_orders_oblig_refund_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('deobligations_recoveries_refund_pri_program_object_class_cpe', models.DecimalField(decimal_places=2, max_digits=21)),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('object_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='references.ObjectClass')),
                ('program_activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='references.RefProgramActivity')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submissions.SubmissionAttributes')),
                ('treasury_account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.TreasuryAppropriationAccount')),
            ],
            options={
                'db_table': 'tas_program_activity_object_class_quarterly',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='tasprogramactivityobjectclassquarterly',
            unique_together=set([('treasury_account', 'program_activity', 'object_class', 'submission')]),
        ),
    ]
