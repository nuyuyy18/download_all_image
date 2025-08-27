## Download All Images Automatically with Python

A simple Python script to download multiple images at once using only two libraries:
--> os → handle folders & file paths
--> requests → fetch images from the web

## Why Use This?

↔️ Save time (no more right–click → save as)
↔️ Keep all images neatly in one folder
↔️ Works for dozens or hundreds of files
↔️ Easy to extend for bigger projects

🔍 How It Works

1. Make a folder: Before downloading, the script creates a directory called downloaded_images. If it already exists, Python skips this step.
2. List your images: Just copy and paste the URLs into the image_urls list. You can add as many as you like.
3. Download loop: The script uses requests.get() to grab each image, then saves it locally with a clean filename like image_1.jpg.
4. Error handling: If any URL is broken or the connection fails, the script won’t stop—it will simply log the error and continue with the next image.

✨ Notes

📝 Add more URLs in the image_urls list to scale.
📝 Script skips broken links and continues automatically.
📝 No extra dependencies needed beyond requests.

⚡ Quick, clean, and effective—let Python handle the downloads for you.