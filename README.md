# 📽️ Facebook Movie Network - Coding Assignment

This project solves a problem where you determine the **most popular movie** in a person’s Facebook-like social network — considering **friends, friends of friends**, and so on.

It uses an object-oriented design in Python with **BFS (Breadth-First Search)** to traverse the network efficiently.

---

## 📁 Project Structure

---

## 🧠 Problem Statement

> On your Facebook account, you have friends who all have a list of movies they like.
> Write a function that returns the most popular movie in your entire **network of friends**.
> The "network" includes **friends of friends**, and so on.

---

## ⚙️ How It Works

- `Person`: Represents a user with a name, a list of liked movies, and a list of friends.
- `MovieNetwork`: Manages the people and uses **BFS** to explore the network and count movie occurrences.
- `test.py`: Creates a sample network, populates users and movies, and prints the most popular movie.

---

## ▶️ Running the Code

Make sure you have Python 3 installed. Then run:

```bash
python test.py

