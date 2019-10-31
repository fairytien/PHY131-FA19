# Graph the butterfly curve.

import altair
import math as m

def butterfly_curve():
    t_vals = range(0,9000)
    x_vals = []
    y_vals = []
    for t in t_vals:
        x_vals.append(m.sin(t) * (m.exp(m.cos(t)) - 2*m.cos(4*t) -(m.sin(t/12))**5))
        y_vals.append(m.cos(t) * (m.exp(m.cos(t)) - 2*m.cos(4*t) -(m.sin(t/12))**5))
        
    data = altair.Data(X=x_vals, Y=y_vals)
    chart = altair.Chart(data)
    mark = chart.mark_point(size=2, filled=True, color='indigo')
    enc = mark.encode(x='X',y='Y')
    enc.display()

butterfly_curve()