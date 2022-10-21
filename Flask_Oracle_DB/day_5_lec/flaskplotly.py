
from flask import Flask, render_template
import pandas as pd
import cx_Oracle as o
import json
import plotly
import plotly.express as px
app = Flask(__name__)

@app.route('/')
def notdash():
   df = pd.DataFrame({
      'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges',
      'Bananas'],
      'Amount': [4, 1, 2, 2, 4, 5],
      'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
   })
   print(df)
   fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')

   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    
   return render_template('nodash.html', graphJSON=graphJSON)

@app.route('/a')
def a():
   df = px.data.iris()
   df.head()
   fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

   return render_template('nodash.html', graphJSON=graphJSON)

@app.route('/b')
def b():
   df = px.data.iris()
   df.head()

   fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species')
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

   return render_template('nodash.html', graphJSON=graphJSON)


@app.route('/student')
def student():
    
    sql = 'select * from student'
    dsn =o.makedsn('localhost','1521','xe')
    conn =o.connect( user='goorm',password='goorm', dsn=dsn)
    
    df = pd.read_sql(sql, conn)
    print(df)
    fig = px.bar(df, x="NAME", y="AGE", title="타이틀", width=600, height=400,
             labels={'NAME':'이름','AGE':'나이'},
             color_discrete_map={"나이": "RebeccaPurple"},
             template="simple_white",text='AGE')
    # fig.update_layout(yaxis_range=[0,100])

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('nodash.html', graphJSON=graphJSON)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8077, debug=True)
