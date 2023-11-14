
from mrz.generator.mrva import MRVACodeGenerator

def generate(data):

    mrva_code = MRVACodeGenerator(*data)

    return mrva_code

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Process the form data (replace with your processing logic)
        form_data = request.form
        data = ("V", form_data["country"], form_data["surname"],form_data["given_name"],form_data["document_number"],
                form_data["nationality"],form_data["dob"],form_data["sex"],form_data["issuing_date"], 
                form_data["optional_values"])
        mrva_code = generate(data)
        result = {'message': 'Form data received successfully', 'data': str(mrva_code)}
        # result = {'message': 'Form data received successfully', 'data': str(mrva_code).split("\n")}
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



