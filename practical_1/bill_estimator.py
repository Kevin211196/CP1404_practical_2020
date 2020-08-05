TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print('Electricity bill estimator 2.0')
choice = int(input('Which tariff? 11 or 31: '))
cent_per_kwh = float(input('Enter daily use in kWh: '))
days = int(input('Enter number of billing day: '))

if choice == 11:
    estimated_bill = cent_per_kwh * days * TARIFF_11
else:
    estimated_bill = cent_per_kwh * days * TARIFF_31

print('Estimated bill: ${:.2f}'.format(estimated_bill))