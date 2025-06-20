# Social Network Analysis using Python & NetworkX

This project analyzes a social network represented as a **directed graph**, where nodes represent individuals and edges represent interactions such as asking questions or influencing others. The network is built from a CSV file named `impressionNetwork.csv`.

The analysis is split into **three questions**, each handled in a separate Python file:

## 🔧 File Overview

### 1. `question1_random_walk.py` – Simulating PageRank via Random Walk

- Constructs a directed graph from `impressionNetwork.csv`.
- Performs a **random walk with teleportation** (similar to Google's PageRank algorithm) to rank users based on how frequently a random walker visits them.
- Each node collects "coins" on visits, and the final count reflects its **importance or centrality**.

### 2. `question2_missing_links.py` – Missing Link Detection

- Finds **potential missing edges** between nodes.
- For every pair of nodes with no mutual connection, it evaluates their structural relation via **least squares approximation** using the adjacency matrix.
- If a predicted value exceeds a threshold, a link is suspected to be missing.
- This is useful in detecting hidden or forgotten interactions in social networks.

### 3. `question3_influencers.py` – Finding Key Influencers (Inspired by Celebrity Problem)

- Computes **influence ratio** for each person:  
  \[
  \text{Influence Ratio} = \frac{\text{Number of people influenced (in-degree)}}{\text{Number of people they follow (out-degree)}}
  \]
- Sorts and ranks people based on this ratio.

#### 👑 How is this similar to the "Celebrity Problem" in DSA?

The classic **Celebrity Problem** is:
> In a party of `n` people, a celebrity is someone who is known by everyone (in-degree `n−1`) but knows no one (out-degree `0`).

In our case:
- We extend this by not only looking for **pure celebrities** but also identifying **relative influencers**.
- A person with a **high influence ratio** is similar to a celebrity: they are known by many (high in-degree) and follow fewer people (low out-degree).
- Thus, **the core logic of looking at in-degree vs. out-degree comes directly from the DSA celebrity problem**, but generalized to allow ratio-based ranking of influence.

---

## 📁 Dataset

Ensure `impressionNetwork.csv` is in the same directory as the Python scripts.

The CSV format:
