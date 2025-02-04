import requests
import random
import time
from lxml import html
import pandas as pd

# Define the target URL
main_url = "https://tvtalkshow.ru/"

# List of User-Agents to rotate
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
]

# Set headers with a random User-Agent
custom_headers = {
    "User-Agent": random.choice(user_agents),
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://tvtalkshow.ru/",
    "Connection": "keep-alive"
}

# Create a session with headers
session = requests.Session()
session.headers.update(custom_headers)

# Introduce a random delay to avoid getting blocked
time.sleep(random.uniform(3, 7))

# Retry logic for fetching the main page
for attempt in range(3):  
    try:
        response = session.get(main_url, timeout=10)
        if response.status_code == 200:
            print(" Main page request successful")

            # Parse HTML content
            tree = html.fromstring(response.content)

            # Extract movie/TV show links
            movie_links = tree.xpath("//h3[contains(@class,'entry-title')]//a/@href")

            if not movie_links:
                print(" No movie links found.")
                break

            print(f" Found {len(movie_links)} movie links")

            movies_data = []  # List to store scraped data

            # Visit each movie page to extract details
            for idx, movie_url in enumerate(movie_links[:10]):  # Limit to first 10 movies for testing
                time.sleep(random.uniform(2, 5))  # Random delay to avoid detection

                for movie_attempt in range(3):  # Retry up to 3 times per movie
                    try:
                        movie_response = session.get(movie_url, timeout=10)

                        if movie_response.status_code == 200:
                            tree = html.fromstring(movie_response.content)

                            # Extract required details
                            title = tree.xpath("//h1[contains(@class,'entry-title')]/text()")
                            year = tree.xpath("(//article//time[contains(@class,'entry-date')]/@datetime)[1]")
                            description = tree.xpath("//div[contains(@class,'entry-content')]//text()")
                            poster_url = tree.xpath("//article[contains(@id,'post-')]/div[@class='post-thumbnail']/img/@src")

                            # Clean and format data
                            title = title[0].strip() if title else "N/A"
                            year = year[0] if year else "N/A"
                            # description = " ".join([d.strip() for d in description if d.strip()])[:500]  # Limit text size
                            description = " ".join([d.strip() for d in description if d.strip()]) # No length limit
                            poster_url = poster_url[0] if poster_url else "N/A"

                            # Store in dictionary
                            movies_data.append({
                                "Title": title,
                                "Year": year,
                                "Description": description,
                                "Poster URL": poster_url,
                                "Movie URL": movie_url
                            })

                            print(f"\n Movie {idx+1}: {title} ({year})")
                            print(f" Description: {description}...")  # Print partial description
                            print(f" Poster: {poster_url}")
                            print(f" URL: {movie_url}")

                            break  # Exit retry loop for this movie

                    except requests.exceptions.RequestException as e:
                        print(f" Retrying {movie_url} (Attempt {movie_attempt+1}) - Error: {e}")
                        time.sleep(3)  # Short delay before retrying
                        continue  # Retry fetching the movie URL

                else:
                    print(f" Skipping {movie_url} after 3 failed attempts.")

            # Save data to Excel
            if movies_data:
                try:
                    df = pd.DataFrame(movies_data)
                    df.to_excel("movies_data.xlsx", index=False)
                    print("\n Data saved to Excel file: movies_data.xlsx")
                except PermissionError:
                    print(" Error: Cannot save Excel file. Please close it if already open.")

            print(f"\n Successfully scraped {len(movies_data)} movies.")
            break  # Exit retry loop after success

    except requests.exceptions.ConnectionError as e:
        print(f" Connection Error on attempt {attempt+1}: {e}")
        time.sleep(5)  # Wait and retry
