from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    """
    Renderiza la página principal y procesa las operaciones matemáticas.
    """
    result = None  # Inicializa el resultado como None
    if request.method == 'POST':
        # Obtén los datos del formulario
        ops = request.form.get('operation')
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))

        # Realiza la operación seleccionada
        if ops == 'add':
            result = num1 + num2
        elif ops == 'subtract':
            result = num1 - num2
        elif ops == 'multiply':
            result = num1 * num2
        elif ops == 'divide':
            result = num1 / num2 if num2 != 0 else "Error: División por cero"
        else:
            result = "Operación inválida"

    # Renderiza la plantilla con el resultado (si existe)
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True) 
    