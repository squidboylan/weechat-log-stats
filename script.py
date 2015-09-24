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
                key = key.lstrip('@')
                key = key.lstrip('+')

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

        sortedfoo = sorted(foo.items(), key=lambda thing: thing[0], reverse=True)

        data = []
        dates = []

        start = sortedfoo[-1][0].split('-')
        curr = datetime.date(int(start[0]), int(start[1]), int(start[2]))

        end = sortedfoo[0][0].split('-')
        end = datetime.date(int(end[0]), int(end[1]), int(end[2]))

        while curr < end:
            year = str(curr.year)

            if curr.month < 10:
                month = "0" + str(curr.month)
            else:
                month = str(curr.month)

            if curr.day < 10:
                day = "0" + str(curr.day)
            else:
                day = str(curr.day)

            try:
                foo[year + "-" + month + "-" + day]

            except:
                foo[year + "-" + month + "-" + day] = 0

            curr += datetime.timedelta(days = 1)

        foo = sorted(foo.items(), key=lambda thing: thing[0], reverse=True)

        for thing in foo:
            date = thing[0].split('-')
            date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
            dates.append(date)

            data.append(thing[1])

        months = MonthLocator()
        days = DayLocator()
        monthsFmt = DateFormatter('%Y-%m')

        fig, ax = plt.subplots()
        ax.plot_date(dates, data, '-')

        ax.xaxis.set_major_formatter(monthsFmt)
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_minor_locator(days)
        ax.autoscale_view()

        ax.fmt_xdata = DateFormatter('%Y-%m-%d')
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

        labels = keys
        sizes = data
        colors = ['blue', 'green', 'violet', 'red', 'orange', 'yellow']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    def messagetypedata(self):
        foo = {}

        for line in open(self.logfile):
            if re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}(\s+|\t+)(@|\+)?([a-z]|[A-Z])+.*", line):
                try:
                    foo['msg'] += 1
                except:
                    foo['msg'] = 0

            elif re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}(\s+|\t+)-->.*", line):
                try:
                    foo['join'] += 1
                except:
                    foo['join'] = 0

            elif re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}(\s+|\t+)<--.*", line):
                try:
                    foo['quit'] += 1
                except:
                    foo['quit'] = 0

            elif re.match("^[0-9]{4}-[0-9]{2}-[0-9]{2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}(\s+|\t+)\*.*", line):
                try:
                    foo['action'] += 1
                except:
                    foo['action'] = 0

        foo = sorted(foo.items(), key=lambda thing: thing[1], reverse=True)
        foo = foo[:100]
        data = []
        keys = []
        for thing in foo:
            data.append(thing[1])
            keys.append(thing[0])

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
thing.messagetypedata()
