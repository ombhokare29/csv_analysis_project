import pandas as pd
from django.shortcuts import render
from .forms import CSVUploadForm
import matplotlib.pyplot as plt
import seaborn as sns
import os
from django.conf import settings
from django.contrib import messages


def upload_file(request):
    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            data = pd.read_csv(csv_file)

            # Data Analysis
            summary = data.describe().to_html()
            head = data.head().to_html()
            missing_values = data.isnull().sum().to_frame(name='Missing Values').to_html()


            # Generate Visualization
            plt.figure(figsize=(10, 6))
            sns.histplot(data.select_dtypes(include='number').iloc[:, 0], kde=True)
            plot_path = os.path.join(settings.MEDIA_ROOT, 'plot.png')
            plt.savefig(plot_path)

            messages.success(request, 'File uploaded and processed successfully!')

            return render(request, 'analysis/result.html', {
                'summary': summary,
                'head': head,
                'missing_values': missing_values,
                'plot_url': settings.MEDIA_URL + 'plot.png'
            })
    else:
        form = CSVUploadForm()
    return render(request, 'analysis/upload.html', {'form': form})
