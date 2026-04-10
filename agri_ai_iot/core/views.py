# from django.shortcuts import render, redirect
# from .models import Farmer, SensorData, Prediction
# from .ml_model import predict

# def farmer_register(request):
#     if request.method == "POST":
#         Farmer.objects.create(
#             name=request.POST['name'],
#             email=request.POST['email'],
#             password=request.POST['password'],
#             phone=request.POST['phone'],
#             location=request.POST['location']
#         )
#         return redirect('farmer_login')
#     return render(request, 'farmer/register.html')
# def add_sensor_data(request):
#     if request.method == "POST":
#         farmer = Farmer.objects.get(id=request.session['farmer_id'])

#         sensor = SensorData.objects.create(
#             farmer=farmer,
#             soil_moisture=request.POST['soil_moisture'],
#             temperature=request.POST['temperature'],
#             humidity=request.POST['humidity'],
#             nitrogen=request.POST['nitrogen'],
#             phosphorus=request.POST['phosphorus'],
#             potassium=request.POST['potassium']
#         )

#         data_dict = {
#             'soil_moisture': float(sensor.soil_moisture),
#             'temperature': float(sensor.temperature),
#             'humidity': float(sensor.humidity),
#             'nitrogen': float(sensor.nitrogen),
#             'phosphorus': float(sensor.phosphorus),
#             'potassium': float(sensor.potassium),
#         }

#         yield_pred = predict(data_dict)

#         irrigation = "Yes" if sensor.soil_moisture < 40 else "No"
#         fertilizer = "Increase NPK" if sensor.nitrogen < 30 else "Optimal"

#         Prediction.objects.create(
#             farmer=farmer,
#             irrigation_required=irrigation,
#             fertilizer_recommendation=fertilizer,
#             yield_prediction=yield_pred
#         )

#         return redirect('view_prediction')

#     return render(request, 'farmer/add_sensor.html')
# def view_farmers(request):
#     farmers = Farmer.objects.all()
#     return render(request, 'admin/view_farmers.html', {'farmers': farmers})
# def view_sensor_data(request):
#     data = SensorData.objects.all()
#     return render(request, 'admin/view_sensor.html', {'data': data})
# import matplotlib.pyplot as plt
# import io
# import base64

# def farmer_dashboard(request):
#     farmer = Farmer.objects.get(id=request.session['farmer_id'])
#     data = SensorData.objects.filter(farmer=farmer)

#     soil = [d.soil_moisture for d in data]

#     plt.figure()
#     plt.plot(soil)
#     plt.title("Soil Moisture Trend")
#     plt.xlabel("Readings")
#     plt.ylabel("Moisture")

#     buffer = io.BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     buffer.close()

#     graph = base64.b64encode(image_png).decode('utf-8')

#     return render(request, 'farmer/dashboard.html', {'graph': graph})
# from django.http import JsonResponse
# import json

# def add_sensor_data(request):
#     if request.method == "POST":

#         farmer = Farmer.objects.get(id=request.session['farmer_id'])

#         # ✅ Convert ALL values to float
#         soil_moisture = float(request.POST['soil_moisture'])
#         temperature = float(request.POST['temperature'])
#         humidity = float(request.POST['humidity'])
#         nitrogen = float(request.POST['nitrogen'])
#         phosphorus = float(request.POST['phosphorus'])
#         potassium = float(request.POST['potassium'])

#         sensor = SensorData.objects.create(
#             farmer=farmer,
#             soil_moisture=soil_moisture,
#             temperature=temperature,
#             humidity=humidity,
#             nitrogen=nitrogen,
#             phosphorus=phosphorus,
#             potassium=potassium
#         )

#         data_dict = {
#             'soil_moisture': soil_moisture,
#             'temperature': temperature,
#             'humidity': humidity,
#             'nitrogen': nitrogen,
#             'phosphorus': phosphorus,
#             'potassium': potassium,
#         }

#         yield_pred = predict(data_dict)

#         # ✅ Now comparison works correctly
#         irrigation = "Yes" if soil_moisture < 40 else "No"
#         fertilizer = "Increase NPK" if nitrogen < 30 else "Optimal"

#         Prediction.objects.create(
#             farmer=farmer,
#             irrigation_required=irrigation,
#             fertilizer_recommendation=fertilizer,
#             yield_prediction=yield_pred
#         )

#         return redirect('view_prediction')

#     return render(request, 'farmer/add_sensor.html')
# def farmer_login(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']

#         try:
#             farmer = Farmer.objects.get(email=email, password=password)
#             request.session['farmer_id'] = farmer.id
#             return redirect('farmer_dashboard')
#         except:
#             return render(request, 'farmer/login.html', {'error': 'Invalid Credentials'})

