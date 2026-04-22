# Practice 10 — Pygame Projects

## 📌 Description

This project contains three games/applications built using **Pygame**:

1. Racer
2. Snake
3. Paint

Each project extends a basic version from lectures and adds extra functionality.

---

## ⚙️ Requirements

* Python 3.x
* Pygame

Install Pygame:

```
pip install pygame
```

---

## 📁 Project Structure

```
Practice10/
 ├── racer/
 │    ├── main.py
 │    └── assets (images if used)
 │
 ├── snake/
 │    └── main.py
 │
 └── paint/
      └── main.py
```

---

## 🚗 Racer

### Features:

* Player movement (left/right)
* Randomly spawning coins
* Coin collection system
* Score displayed in top-right corner

### Controls:

* LEFT / RIGHT arrows — move

### Run:

```
cd racer
python main.py
```

---

## 🐍 Snake

### Features:

* Snake movement
* Collision with walls (game over)
* Collision with itself
* Random food generation (not on snake)
* Score system
* Level system (increases every 4 points)
* Speed increases with level

### Controls:

* Arrow keys — movement

### Run:

```
cd snake
python main.py
```

---

## 🎨 Paint

### Features:

* Free drawing (brush)
* Rectangle drawing
* Circle drawing
* Eraser tool
* Color selection

### Controls:

* D — brush
* R — rectangle
* C — circle
* E — eraser

Colors:

* 1 — black
* 2 — red
* 3 — blue

### Run:

```
cd paint
python main.py
```

---

## 🧠 Notes

* All code is commented for better understanding
* Random generation is used for coins and food
* Game difficulty increases dynamically (Snake)

---

## ✅ Author

Student Practice Work — Pygame
