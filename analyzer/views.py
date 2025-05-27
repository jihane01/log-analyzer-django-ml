from django.shortcuts import render

# analyzer/views.py
from django.shortcuts import render
from .forms import LogForm
import joblib

def analyze_log(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            log_text = form.cleaned_data['log_text']
            
            # Load trained model
            model = joblib.load('error_classifier_model.joblib')
            vectorizer = joblib.load('vectorizer.joblib')
            
            # Predict error type
            prediction = model.predict(vectorizer.transform([log_text]))[0]
            
            # Simple fix suggestions (can be expanded)
            fixes = {
                "Network": "Check server connectivity or firewall rules.",
                "Database": "Verify table exists and permissions are correct.",
                "Resource": "Increase memory allocation or optimize code.",
                "Storage": "Free up disk space or expand storage.",
                "HTTP": "Validate URL or API endpoint.",
                "Security": "Review user permissions."
            }
            
            return render(request, 'analyzer/result.html', {
                'prediction': prediction,
                'fix_suggestion': fixes.get(prediction, "No specific suggestion available.")
            })
    else:
        form = LogForm()
    
    return render(request, 'analyzer/upload.html', {'form': form})
