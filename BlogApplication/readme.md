
# Blog Application: Cuisine Marocaine 🥘 🍴

Introduction: 🥘 🍴

This project is a Django-based blog application focusing on Moroccan cuisine. The blog showcases a variety of articles and recipes, bringing the rich culinary heritage of Morocco to the forefront.

---

## Features 📂 🗂️

- **User-Friendly Interface:** Built with Bootstrap for responsive design and aesthetics.
- **Recipe Showcase:** Detailed Moroccan recipes with ingredients and step-by-step instructions.
- **Articles:** Informative posts about Moroccan food culture, history, and dining traditions.
- **Dynamic Content:** Manage recipes and articles with ease using Django's admin interface.
- **Search Functionality:** Quickly find articles and recipes by keyword.

---

## Technologies Used 💻 🧑‍💻

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Bootstrap)
- **Database:** SQLite (default Django database)
- **Others:** JavaScript for interactivity

---

## File Structure 📂 🗂️
Here is the structure of the project:
```
BLOG APPLICATION


|
├── base
│   ├── templatetags
│   │   ├── __pycache__
│   │   ├── article_filters.py
│   │   ├── custom_filters.py
│   │   ├── __init__.py
│   ├── asgi.py
│   ├── admin.py
│   ├── models.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
├── media
├── static
│   ├── css
│   │   ├── article_list.css
│   │   ├── style.css
│   ├── img
├── templates
│   ├── article_list.html
│   ├── base.html
│   ├── home.html
├── db.sqlite3
├── manage.py
```

---

## Functionalities 🌟

### 1. **Home Page 🏠**
- **Featured Recipes:** Displays a list of featured recipes, including preparation time.
- **Trending Articles:** Showcases the top 5 trending articles.
- **Spotlight Recipe:** Highlights a special Moroccan recipe (e.g., Tajine).
- **Categories:** Allows users to explore recipes by category.
- **Testimonials:** Displays customer feedback in a dynamic carousel.

### 2. **Article List Page 📄**
- **Article Details:** Provides detailed information about each article, including tags and author details.
- **Recipe Details:**
  - Displays preparation time, cooking time, and total time.
  - Lists ingredients with images and quantities.
  - Includes preparation steps and cost estimation in MAD.
- **Ratings and Comments:**
  - Allows users to rate recipes (1 to 5 stars) and leave comments.
  - Displays average ratings, total reviews, and a star breakdown.
- **Similar Recipes:** Recommends recipes similar to the current one.

### 3. **User Interaction 🗨️**
- **Rating System:**
  - Users can give a star rating to recipes, ranging from 1 to 5.
  - Average ratings and star percentages are displayed.
- **Comments Section:**
  - Users can leave comments, which are displayed in a structured format.
- **Newsletter Subscription:**
  - Users can subscribe to the newsletter via a form on the homepage.

### 4. **Backend Features (Admin Panel) 🛠️**
- **Article Management:**
  - Admins can create, edit, and delete articles.
  - Articles can be marked as featured.
- **Tag and Category Management:**
  - Admins can manage tags and categories for content organization.
- **Recipe Management:**
  - Recipes can be managed in detail, including adding ingredients, preparation, and cooking times.
- **Testimonial Management:**
  - Admins can manage user testimonials.

### 5. **Dynamic Features 🔄**
- **Dynamic Time Formatting:** Calculates and displays preparation and cooking times.
- **Carousel Displays:** Implements Bootstrap carousels for trending articles, categories, and testimonials.
- **Custom Filters:** Filters and logic for chunking items in carousels.

### 6. **Frontend Design 🎨**
- **Responsive Design:** Fully compatible with mobile and desktop screens.
- **Modern UI:** Features an elegant design with Moroccan cuisine themes.
- **Custom CSS:** Enhances user experience with additional styling.

### 7. **Additional Features 🍴**
- **Ingredient Details:** Displays ingredient images, names, and quantities.
- **Preparation Steps:** Formats steps into easy-to-read sections.
- **Footer with Social Links:** Includes links to social media and legal information.

---

## Installation 🔧

### Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment tool (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Rochdi7/Django-Projects
   cd BlogApplication
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate    # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open the application in your browser:
   - Navigate to: `http://127.0.0.1:8000`

---

## Usage  🛠️

- Visit the homepage to browse recipes and articles.
- Use the search bar to find content.
- Login as an admin to manage posts and recipes.

---

## Screenshots 📸

1. **Homepage:**
   ![Homepage Screenshot](path/to/homepage-screenshot.png)

2. **Recipe Page:**
   ![Recipe Screenshot](path/to/recipe-screenshot.png)

3. **Article Page:**
   ![Article Screenshot](path/to/article-screenshot.png)

4. **Admin Dashboard:**
   ![Admin Dashboard Screenshot](path/to/admin-screenshot.png)

---

## Video Demo 🎥

[Watch Demo Video](path/to/demo-video.mp4)

---

## Contribution 🤝

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request

---

## License 📜

This project is licensed under the MIT License:

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Contact 📧 📞

For any inquiries or support, feel free to reach out at: rochdi.karouali1234@gmail.com.
