from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.


def index(request):
    return render(request, 'startpage.html')

@api_view(['POST'])
def get_report(request):
    if request.method == 'POST':
        report_id = request.data.get('report_id')
        scientist_id = request.data.get('scientist_id')
        absolut_path = request.data.get('absolut_path')

        try:
            report = Report.objects.get(id=report_id)
            scientist = Scientist.objects.get(id=scientist_id)
            received_report = ReceivedReport(report=report, scientist=scientist, absolut_path=absolut_path)
            received_report.save()
            return Response({'message': 'Received report saved successfully'})
        except Report.DoesNotExist:
            return Response({'error': 'Report with id {} does not exist'.format(report_id)}, status=400)
        except Scientist.DoesNotExist:
            return Response({'error': 'Scientist with id {} does not exist'.format(scientist_id)}, status=400)
    else:
        return Response({'error': 'Invalid request method'}, status=405)