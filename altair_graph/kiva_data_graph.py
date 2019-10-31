# Graph Kiva Lending Data.
loan_amount = [1250.0, 500.0, 1450.0, 200.0, 700.0, 100.0, 250.0, 225.0, 1200.0, 150.0, 600.0, 300.0, 700.0, 125.0, 650.0, 175.0, 1800.0, 1525.0, 575.0, 700.0, 1450.0, 400.0, 200.0, 1000.0, 350.0]
country_name = ['Azerbaijan', 'El Salvador', 'Bolivia', 'Paraguay', 'El Salvador', 'Philippines', 'Philippines', 'Nicaragua', 'Guatemala', 'Philippines', 'Paraguay', 'Philippines', 'Bolivia', 'Philippines', 'Philippines', 'Madagascar', 'Georgia', 'Uganda', 'Kenya', 'Tajikistan', 'Jordan', 'Kenya', 'Philippines', 'Ecuador', 'Kenya']
time_to_raise = [193075.0, 1157108.0, 1552939.0, 244945.0, 238797.0, 1248909.0, 773599.0, 116181.0, 2288095.0, 51668.0, 26717.0, 48030.0, 1839190.0, 71117.0, 580401.0, 800427.0, 1156218.0, 1166045.0, 2924705.0, 470622.0, 24078.0, 260044.0, 445938.0, 201408.0, 2370450.0]
num_lenders_total = [38, 18, 51, 3, 21, 1, 10, 8, 42, 1, 18, 6, 28, 5, 16, 7, 54, 1, 18, 22, 36, 12, 8, 24, 8]

import altair

# Make a scatter plot of the number of donors versus the time to raise the money for the loan. Make the size of the circle correspond to the loan amount. Make the color corresponds to the country.
data = altair.Data(loan=loan_amount,country=country_name,time=time_to_raise,lenders=num_lenders_total)
chart = altair.Chart(data)
mark = chart.mark_point()
enc = mark.encode(x='lenders',y='time',color='country:N',size='loan')
enc.display()

# Make a bar chart that shows the total amount of money loaned in each country.
data = altair.Data(loan=loan_amount,country=country_name)
chart = altair.Chart(data)
mark = chart.mark_bar()
enc = mark.encode(x='country:N',y='loan:Q',color='country:N')
enc.display()

# Make a bar chart that shows the number of loans in each country.
data = altair.Data(country=country_name)
chart = altair.Chart(data)
mark = chart.mark_bar()
enc = mark.encode(x='country:N',y='count()',color='country:N')
enc.display()

# Make a histogram that shows the distribution of the loan amounts.
data = altair.Data(loan=loan_amount)
chart = altair.Chart(data)
mark = chart.mark_bar()
enc = mark.encode(altair.X('loan', bin=True), y='count()')
enc.display()
