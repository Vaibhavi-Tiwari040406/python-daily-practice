import matplotlib.pyplot as plt
import pandas as pd

# Sample movie ratings analysis
data = {
    "Movie": ["Inception", "Interstellar", "The Dark Knight", "Dunkirk"],
    "Rating": [8.8, 8.7, 9.0, 7.8],
}
df = pd.DataFrame(data)

# Filtering high-rated movies
top_movies = df[df["Rating"] >= 8.5]

# Plotting
plt.bar(top_movies["Movie"], top_movies["Rating"], color="#d81b60")
plt.title("Top Rated Movies")
plt.ylabel("IMDb Rating")
plt.show()
