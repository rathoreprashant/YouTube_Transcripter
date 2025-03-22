### ✅`README.md`

```markdown
# YouTube Audio Downloader & Compressor API (FastAPI + Google Cloud Run)

This API accepts a YouTube video URL, downloads the audio, compresses it using `ffmpeg`, and returns a downloadable MP3 file.

---

## 📌 API Endpoint

**GET** `/download`

### Query Parameters:
- `url` – Full YouTube video URL

### Example:
```bash
curl -L "https://your-service-url.a.run.app/download?url=https://www.youtube.com/watch?v=KShDB169KP4" --output audio.mp3
```

---

## 🛠 Technologies Used

- FastAPI
- yt-dlp
- ffmpeg
- Uvicorn
- Google Cloud Run
- Docker

---

## 📦 Project Structure

```
.
├── app.py              # Main FastAPI app
├── Dockerfile          # Container config
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## 🚀 How to Run Locally

### ✅ Step 1: Install ffmpeg and ffprobe

Make sure `ffmpeg` and `ffprobe` are installed on your system.

#### On Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg -y
```

#### On macOS (using Homebrew):
```bash
brew install ffmpeg
```

#### On Windows:
Download from: https://ffmpeg.org/download.html  
Add `ffmpeg/bin` to your system PATH.

---

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/YouTube_Transcripter.git
cd YouTube_Transcripter
```

### Step 3: (Optional) Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the App

```bash
uvicorn app:app --host 0.0.0.0 --port 8080
```

### Step 6: Access the API Locally

```bash
curl -L "http://localhost:8080/download?url=https://www.youtube.com/watch?v=KShDB169KP4" --output audio.mp3
```
```
---

## 🚀 How to Deploy on Google Cloud Run

### 1. Build Docker Image

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/youtube-api
```

### 2. Deploy to Cloud Run

```bash
gcloud run deploy youtube-api \
  --image gcr.io/YOUR_PROJECT_ID/youtube-api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```
Or
```bash
gcloud run deploy youtube-api --image gcr.io/my-project-ag-to-ghl-for-ut/youtube-api --platform managed --region us-central1 --allow-unauthenticated
```

### 3. Use the API

After deployment, Google will provide a public URL:

```bash
curl -L "https://your-service-url.a.run.app/download?url=https://www.youtube.com/watch?v=KShDB169KP4" --output audio.mp3
```
#Response
``bash
[
    {
        "statusCode": 200,
        "data": "IMTBuffer(10295277, binary, adc6e9ccb3fdfeb734cc3e2297d4c2e5c6cfb292): 49443304000000000023545353450000000f0000034c61766635392e32372e3130300000000000000000000000fffb54000000000000000000000000000000000000000000000000000000000000000000496e666f0000000f0000d174009d17c0000306",
        "fileSize": 10295277
    }
]
```
## ✅ Status
Live and ready to use via any HTTP client (e.g., Curl, Postman, Python requests).
```
