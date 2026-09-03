class AgenticBnplInstallmentCreditOptimizerClient:
    def optimize_installment_plan(self, cart_total_usd=480.00, customer_credit_tier='PRIME_TIER_1', preferred_term_months=4):
        monthly_amount = round(cart_total_usd / preferred_term_months, 2)
        return {
            'plan_id': 'bnpl_opt_9918',
            'cart_total_usd': cart_total_usd,
            'selected_plan_type': 'PAY_IN_4_ZERO_APR',
            'monthly_installment_usd': monthly_amount,
            'effective_apr_pct': 0.0,
            'instant_credit_approval': True,
            'payment_schedule_url': 'https://bnpl.klarna.genpark.ai/schedules/9918.json'
        }
