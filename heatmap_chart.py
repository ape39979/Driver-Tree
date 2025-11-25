import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def create_heatmap():
    # Data
    categories = [
        "Cohesion", "Connectedness", "Engagement", "Fairness",
        "Leadership", "Morale", "Work-Life Balance",
        "Transformational Leadership", "Safe Storage"
    ]

    # Data format: [Favorable, Neutral, Unfavorable]
    data_values = [
        [78, 13, 9],  # Cohesion
        [80, 12, 8],  # Connectedness
        [79, 14, 7],  # Engagement
        [65, 17, 18], # Fairness
        [83, 10, 8],  # Leadership
        [60, 25, 15], # Morale
        [73, 15, 12], # Work-Life Balance
        [78, 19, 3],  # Transformational Leadership
        [86, 9, 4]    # Safe Storage
    ]

    sentiments = ["Favorable", "Neutral", "Unfavorable"]

    # Creating DataFrame
    # Rows: Categories
    # Columns: Sentiments
    df = pd.DataFrame(data_values, index=categories, columns=sentiments)

    # Transpose to match the user's request of:
    # xAxis: Categories
    # yAxis: Sentiments
    df_transposed = df.T

    plt.figure(figsize=(12, 6))

    # Create Heatmap
    sns.heatmap(df_transposed, annot=True, fmt="d", cmap="YlGnBu", linewidths=.5)

    plt.title("Positive Issues Heat Chart")
    plt.xlabel("Categories")
    plt.ylabel("Sentiments")

    plt.tight_layout()
    plt.savefig("heatmap.png")
    print("Heatmap saved to heatmap.png")

if __name__ == "__main__":
    create_heatmap()
