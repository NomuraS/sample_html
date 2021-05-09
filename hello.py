import flask 

app = flask.Flask(__name__)


title='flask-frozen test'
name1 = 'Taro'
name2 = 'Jiro'

@app.route('/')
def index():
    return flask.render_template(
    	'index.html', 
    	title=title,
    	name1=name1,
    	name2=name2
    	)

@app.route('/pages/<page_name>.html', methods=['GET'])
def hello_function(page_name):
    return flask.render_template(
    	'/pages/%s.html' %page_name, 
    	title=title, 
    	name0=page_name,
    	)
    
if __name__ == "__main__":
    app.run(debug=True)

