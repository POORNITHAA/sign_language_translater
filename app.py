import os
from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

def find_image(path_without_ext):
    """Check PNG first, then JPG"""
    png = path_without_ext + ".png"
    jpg = path_without_ext + ".jpg"

    if os.path.exists(os.path.join("static", png)):
        return png
    elif os.path.exists(os.path.join("static", jpg)):
        return jpg
    return None


@app.route("/", methods=["GET", "POST"])
def index():
    images = []
    translated_text = ""

    if request.method == "POST":
        text = request.form["text"]
        translated = translator.translate(text, dest="en")
        translated_text = translated.text.upper()

        words = translated_text.split()

        for word in words:
            # 🟢 1. Try GENERAL WORD sign
            word_img = find_image(f"isl/words/{word.lower()}")
            if word_img:
                images.append(word_img)
                continue

            # 🟡 2. Else fallback to letters & numbers
            for char in word:
                if char.isalpha():
                    img = find_image(f"isl/alphabets/{char}1")
                    if img:
                        images.append(img)
                elif char.isdigit():
                    img = find_image(f"isl/numbers/{char}")
                    if img:
                        images.append(img)

    return render_template(
        "index.html",
        images=images,
        translated_text=translated_text
    )


if __name__ == "__main__":
    app.run(debug=True)