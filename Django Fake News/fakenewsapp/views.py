from django.shortcuts import render
from joblib import load

def load_model(model_name):
    """Load the model based on the language selected."""
    if model_name == 'English_model':
        return load('./fakenewsapp/mymodels/English_model.joblib')
    else:
        return load('./fakenewsapp/mymodels/Swahili_model.joblib')

def predictor(request):
    """Render the form for news content input."""
    # Always render the form page for GET requests without parameters
    if not (request.method == 'GET' and 'text' in request.GET and 'language_model' in request.GET):
        return render(request, 'main.html')
    
    # Only process the form if parameters are present
    text = request.GET.get('text')
    language_model = request.GET.get('language_model')
    result = ''

    if text and language_model:
        # Load the corresponding model based on the selected language model
        model = load_model(language_model)
        try:
            if hasattr(model, 'predict'):
                prediction = model.predict([text])  # Making the prediction
                result = "real" if prediction[0] == 1 else "fake"
            else:
                result = "Error: Model does not have a 'predict' method."
        except Exception as e:
            result = f"Error: An exception occurred during prediction - {str(e)}"
    else:
        result = "Error: Missing text or language model selection."

    return render(request, 'result.html', {'result': result})

