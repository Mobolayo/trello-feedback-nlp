"""
collect_reviews.py
Collects Google Play reviews for Trello and saves them to a CSV file.
"""

import time
import pandas as pd
from google_play_scraper import reviews, Sort

# ---------- Configuration ----------
APP_ID = "com.trello"
TARGET_REVIEWS = 5000
BATCH_SIZE = 200
LANG = "en"
COUNTRY = "us"
OUTPUT_FILE = "trello_reviews_raw.csv"


def collect_reviews():
    all_reviews = []
    token = None

    while len(all_reviews) < TARGET_REVIEWS:
        batch, token = reviews(
            APP_ID,
            lang=LANG,
            country=COUNTRY,
            sort=Sort.NEWEST,
            count=BATCH_SIZE,
            continuation_token=token,
        )

        if not batch:
            print("No more reviews returned; stopping.")
            break

        all_reviews.extend(batch)
        print(f"Collected {len(all_reviews)} reviews so far...")

        if token is None:
            print("Reached the end of available reviews.")
            break

        time.sleep(1)

    return all_reviews[:TARGET_REVIEWS]


def main():
    raw = collect_reviews()
    df = pd.DataFrame(raw)

    keep = {
        "reviewId": "review_id",
        "content": "review_text",
        "score": "rating",
        "at": "date",
        "thumbsUpCount": "helpful_count",
        "appVersion": "app_version",
        "replyContent": "developer_reply",
    }
    df = df[list(keep.keys())].rename(columns=keep)

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nSaved {len(df)} reviews to {OUTPUT_FILE}")
    print("\nPreview:")
    print(df.head())


if __name__ == "__main__":
    main()