# House Joy 🏠🛠️

**House Joy** ek web-based service platform hai jo users ko verified local service providers se connect karta hai. Is project ko **Python aur Django** framework ka use karke develop kiya gaya hai. Users easily services explore kar sakte hain, provider ki details aur availability check kar sakte hain, aur online booking kar sakte hain.

---

## 📌 Key Features

* **User Authentication:** User registration, login, logout, aur profile management.
* **Service Categories:** Interior Design, House Renovation, Plumbing, AC Repair, Cleaning, aur Painting jaise categories.
* **Service Provider Details:** Provider profile, ratings, per-square/hourly charges, discounts, aur weekly schedule.
* **Booking System:** Appointment date, time slot, address, aur custom service description ke sath booking form.
* **Booking History:** User ke purane orders aur real-time status (Pending/Approved) dekhne ki suvidha[cite: 2].
* **Admin Dashboard:** Django admin panel se services, categories, bookings, aur contact messages manage karne ka option[cite: 2].

---

## 🛠️ Tech Stack

* **Backend:** Python, Django[cite: 2]
* **Frontend:** HTML5, CSS3, Bootstrap, FontAwesome[cite: 2]
* **Database:** SQLite3[cite: 2]
* **Architecture:** Model-View-Template (MVT)[cite: 2]

---

## 📂 Project Structure

```text
myproject/
│── myproject/             # Project settings, URLs, WSGI/ASGI
│── user/                  # Main application (models, views, forms)
│── static/                # CSS, JS, images
│── templates/             # HTML templates (base, index, services, etc.)
│── db.sqlite3             # SQLite Database
│── manage.py              # Django management script
└── README.md              # Project documentation
