import matplotlib.pyplot as plt
import pandas as pd

# 1. Expanded and Populated Data
data = {
    "Movie/Show": [
        "The Vampire Diaries",
        "Stranger Things",
        "The Penthouse",
        "Off Campus",
        "Celebrity",
        "Juvenile Justice",
        "Manifest",
        "The Glory",
        "Parasyte: The Grey",
        "A Good Girl's Guide to Murder",
        "Mask Girl",
        "If Wishes Could Kill",
        "Never Have I Ever",
    ],
    "IMDb Rating": [7.7, 8.7, 7.9, 7.9, 7.4, 8.0, 7.1, 8.1, 7.1, 6.8, 7.3, 7.5, 7.9],
    "Genre": [
        "Supernatural Drama",
        "Sci-Fi Horror",
        "Revenge Thriller",
        "Romance Sport",
        "Mystery Drama",
        "Legal Drama",
        "Sci-Fi Mystery",
        "Revenge Thriller",
        "Sci-Fi Horror",
        "Mystery Thriller",
        "Dark Comedy Thriller",
        "Supernatural Horror",
        "Teen Comedy",
    ],
    "Country of Origin": [
        "United States",
        "United States",
        "South Korea",
        "United States",
        "South Korea",
        "South Korea",
        "United States",
        "South Korea",
        "South Korea",
        "United Kingdom",
        "South Korea",
        "South Korea",
        "United States",
    ],
    "Language": [
        "English",
        "English",
        "Korean",
        "English",
        "Korean",
        "Korean",
        "English",
        "Korean",
        "Korean",
        "English",
        "Korean",
        "Korean",
        "English",
    ],
    "OTT Platform": [
        "Netflix",
        "Netflix",
        "Viki / Netflix",
        "Prime Video",
        "Netflix",
        "Netflix",
        "Netflix",
        "Netflix",
        "Netflix",
        "Netflix / BBC",
        "Netflix",
        "Netflix",
        "Netflix",
    ],
    # --- New Recommended Parameters ---
    "Seasons": [8, 4, 3, 1, 1, 1, 4, 1, 1, 1, 1, 1, 4],
    "Content Rating": [
        "TV-14",
        "TV-14",
        "TV-MA",
        "TV-MA",
        "TV-MA",
        "TV-MA",
        "TV-14",
        "TV-MA",
        "TV-MA",
        "TV-MA",
        "TV-MA",
        "TV-MA",
        "TV-14",
    ],
    "Status": [
        "Ended",
        "Ongoing",
        "Ended",
        "Ongoing",
        "Ended",
        "Ended",
        "Ended",
        "Ended",
        "Ongoing",
        "Ongoing",
        "Ended",
        "Ended",
        "Ended",
    ],
    "Target Audience": [
        "Teens & Adults",
        "General",
        "Adults",
        "Young Adults",
        "Adults",
        "Adults",
        "General",
        "Adults",
        "Adults",
        "Teens & Young Adults",
        "Adults",
        "Teens & Adults",
        "Teens & Young Adults",
    ],
}

df = pd.DataFrame(data)

# 2. Filter high-rated shows/movies (IMDb >= 7.8)
top_movies = df[df["IMDb Rating"] >= 7.8].sort_values(
    by="IMDb Rating", ascending=True
)

# 3. Horizontal Bar Plot (Easier to read long title names!)
plt.figure(figsize=(10, 5))
plt.barh(top_movies["Movie/Show"], top_movies["IMDb Rating"], color="#d81b60")
plt.xlabel("IMDb Rating")
plt.title("Top Rated Shows & Movies (IMDb >= 7.8)")
plt.xlim(7.0, 9.0)  # Zoom in on relevant rating scale
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.tight_layout()

plt.show()
