import yt_dlp
import os

def list_formats(info_dict):
    """List available formats for the video."""
    formats = info_dict.get('formats', [info_dict])
    format_list = []
    for f in formats:
        if f.get('resolution'):
            format_list.append(f"{f['format_id']}: {f['resolution']} ({f['ext']})")
    return format_list

def download_video(url, format_id, save_path):
    """Download the video with the specified format and save it to the given path."""
    ydl_opts = {
        'format': format_id,
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            print(f"Title: {info_dict['title']}")
            print(f"Author: {info_dict['uploader']}")

            print(f"Downloading {info_dict['title']} in {format_id}...")
            ydl.download([url])
            print(f"Video downloaded successfully to: {os.path.join(save_path, info_dict['title'])}.{info_dict['ext']}")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Input YouTube URL
    url = input("Enter the YouTube video URL: ")

    # Get available formats
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = list_formats(info_dict)

    print("Available formats:")
    for i, fmt in enumerate(formats, start=1):
        print(f"{i}. {fmt}")

    # Let the user choose a format
    choice = int(input("Select the format by number: "))
    if choice < 1 or choice > len(formats):
        print("Invalid choice!")
        return

    selected_format = formats[choice - 1].split(':')[0]

    # Input save path
    save_path = input("Enter the directory to save the video (leave blank for current directory): ").strip()
    if not save_path:
        save_path = os.getcwd()  # Use current directory if no path is provided

    # Download the video
    download_video(url, selected_format, save_path)

if __name__ == "__main__":
    main()