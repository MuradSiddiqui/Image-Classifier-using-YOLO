# YOLO-based Image Classifier

Welcome to the YOLO-based Image Classifier project! This project uses the YOLO (You Only Look Once) algorithm for real-time object detection and classification.

## Features

- **Real-Time Detection:** Fast and efficient object detection in real-time.
- **High Accuracy:** Utilizes the YOLO algorithm known for its accuracy and speed.
- **Multiple Object Classes:** Capable of detecting and classifying multiple object classes.
- **Easy to Use:** Simple interface for loading images and viewing results.

## Installation

To run this image classifier, you need to have Python and the necessary libraries installed on your machine. Follow the steps below to set up the project:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/MuradSiddiqui/yolo-image-classifier.git
    cd yolo-image-classifier
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download the YOLO weights:**
    Download the pre-trained YOLO weights (e.g., YOLOv3, YOLOv4) and place them in the `weights` directory.
    ```bash
    mkdir weights
    # Download the weights and place them in the weights directory
    ```

## Running the Classifier

Once the setup is complete, you can start the classifier by running:

```bash
python main.py --image path/to/your/image.jpg


How It Works
Loading the Model: The YOLO model is loaded with pre-trained weights.
Preprocessing: The input image is preprocessed to fit the model's requirements.
Detection: The YOLO model detects objects in the image and classifies them.
Postprocessing: The results are processed to draw bounding boxes and labels on the image.

Examples
Here are some examples of the image classifier in action:
![image](https://github.com/MuradSiddiqui/Image-Classifier-using-YOLO/assets/109691430/54a0d912-6c47-4bbf-a6ce-e65eb7c3b905)


Credits
This project uses code from the AlexeyAB/darknet repository. A huge thanks to AlexeyAB and the contributors for their incredible work on the YOLO implementation.