#     return render(request, 'farmer/login.html')
# def farmer_logout(request):
#     request.session.flush()
#     return redirect('farmer_login')
# def view_prediction(request):
#     farmer = Farmer.objects.get(id=request.session['farmer_id'])
#     predictions = Prediction.objects.filter(farmer=farmer).order_by('-created_at')
#     return render(request, 'farmer/view_prediction.html', {'predictions': predictions})
# from django.shortcuts import render

# def admin_dashboard(request):
#     return render(request, 'admin/dashboard.html')
# import matplotlib.pyplot as plt
# import io
# import base64
# from .ml_model import get_feature_importance
# def feature_importance_view(request):

#     importance = get_feature_importance()

#     features = list(importance.keys())
#     values = list(importance.values())

#     plt.figure()
#     plt.bar(features, values)
#     plt.xticks(rotation=45)
#     plt.title("Feature Importance")
#     plt.tight_layout()

#     buffer = io.BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     buffer.close()

#     graph = base64.b64encode(image_png).decode('utf-8')

#     return render(request, 'admin/feature_importance.html', {'graph': graph})
# def train_model():
#     data = pd.read_csv(DATASET_PATH)

#     X = data[['soil_moisture','temperature','humidity','nitrogen','phosphorus','potassium']]
#     y = data['yield']

#     model = RandomForestRegressor()
#     model.fit(X, y)

#     joblib.dump(model, MODEL_PATH)
# def admin_login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         # Simple static admin login (for project demo)
#         if username == "admin@gmail.com" and password == "admin123":
#             request.session['admin_logged_in'] = True
#             return redirect('admin_dashboard')
#         else:
#             return render(request, 'admin/login.html', {'error': 'Invalid Admin Credentials'})

#     return render(request, 'admin/login.html')
# def admin_logout(request):
#     request.session.flush()
#     return redirect('admin_login')
# def admin_dashboard(request):
#     if not request.session.get('admin_logged_in'):
#         return redirect('admin_login')

#     return render(request, 'admin/dashboard.html')
# from .ml_model import train_model
# import matplotlib.pyplot as plt
# import io
# import base64
# import numpy as np

# def algorithm_results(request):

#     if not request.session.get('admin_logged_in'):
#         return redirect('admin_login')

#     accuracy, cm = train_model()

#     # Plot Confusion Matrix
#     plt.figure()
#     plt.imshow(cm, interpolation='nearest')
#     plt.title("Confusion Matrix")
#     plt.colorbar()

#     classes = ['Low Yield', 'High Yield']
#     tick_marks = np.arange(len(classes))
#     plt.xticks(tick_marks, classes, rotation=45)
#     plt.yticks(tick_marks, classes)

#     plt.xlabel('Predicted')
#     plt.ylabel('Actual')

#     buffer = io.BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     buffer.close()

#     graph = base64.b64encode(image_png).decode('utf-8')

#     return render(request, 'admin/algorithm_results.html', {
#         'accuracy': round(accuracy*100,2),
#         'graph': graph
#     })

# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# import json


# @csrf_exempt
# def arduino_api(request):

#     if request.method == "POST":

#         data = json.loads(request.body)

#         # get first farmer automatically
#         farmer, created = Farmer.objects.get_or_create(
#             name="Default Farmer",
#             email="default@gmail.com",
#             password="123",
#             phone="0000000000",
#             location="Field"
#         )

#         soil = float(data["soil_moisture"])
#         temperature = float(data["temperature"])
#         humidity = float(data["humidity"])
#         nitrogen = float(data["nitrogen"])
#         phosphorus = float(data["phosphorus"])
#         potassium = float(data["potassium"])

#         SensorData.objects.create(
#             farmer=farmer,
#             soil_moisture=soil,
#             temperature=temperature,
#             humidity=humidity,
#             nitrogen=nitrogen,
#             phosphorus=phosphorus,
#             potassium=potassium
#         )

#         data_dict = {
#             "soil_moisture": soil,
#             "temperature": temperature,
#             "humidity": humidity,
#             "nitrogen": nitrogen,
#             "phosphorus": phosphorus,
#             "potassium": potassium,
#         }

#         yield_pred = predict(data_dict)

#         irrigation = "Yes" if soil < 40 else "No"
#         fertilizer = "Increase NPK" if nitrogen < 30 else "Optimal"

#         Prediction.objects.create(
#             farmer=farmer,
#             irrigation_required=irrigation,
#             fertilizer_recommendation=fertilizer,
#             yield_prediction=yield_pred
#         )

#         return JsonResponse({"status": "success"})
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Farmer, SensorData, Prediction
from .ml_model import predict, get_feature_importance, train_model
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import json
import numpy as np


# ---------------- DASHBOARD ---------------- #

def farmer_dashboard(request):
    farmer = Farmer.objects.first()
    data = SensorData.objects.filter(farmer=farmer)

    soil = [d.soil_moisture for d in data]

    plt.figure()
    plt.plot(soil)
    plt.title("Soil Moisture Trend")
    plt.xlabel("Readings")
    plt.ylabel("Moisture")

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graph = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'farmer/dashboard.html', {'graph': graph})


