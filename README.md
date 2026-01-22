<h1 align="center">Malaria Cell Classification using CNN 🦟</h1>

<p align="center">
  <strong>A robust Deep Learning solution to detect Malaria in blood smear images.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/TensorFlow-2.0+-FF6F00?style=flat&logo=tensorflow&logoColor=white" alt="TensorFlow" />
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License" />
</p>

<br>

<h2>🔍 Overview</h2>

<p>
  Diagnosing malaria manually requires an expert to examine blood smears under a microscope, which is time-consuming and error-prone. This project automates that process using a <strong>Convolutional Neural Network (CNN)</strong>.
</p>

<p>
  What makes this model different is that it wasn't just trained on clean data. I specifically trained and tested it against common image degradations (blur, defocus, noise) to ensure it remains accurate even when image quality drops.
</p>

<br>

<h2 align="center">🛠️ Tech Stack</h2>
<p align="center">
  <a href="https://www.python.org/">Python</a> &nbsp;&bull;&nbsp;
  <a href="https://www.tensorflow.org/">TensorFlow/Keras</a> &nbsp;&bull;&nbsp;
  <a href="https://streamlit.io/">Streamlit</a> &nbsp;&bull;&nbsp;
  <a href="https://opencv.org/">OpenCV</a>
</p>

<br>

<h2>✨ Key Features</h2>
<ul>
  <li><strong>Binary Classification:</strong> Distinguishes between "Parasitized" (Infected) and "Uninfected" cells.</li>
  <li><strong>Robustness:</strong> Handles blurry or low-quality images better than standard models.</li>
  <li><strong>Web Interface:</strong> Upload an image and get an instant prediction with confidence score.</li>
</ul>

<br>

<h2>🚀 Getting Started</h2>

<p>Follow these steps to run the project locally on your machine.</p>

<h3>1. Clone the repository</h3>
<pre>
git clone https://github.com/sankalp6115/Malaria-Prediction-using-CNN
cd malaria-prediction-cnn
</pre>

<h3>2. Install dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>3. Run the Streamlit App</h3>
<pre>
streamlit run app.py
</pre>

<p>
  This will open a local server (usually at <code>http://localhost:8501</code>) where you can upload cell images to test the model.
</p>

<br>

<h2>🧠 How it Works</h2>
<ol>
  <li><strong>Input:</strong> The model takes in a standard <code>.png</code> or <code>.jpg</code> of a single cell.</li>
  <li><strong>Preprocessing:</strong> The image is resized and normalized to match the training constraints.</li>
  <li><strong>Prediction:</strong> The CNN analyzes the texture (looking for the parasite's "ring" shape).</li>
  <li><strong>Result:</strong> Displays <strong>Infected</strong> or <strong>Uninfected</strong>.</li>
</ol>

<br>

<hr>
<p align="center">
  Made with ❤️ by <a href="https://github.com/sankalp6115">Your Name</a>
</p>