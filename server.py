from flask import Flask #import Flask package and tools
app = Flask(__name__) #create flask instance with current module

@app.route('/') #index route, @ is decorator used to attach route to function
def index():
    return "Hello Index!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<word>')
def sayWord(word):
    return f'Hi {word}!'

@app.route('/repeat/<int:num>/<word>') #path variable must be the same as parameter
def repeatWord(num, word):
    return word * num

if __name__=='__main__': #make sure we are in the correct module
    app.run(debug=True) #turn debug mode on. Also where you define host and ports