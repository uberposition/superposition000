from pyicloud import PyiCloudService
from datetime import datetime, timedelta
from getpass import getpass
import time
import os

# Prompt for iCloud username and password
username = input("iCloud username: ")
password = getpass("iCloud password: ")

# Initialize iCloud service
api = PyiCloudService(username, password)

# Create a directory to save photos and videos
main_directory = "ExtractedMedia"
if not os.path.exists(main_directory):
    os.makedirs(main_directory)

# Create a new directory with the current date and timestamp
current_date_time = datetime.now().strftime("%y-%m-%d-%H%M%S")
new_directory = f"{main_directory}/ExtractedPhotosVideo{current_date_time}"

# Create the new directory
if not os.path.exists(new_directory):
    os.makedirs(new_directory)

# Handle 2FA
if api.requires_2fa:
    print("Two-factor authentication required.")
    code = input("Enter the code sent to your trusted device: ")
    result = api.validate_2fa_code(code)
    if result:
        print("2FA validated.")
    else:
        print("Could not verify 2FA code.")

# Fetch photos
print("Fetching photos from iCloud...")
photos = api.photos.all
total_photos = len(photos)
print(f"Total photos fetched: {total_photos}")

# Initialize counters
matched_count = 0
skipped_count = 0

# Calculate date for "today - 6 months"
six_months_ago = datetime.now() - timedelta(days=180)

# Main loop for photo processing
for photo in photos:
    photo_date = photo.created.replace(tzinfo=None)
    skipped_count += 1

    # Update the skipped_count dynamically in real-time
    print(f"\rSkipped {skipped_count} recent photos; ", end="")

    # Skip photos newer than "today - 6 months"
    if photo_date > six_months_ago:
        continue

    # Download and save photos older than "today - 6 months"
    while True:  # Retry mechanism
        try:
            photo_data = photo.download()
            if photo_data is not None:
                with open(f"{new_directory}/photo_{matched_count}.jpg", "wb") as f:
                    f.write(photo_data.content)

                # Validate download
                if os.path.exists(f"{new_directory}/photo_{matched_count}.jpg"):
                    # Delete photo from iCloud
                    photo.delete()
                    print(f"Downloaded {matched_count} photos from iCloud.")

                matched_count += 1  # Increment the matched_count
                break  # Exit retry loop
            else:
                print(f"Failed to download photo {matched_count}. Retrying.")
        except Exception as e:
            print(f"An error occurred: {e}. Retrying.")
            time.sleep(5)  # Wait for 5 seconds before retrying
