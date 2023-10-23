from flask import Flask, request, render_template
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def download_video():
    if request.method == 'POST':
        url = request.form['url']
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        # stream.download('downloads/')
        # return send_file(f'downloads/{yt.title}.mp4', as_attachment=True)

        """method2"""

        save_path = 'C:/Users/DELL/Downloads'
        stream.download(output_path=save_path)
        print(f"Video '{yt.title}' has been downloaded to {save_path}")

    return render_template('home.html')

    

if __name__ == '__main__':
    app.run(debug=True)







