# Garbage Classification Dashboard

## Description
This Django-based web application provides a real-time dashboard for classifying and monitoring garbage as flammable or non-flammable. It utilizes a deep learning model for image classification and displays live statistics on the web interface.

## Features
- Real-time garbage image capture using a webcam interface.
- Image classification into flammable and non-flammable categories.
- Live dashboard updates with total captures, flammable count, and non-flammable count.
- Responsive web design for various devices.

## Installation
To set up the project locally, follow these steps:

1. **Clone the Repository**
```
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

2. **Set Up a Virtual Environment** (Optional but recommended)
```
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

3. **Install Dependencies**
```
pip install -r requirements.txt
```

4. **Initialize Database**

```
python manage.py makemigrations
python manage.py migrate
```


5. **Run the Development Server**
```
python manage.py runserver
```

The application will be available at `http://localhost:8000`.

## Usage
- Navigate to `http://localhost:8000` in your web browser.
- Allow webcam access to the web application.
- Use the `Capture & Upload` button to take a picture of the garbage and classify it.
- View the real-time updates on the dashboard.

## Contributing
Contributions to this project are welcome. Here are some ways you can contribute:
- Reporting bugs
- Suggesting enhancements
- Submitting pull requests

## License
[MIT License](LICENSE)

