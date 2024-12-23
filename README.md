# Who Sang It?

# 🎤 Who Sang It? 
**Who Sang It?** is an AI-powered app that predicts the artist of a song based on its lyrics. This project combines data science, machine learning, and a user-friendly GUI to deliver a fun and interactive experience.  

---

## 🛠 Features  
- **Artist Prediction**: Identifies the artist (Michael Jackson, Kendrick Lamar, or Bob Marley) based on song lyrics.  
- **Clean Dataset**: Preprocessed dataset of 150 songs with extra tags like `[Intro]`, `[Chorus]`, and `[Verse]` removed.  
- **Duplicate Prevention**: Ensures no duplicate songs are added to the dataset.  
- **Interactive GUI**: Users can input song lyrics and get real-time predictions, with options to contribute new data.  

---

## 📂 Project Structure  
- **`data.csv`**: Preprocessed dataset of 150 songs.  
- **`model.py`**: Core script for training the model and running the GUI app.  
- **`notebook.ipynb`**: Jupyter Notebook for model development and performance analysis.  
- **`README.md`**: Project documentation (this file).  

---

## 🚀 How It Works  
1. **Dataset Creation**:  
   - Lyrics for the top 50 songs from Michael Jackson, Kendrick Lamar, and Bob Marley were scraped and cleaned.  
   - Preprocessing removed tags like `[Intro]`, `[Chorus]`, etc.  

2. **Model Training**:  
   - Used **CountVectorizer** for text vectorization and a **Naive Bayes Classifier** for predictions.  
   - Evaluated performance with a confusion matrix and classification report.  

3. **User Interaction**:  
   - Developed a **Tkinter GUI** for real-time artist prediction.  
   - Integrated features to add new songs and prevent duplicates in the dataset.
  
   ---

## 📦 Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Ahmad-Ramy20/Who-Sang-It-.git
   cd Who-Sang-It-

---

 ## 📊 Results
The model achieves high accuracy in distinguishing artists based on lyrics. Check the confusion matrix and classification report for details.

---

 ## 🤔 Future Work
Expand the dataset to include more artists and genres.
Enhance the model with advanced NLP techniques like TF-IDF or transformer-based models.
Improve GUI design for better user experience.

---

## 💻 Contributing
Contributions are welcome! Please open an issue or submit a pull request for suggestions and fixes.

---

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🙌 Acknowledgments
- Lyrics data sourced from the generous contributors of [[Genius](https://genius.com/)].
- Inspiration from the unique lyrical styles of Michael Jackson, Kendrick Lamar, and Bob Marley.
