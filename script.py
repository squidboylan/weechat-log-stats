import sys
import matplotlib.pyplot as plt
from pylab import *
import re
import datetime

class graph:
    def __init__(self):
        self.logfile = sys.argv[1]

    def userdata(self):
        foo = {}

        for line in open(self.logfile):
            if re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}(\s+|\t+)(@|\+)?([a-z]|[A-Z])+.*", line):
                key = line.split('\t')[1]

                try:
                    val = foo[key] + 1
                    foo[key] = val

                except:
                    foo[key] = 0

        foo = sorted(foo.items(), key=lambda thing: thing[1], reverse=True)
        data = []
        keys = []
        for thing in foo:
            data.append(thing[1])
            keys.append(thing[0])

        print(keys)

        labels = keys
        sizes = data
        colors = ['blue', 'green', 'violet', 'red', 'orange', 'yellow']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    def timedata(self):
        foo = {}

        for line in open(self.logfile):
            if re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}(\s+|\t+)(@|\+)?([a-z]|[A-Z])+.*", line):
                key = line.split(' ')[0]

                try:
                    val = foo[key] + 1
                    foo[key] = val

                except:
                    foo[key] = 0

        foo = sorted(foo.items(), key=lambda thing: thing[0], reverse=True)

        data = []
        dates = []

        for thing in foo:
            date = thing[0].split('-')
            date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
            dates.append(date)

            data.append(thing[1])

        months = MonthLocator()  # every month
        monthsFmt = DateFormatter('%Y-%m')

        fig, ax = plt.subplots()
        ax.plot_date(dates, data, '-')

        ax.xaxis.set_major_formatter(monthsFmt)
        ax.autoscale_view()

        ax.fmt_xdata = DateFormatter('%Y-%m-%d')
        #ax.fmt_ydata = data
        ax.grid(True)

        fig.autofmt_xdate()
        plt.show()

    def worddata(self):
        foo = {}

        for line in open(self.logfile):
            if re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}(\s+|\t+)(@|\+)?([a-z]|[A-Z])+.*", line):
                for key in line.split(' ')[2:]:
                    key = key.lower()
                    key = key.replace("\n","")
                    if len(key) > 4:
                        try:
                            val = foo[key] + 1
                            foo[key] = val

                        except:
                            foo[key] = 0

        foo = sorted(foo.items(), key=lambda thing: thing[1], reverse=True)
        foo = foo[:100]
        data = []
        keys = []
        for thing in foo:
            data.append(thing[1])
            keys.append(thing[0])

        print(keys)

        labels = keys
        sizes = data
        colors = ['blue', 'green', 'violet', 'red', 'orange', 'yellow']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

thing = graph()

thing.userdata()
thing.worddata()
thing.timedata()
