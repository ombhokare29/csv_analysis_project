import pandas as pd
from django.shortcuts import render, redirect
from .forms import CSVUploadForm
import matplotlib.pyplot as plt
import seaborn as sns
import os
from django.conf import settings
from django.contrib import messages


# Store processed data temporarily
processed_data = {
    'summary': None,
    'head': None,
    'missing_values': None,
    'plot_url': None,
}

def upload_file(request):
    global processed_data
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            data = pd.read_csv(csv_file)

            summary = data.describe().to_html()
            head = data.head().to_html()
            missing_values = data.isnull().sum().to_frame(name='Missing Values').to_html()

            plt.figure(figsize=(10, 6))
            sns.histplot(data.select_dtypes(include='number').iloc[:, 0], kde=True)
            plot_path = os.path.join(settings.MEDIA_ROOT, 'plot.png')
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            plt.savefig(plot_path)

            processed_data = {
                'summary': summary,
                'head': head,
                'missing_values': missing_values,
                'plot_url': settings.MEDIA_URL + 'plot.png',
            }

            messages.success(request, 'File uploaded and processed successfully!')
            return redirect('results')
        else:
            messages.error(request, 'Failed to upload the file. Please try again.')
    else:
        form = CSVUploadForm()

    return render(request, 'analysis/upload.html', {'form': form})

def results(request):
    global processed_data
    if not processed_data['summary']:
        messages.warning(request, 'No data available. Please upload a CSV file first.')
        return redirect('upload_file')

    return render(request, 'analysis/result.html', {
        'summary': processed_data['summary'],
        'head': processed_data['head'],
        'missing_values': processed_data['missing_values'],
        'plot_url': processed_data['plot_url'],
    })
