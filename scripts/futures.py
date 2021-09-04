from make_markdown_table import make_markdown_table

def format_number(x):
    if(x < 0):
        return "(" + str(-x) + ")"
    return str(x)


def future_analysis(quantity, prices, margin, maintenance, decimals=2, long=True):

    payoff = 0
    payoff_acum = 0
    margin_account = margin

    data = [["Dia", "Cotizacion", "Ganancia", "Ganancia Acumulada", "Cuenta margen",
             "Margin call"], [":-:", "-:", "-:", "-:", '-:', '-:'], [1, prices[0], payoff, payoff_acum, margin_account, 0]]

    for i in range(1, len(prices)):
        if long:
            payoff = quantity * (prices[i] - prices[i - 1])
        else:
            payoff = quantity * (prices[i - 1] - prices[i])

        payoff_acum += payoff
        margin_account += payoff

        payoff = round(payoff, decimals)
        payoff_acum = round(payoff_acum, decimals)
        margin_account = round(margin_account, decimals)

        margin_call = 0
        if long and margin_account < maintenance:
            margin_call = margin - margin_account

        data.append([i + 1, prices[i], format_number(payoff), format_number(payoff_acum),
                     margin_account, margin_call])

        if(margin_call != 0):
            margin_account = margin

    return make_markdown_table(data)


