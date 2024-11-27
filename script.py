import instaloader
import os
import sys
from typing import List, Optional

def download_instagram_posts(username: Optional[str] = None, 
                              post_links: Optional[List[str]] = None, 
                              max_posts: int = 100):
    """
    Download Instagram posts by username or list of post links.
    
    :param username: Instagram username (optional)
    :param post_links: List of Instagram post links (optional)
    :param max_posts: Maximum number of posts to download (default: 100)
    """
    # Initialize Instaloader with specific settings
    L = instaloader.Instaloader(
        download_pictures=True,         # Enable picture download
        download_videos=False,          # Disable video download
        download_video_thumbnails=False,# Disable video thumbnails
        download_comments=False,        # Disable comment download
        save_metadata=False             # Disable metadata saving
    )

    # Prompt for login credentials (REPLACE WITH YOUR OWN)
    username_login = "your_instagram_username"
    password_login = "your_instagram_password"

    # Login process
    try:
        L.login(username_login, password_login)
        print("Login successful!")
    except instaloader.exceptions.BadCredentialsException:
        print("Incorrect username or password.")
        return
    except instaloader.exceptions.ConnectionException as conn_error:
        print(f"Connection error: {conn_error}")
        return

    # Create download directory if it doesn't exist
    download_folder = 'instagram_downloads'
    os.makedirs(download_folder, exist_ok=True)

    try:
        # Download posts from a username
        if username:
            profile = instaloader.Profile.from_username(L.context, username)
            
            print(f"Downloading posts from account: {username}")
            
            for i, post in enumerate(profile.get_posts(), 1):
                if i > max_posts:
                    break
                
                try:
                    L.download_post(post, target=download_folder)
                    print(f"Downloaded post {i}: {post.shortcode}")
                except Exception as post_error:
                    print(f"Error downloading post {post.shortcode}: {post_error}")

        # Download posts from a list of links
        elif post_links:
            print("Downloading posts from link list...")
            for link in post_links:
                try:
                    shortcode = link.split('/')[-2] if '/p/' in link else link
                    
                    post = instaloader.Post.from_shortcode(L.context, shortcode)
                    L.download_post(post, target=download_folder)
                    print(f"Downloaded post: {shortcode}")
                except Exception as link_error:
                    print(f"Error downloading link {link}: {link_error}")

        else:
            print("Please provide a username or list of post links.")
            return

        print(f"Download complete. Check folder: {download_folder}")

    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    """
    Main function to run script from command line.
    """
    if len(sys.argv) > 1:
        if sys.argv[1].startswith('http'):
            download_instagram_posts(post_links=sys.argv[1:])
        else:
            download_instagram_posts(username=sys.argv[1])
    else:
        example_links = [
            'https://www.instagram.com/p/example1/',
            'https://www.instagram.com/p/example2/'
        ]
        download_instagram_posts(post_links=example_links)

if __name__ == "__main__":
    main()