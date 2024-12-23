import tkinter as tk
from tkinter import messagebox
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import re

# Load data and train the model
data = pd.read_csv("data.csv")
data['input_text'] = data['song'] + " " + data['lyrics']
X = data['input_text']
y = data['artist']


pipeline = make_pipeline(
    CountVectorizer(stop_words='english'),
    MultinomialNB()
)
pipeline.fit(X, y)

def clean_lyrics(lyrics):
    """Remove all text inside square brackets, including nested and multiline brackets."""
    cleaned_lyrics = re.sub(r'\[.*?\]', '', lyrics, flags=re.DOTALL)
    return cleaned_lyrics

def predict_artist(song_name, lyrics):
    input_text = song_name + " " + lyrics
    prediction = pipeline.predict([input_text])
    return prediction[0]

def song_exists(song_name):
    """Check if the song already exists in the dataset."""
    return song_name in data['song'].values

def add_to_csv(song_name, lyrics, artist):
    """Adds the song, lyrics, and artist to the CSV file if not already exists."""
    global data
    
    if song_exists(song_name):
        messagebox.showwarning("Duplicate Song", f"The song '{song_name}' already exists in the dataset.")
        return
    
    new_entry = pd.DataFrame({
        'artist': [artist],
        'song': [song_name],
        'lyrics': [lyrics]
    })
    new_entry['input_text'] = new_entry['song'] + " " + new_entry['lyrics']
    
    # Append to a DataFrame and save to CSV
    data = pd.concat([data, new_entry], ignore_index=True)
    data.to_csv("data.csv", index=False)
    messagebox.showinfo("Success", "Song added to the dataset!")

# GUI
def get_prediction():
    song_name = song_name_entry.get()
    raw_lyrics = lyrics_text.get("1.0", tk.END).strip()

    if not song_name or not raw_lyrics:
        messagebox.showwarning("Input Error", "Please provide both song name and lyrics.")
        return

    # Clean the lyrics by removing [##]
    lyrics = clean_lyrics(raw_lyrics)

    predicted_artist = predict_artist(song_name, lyrics)
    result_label.config(text=f"{predicted_artist}")

    # Ask user if the prediction is correct
    is_correct = messagebox.askyesno("Prediction Check", f"Is it {predicted_artist}?")
    if is_correct:
        add_to_csv(song_name, lyrics, predicted_artist)

# Initialize the GUI app
app = tk.Tk()
app.title("Who's the Artist?")
app.geometry("400x500")

# Widgets
song_name_label = tk.Label(app, text="Song Name")
song_name_label.pack(pady=5)

song_name_entry = tk.Entry(app, width=40)
song_name_entry.pack(pady=5)

lyrics_label = tk.Label(app, text="Lyrics")
lyrics_label.pack(pady=5)

lyrics_text = tk.Text(app, height=15, width=40)
lyrics_text.pack(pady=5)

predict_button = tk.Button(app, text="Predict Artist", command=get_prediction)
predict_button.pack(pady=10)

result_label = tk.Label(app, text=" ", font=("Helvetica", 12))
result_label.pack(pady=20)

# Run the app
app.mainloop()