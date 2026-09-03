from client import AgenticBnplInstallmentCreditOptimizerClient

def main():
    client = AgenticBnplInstallmentCreditOptimizerClient()
    res = client.optimize_installment_plan(600.00, 'EXCELLENT', 4)
    print('BNPL Credit Optimizer: ' + res['plan_id'] + ' (' + res['selected_plan_type'] + ')')
    print('Monthly: $' + str(res['monthly_installment_usd']) + ' | Approval: ' + str(res['instant_credit_approval']))
    print('Schedule URL: ' + res['payment_schedule_url'])

if __name__ == '__main__':
    main()
