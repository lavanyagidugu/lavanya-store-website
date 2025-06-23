from flask import Flask, render_template,jsonify

app = Flask(__name__)
JOBS=[
    {'product id' : '123456789',
    'product_name' : 'Traditional wear Dresses'
    },
    {'product id' : '123456756',
    'product_name' : 'Saree'
    },
    {'product id' : '123459890',
    'product_name' : 'Western Wear'
    },
    {'product id' : '123876789',
    'product_name' : 'Suites'
    }
    
]

@app.route("/")
def hello_world():
    return render_template("home.html",jobs=JOBS,company_name="LavanyaBalu")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