# ---------------- VIEW PREDICTION ---------------- #

def view_prediction(request):
    farmer = Farmer.objects.first()
    predictions = Prediction.objects.filter(farmer=farmer).order_by('-created_at')
    return render(request, 'farmer/view_prediction.html', {'predictions': predictions})


# ---------------- ADMIN DASHBOARD ---------------- #

def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


# ---------------- FEATURE IMPORTANCE ---------------- #

def feature_importance_view(request):

    importance = get_feature_importance()

    features = list(importance.keys())
    values = list(importance.values())

    plt.figure()
    plt.bar(features, values)
    plt.xticks(rotation=45)
    plt.title("Feature Importance")
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graph = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'admin/feature_importance.html', {'graph': graph})


# ---------------- ARDUINO API ---------------- #

@csrf_exempt
def arduino_api(request):

    if request.method == "POST":

        data = json.loads(request.body)

        farmer, created = Farmer.objects.get_or_create(
            name="Default Farmer",
            email="default@gmail.com",
            password="123",
            phone="0000000000",
            location="Field"
        )

        soil = float(data["soil_moisture"])
        temperature = float(data["temperature"])
        humidity = float(data["humidity"])
        nitrogen = float(data["nitrogen"])
        phosphorus = float(data["phosphorus"])
        potassium = float(data["potassium"])

        SensorData.objects.create(
            farmer=farmer,
            soil_moisture=soil,
            temperature=temperature,
            humidity=humidity,
            nitrogen=nitrogen,
            phosphorus=phosphorus,
            potassium=potassium
        )

        data_dict = {
            "soil_moisture": soil,
            "temperature": temperature,
            "humidity": humidity,
            "nitrogen": nitrogen,
            "phosphorus": phosphorus,
            "potassium": potassium,
        }

        yield_pred = predict(data_dict)

        irrigation = "Yes" if soil < 40 else "No"
        fertilizer = "Increase NPK" if nitrogen < 30 else "Optimal"

        Prediction.objects.create(
            farmer=farmer,
            irrigation_required=irrigation,
            fertilizer_recommendation=fertilizer,
            yield_prediction=yield_pred
        )

        return JsonResponse({"status": "success", "prediction": yield_pred})

    return JsonResponse({"status": "invalid request"})


# ---------------- ADD SENSOR PAGE ---------------- #

def add_sensor(request):

    if request.method == "POST":

        farmer, created = Farmer.objects.get_or_create(
            name="Default Farmer",
            email="default@gmail.com",
            password="123",
            phone="0000000000",
            location="Field"
        )

        soil = float(request.POST['soil_moisture'])
        temperature = float(request.POST['temperature'])
        humidity = float(request.POST['humidity'])
        nitrogen = float(request.POST['nitrogen'])
        phosphorus = float(request.POST['phosphorus'])
        potassium = float(request.POST['potassium'])

        SensorData.objects.create(
            farmer=farmer,
            soil_moisture=soil,
            temperature=temperature,
            humidity=humidity,
            nitrogen=nitrogen,
            phosphorus=phosphorus,
            potassium=potassium
        )

        data_dict = {
            "soil_moisture": soil,
            "temperature": temperature,
            "humidity": humidity,
            "nitrogen": nitrogen,
            "phosphorus": phosphorus,
            "potassium": potassium,
        }

        yield_pred = predict(data_dict)

        irrigation = "Yes" if soil < 40 else "No"
        fertilizer = "Increase NPK" if nitrogen < 30 else "Optimal"

        Prediction.objects.create(
            farmer=farmer,
            irrigation_required=irrigation,
            fertilizer_recommendation=fertilizer,
            yield_prediction=yield_pred
        )

        return redirect('view_prediction')

    return render(request, 'farmer/add_sensor.html')


# ---------------- ADMIN FUNCTIONS ---------------- #

def view_farmers(request):
    farmers = Farmer.objects.all()
    return render(request, 'admin/view_farmers.html', {'farmers': farmers})


def view_sensor_data(request):
    data = SensorData.objects.all()
    return render(request, 'admin/view_sensor.html', {'data': data})


def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if username == "admin" and password == "admin123":
            request.session['admin_logged_in'] = True
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin/login.html', {'error': 'Invalid credentials'})

    return render(request, 'admin/login.html')


def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')


# ---------------- ALGORITHM RESULTS ---------------- #

def algorithm_results(request):

    accuracy, cm = train_model()

    plt.figure()
    plt.imshow(cm, interpolation='nearest')
    plt.title("Confusion Matrix")
    plt.colorbar()

    classes = ['Low Yield', 'High Yield']
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    plt.xlabel('Predicted')
    plt.ylabel('Actual')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graph = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'admin/algorithm_results.html', {
        'accuracy': round(accuracy * 100, 2),
        'graph': graph
    })