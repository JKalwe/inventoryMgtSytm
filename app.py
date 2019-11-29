from flask import Flask, render_template
import pygal




app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('inventory.html')


@app.route('/dashboard')
def piechart():
    ratios = [('Men', 5),('Ladies',10)]

    pie_chart = pygal.Pie()
    pie_chart.title = 'Men against ladies in techcamp training (in %)'
    pie_chart.add(ratios[0][0], ratios[0][1])
    pie_chart.add(ratios[1][0], ratios[1][1])
    # pie_chart.add('Chrome', 36.3)
    # pie_chart.add('Safari', 4.5)
    # pie_chart.add('Opera', 2.3)
    pie_data = pie_chart.render_data_uri()

    data = [
        {'month': 'January','total': 22},
        {'month': 'February','total': 27},
        {'month': 'March','total': 23},
        {'month': 'April','total': 20},
        {'month': 'May','total': 12},
        {'month': 'June','total': 32},
        {'month': 'July','total': 42},
        {'month': 'August','total': 72},
        {'month': 'September','total': 42},
        {'month': 'November','total': 42},
        {'month': 'December','total': 42},
    ]

    x = []
    y = []

    graph = pygal.Line()
    graph.title = '% Change Coolness of programming languages over time.'
    graph.x_labels = ['2011', '2012', '2013', '2014', '2015', '2016']
    graph.add('Python', [15, 31, 89, 200, 356, 900])
    # graph.add('Java', [15, 45, 76, 80, 91, 95])
    # graph.add('C++', [5, 51, 54, 102, 150, 201])
    # graph.add('All others combined!', [5, 15, 21, 55, 92, 105])
    graph_data = graph.render_data_uri()

    return render_template('dashboard.html', pie_data = pie_data, graph_data=graph_data)


@app.route('/index')
def big_day():
    x = 1000
    return render_template('index.html', x=x)



@app.route('/About')
def about_page():
    return render_template('About.html')



@app.route('/Contact')
def contact_page():
    return render_template('Contact.html')


@app.route('/inventory')
def inventory_page():
    return render_template('inventory.html')

if __name__ == '__main__':
    app.run()
