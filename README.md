# 🖐️ Hand Gesture Recognition Using CNN

A Deep Learning project that uses a **Convolutional Neural Network (CNN)** to recognize different hand gestures from images.

This project was developed as **Task 4 of my SkillCraft Technology Internship**, where the objective was to build a hand gesture recognition model using Deep Learning and deploy it as an interactive application.

The model is trained on the **LeapGestureRecog dataset** containing **10 different hand gesture classes**, with approximately **2,000 images per class**.

The trained CNN model is integrated with a **Streamlit web application**, allowing users to upload an image and get the predicted hand gesture.

---

## 💼 Internship Task

**Internship:** SkillCraft Technology Internship

**Task:** Task 4 – Hand Gesture Recognition

**Domain:** Machine Learning / Deep Learning

**Objective:** Build a Deep Learning model capable of recognizing different hand gestures from images and integrate the trained model into an interactive application.

---

## 🔗 Project Links

* 🐙 **GitHub Repository:** https://github.com/Lohith-CSE-AIML/SCT_ML_4
* 🚀 **Live Demo:** https://sctml4-kryzcw47ciyhxsbscck7vs.streamlit.app/

---

## 🎯 Objectives

The main objectives of this project are:

* To understand image classification using Deep Learning.
* To learn how Convolutional Neural Networks work with image data.
* To preprocess grayscale hand gesture images for CNN training.
* To train a multi-class image classification model.
* To evaluate the trained model using test data.
* To deploy the trained model using Streamlit.
* To provide a simple interface for predicting hand gestures from uploaded images.

---

## 📊 Dataset

This project uses the **LeapGestureRecog dataset**.

The dataset contains **10 different hand gesture classes**, with approximately **2,000 images in each class**.

### Gesture Classes

| Class | Gesture    |
| ----- | ---------- |
| 01    | Palm       |
| 02    | L          |
| 03    | Fist       |
| 04    | Fist Moved |
| 05    | Thumb      |
| 06    | Index      |
| 07    | OK         |
| 08    | Palm Moved |
| 09    | C          |
| 10    | Down       |

The dataset contains approximately **20,000 images in total**.

> **Note:** The complete dataset is not included in this GitHub repository because of its large size.

---

## 🧹 Image Preprocessing

Before training the CNN model, the images were preprocessed to make them suitable for the neural network.

The preprocessing steps include:

* Loading the images.
* Converting the images to grayscale.
* Resizing the images to **128 × 128 pixels**.
* Normalizing pixel values.
* Adding the required channel dimension for CNN input.
* Splitting the dataset into training and testing sets.

### Input Shape

```text
128 × 128 × 1
```

The `1` represents the single grayscale channel.

---

## 🧠 CNN Model

A **Convolutional Neural Network (CNN)** was used for hand gesture classification.

The CNN learns visual features from the images automatically, such as:

* Edges
* Shapes
* Finger patterns
* Hand orientation
* Gesture-specific structures

The general architecture consists of:

```text
Input Image
     ↓
Convolution Layer
     ↓
Activation Function
     ↓
Pooling Layer
     ↓
Convolution Layer
     ↓
Activation Function
     ↓
Pooling Layer
     ↓
Flatten
     ↓
Dense Layer
     ↓
Output Layer
     ↓
10 Gesture Classes
```

The final output layer produces predictions for the **10 gesture classes**.

---

## 🏋️ Model Training

The model was trained using the training portion of the dataset.

The dataset was divided into:

```text
Training Images : 1,600 images per class
Testing Images  :   400 images per class
```

Therefore:

```text
Training Set : 16,000 images
Testing Set  :  4,000 images
```

The model was trained using **TensorFlow/Keras**.

---

## 📈 Model Performance

The trained CNN achieved the following performance on the test dataset:

### Test Accuracy

```text
92.60%
```

### Test Loss

```text
0.2062
```

The model was able to correctly classify the majority of unseen test images across the 10 gesture classes.

---

## 🌐 Streamlit Application

The trained model is integrated into a Streamlit web application.

Users can:

1. Open the web application.
2. Upload a hand gesture image.
3. The image is preprocessed automatically.
4. The trained CNN model analyzes the image.
5. The application displays the predicted gesture.

### Live Application

🚀 **Live Demo:** https://sctml4-kryzcw47ciyhxsbscck7vs.streamlit.app/

---

## 📸 Screenshots

### Streamlit Application

<img width="881" height="838" alt="Screenshot 2026-08-28 175412" src="https://github.com/user-attachments/assets/e64aed45-c9e7-4a70-885b-46cc1e2b3951" />




> **Note:** The screenshots are included to demonstrate the deployed application, prediction interface, and GitHub repository.

---

## 🚀 How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Lohith-CSE-AIML/SCT_ML_4.git
```

### 2. Navigate to the Project Folder

```bash
cd SCT_ML_4
```

### 3. Create a Virtual Environment

```bash
python -m venv hand_gesture
```

### 4. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.\hand_gesture\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📁 Project Structure

```text
SCT_ML_4/
│
├── app.py
├── hand_gesture_model.keras
├── hand_gesture_recognition.ipynb
├── requirements.txt
├── runtime.txt
├── .gitignore
└── screenshots/
    ├── streamlit_app.png
   
```

---

## ⚠️ Important Testing Note

The model was trained using images from the **LeapGestureRecog dataset**.

For better predictions, test the application using images that are **similar in appearance to the training dataset**, including:

* Similar hand positioning
* Similar background
* Similar lighting conditions
* Similar image orientation
* A clearly visible hand gesture

Images that are significantly different from the training data may result in incorrect predictions.

This is an important limitation of the current model and demonstrates why the diversity of training data is important in image classification.

---

## 🔮 Future Improvements

Some possible improvements for this project include:

* Using data augmentation to improve model generalization.
* Adding more diverse hand gesture images.
* Testing with real-time camera input.
* Using transfer learning with pretrained CNN models.
* Improving performance on different backgrounds and lighting conditions.
* Adding confidence scores for predictions.
* Expanding the number of recognizable gestures.

---

## 🛠️ Technologies Used

* **Python**
* **TensorFlow**
* **Keras**
* **NumPy**
* **Pillow**
* **Streamlit**
* **Jupyter Notebook**
* **Git & GitHub**

---

## 📚 What I Learned

Through this internship task, I learned:

* How images are represented as numerical data.
* How grayscale images are processed for CNNs.
* The basic working of convolution and pooling layers.
* How CNNs extract features from images.
* How to prepare image datasets for training.
* How to train a multi-class CNN classifier.
* How to evaluate a Deep Learning model.
* How to save and load a trained Keras model.
* How to build a Streamlit interface for a trained model.
* How to deploy a Machine Learning application.
* How to manage a project using Git and GitHub.

---

## 👨‍💻 Author

**Lohith**

B.Tech Computer Science and Engineering (AIML)

---

## 🙏 Acknowledgement

This project was completed as **Task 4 of my SkillCraft Technology Internship**.

I would like to thank **SkillCraft Technology** for providing the opportunity to work on practical Machine Learning and Deep Learning tasks and gain hands-on experience in **CNN-based image classification, model development, deployment, and GitHub project management**.

---

## ⭐ If You Like This Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

🐙 **GitHub:** https://github.com/Lohith-CSE-AIML/SCT_ML_4

🚀 **Live Demo:** https://sctml4-kryzcw47ciyhxsbscck7vs.streamlit.app/
