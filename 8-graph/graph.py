from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker

#записываем данные из файла settings в массив
with open('settings.txt') as file:
    settings = [float(i) for i in file.read().split('\n')]

# загружаем данные в массив data, умножаем на шаг по напряжению
data = numpy.loadtxt('data.txt', dtype = int)*settings[1]

#создали массив из времен
times = numpy.array([i*settings[0] for i in range(data.size)])

fig, ax = pyplot.subplots(figsize = (16, 10), dpi = 500)
ax.axis([times.min(), times.max(), data.min(), data.max()])

ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

ax.set_title("\n".join(wrap('Процесс заряда и разряда конденсатора в RC - цепочке', 60)), loc = 'center', fontsize = 28,)

ax.grid(which = 'major', color = 'k')
ax.minorticks_on()
ax.grid(which = 'minor', color = 'gray', linestyle = ':')

ax.set_xlabel("Время, с", fontsize = 16)
ax.set_ylabel("Напряжение, В", fontsize = 16)

ax.text(130, 2.5,  "Время зарядки = 56.18 с", fontsize = 18)
ax.text(130, 2.4,  "Время разрядки = 146.25 с", fontsize = 18)

ax.plot(times, data, c = 'purple', linewidth = 1, label = "V(t)",marker = 'o', markevery = 30)
#ax.scatter(times[0:data.size:30],data[0:data.size:30], marker = 's', c ='red', s = 10)

ax.legend(shadow  = False, loc = 'right', fontsize = 30)

fig.savefig('graf.png')
fig.savefig('graf.svg')