# Instagram Post Downloader
- WARNING: PLEASE CAREFULLY TO USE THE APP, BECAUSE IT CAN MAKE YOU LOCK YOUR ACCOUNT (TEST with 150 posts and the IG was warning my account)
## Description
A Python script to download Instagram posts by username or specific post links using the Instaloader library.


https://github.com/user-attachments/assets/da4e503d-c6d3-42e6-a3cf-b551dcd2edec



## Features
- Download posts from a specific Instagram username
- Download posts using direct links
- Configurable maximum number of posts
- Simple command-line interface

## Prerequisites
- Python 3.8+
- Instagram account

## Installation

1. Clone the repository:
```bash
git clone https://github.com/thepKz/instragram-image-downloader.git
cd instragram-image-downloader
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
⚠️ **Important Security Note**: 
Never commit your actual Instagram credentials to version control. Replace placeholders in the script with your own credentials.

## Usage

### Method 1: Download by Username
```bash
python script.py username
```
Replace `username` with the target Instagram account.

### Method 2: Download by Post Links
```bash
python script.py https://instagram.com/p/post1 https://instagram.com/p/post2
```

### Method 3: Direct Script Modification
Edit the script directly to set:
- `username_login`: Your Instagram username
- `password_login`: Your Instagram password
- Modify `max_posts` to limit downloads
- Customize `download_folder` path

## Limitations
- Requires active Instagram login
- Does not download private accounts unless your account follows them
- Limited by Instagram's API restrictions

## Legal and Ethical Use
- Respect Instagram's Terms of Service
- Only download content you have permission to access
- This tool is for personal and educational purposes

## Troubleshooting
- Ensure you have a stable internet connection
- Check your Instagram login credentials
- Verify you have the latest version of dependencies

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer
This script is provided "as is" without warranty of any kind. Use at your own risk. 

Additionally, it can be used for private accounts if your account follows them, and the script to run is `script.py`.
