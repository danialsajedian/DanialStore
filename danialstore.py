# ===========================
# 🖼️ کتابخانه‌های رابط گرافیکی
# ===========================
import tkinter as tk        # ساخت پنجره لیبل دکمه گرافیکی
from tkinter import ttk, messagebox, filedialog      # ایجاد پیام های هشدار اطلاعات یا خطا
                                                     # دومی هم برای انتخاب فایل استفاده میشه

# ===========================
# 🗃️ پایگاه داده و زمان
# ===========================
import sqlite3              # برای ارتباط با دیتابیس SQLite
import datetime             # مدیریت تاریخ و زمان

# ===========================
# 🧵 پردازش چند نخی
# ===========================
import threading            # اجرای همزمان چند فرایند

# ===========================
# 📁 مدیریت فایل و مسیرها
# ===========================
import os                   # برای کار با مسیر فایل‌ها
import sys                  # مدیریت سیستم و مسیر اجرای اسکریپت
import subprocess           # اجرای دستورهای سیستمی
import tempfile             # برای ایجاد ساخت فایل موقت
# ===========================
# 🔐 رمزنگاری و توکن‌ سازی
# ===========================
import hashlib              # رمزنگاری پسوردها
import random               # تولید مقادیر تصادفی
import string               # کار با رشته‌ها برای ساخت توکن

# ===========================
# 🌐 ارتباطات شبکه‌ای و API 
# ===========================
import json                 # کار با داده‌های JSON
import requests             # ارسال درخواست HTTP
import webbrowser           # باز کردن مرورگر برای پرداخت

# ===========================
# 🎙️ تبدیل گفتار به متن (Speech Recognition)
# ===========================
import sounddevice as sd            # ضبط صدا از میکروفون
import numpy as np                  # پردازش عددی (برای سیگنال صدا)
from vosk import Model, KaldiRecognizer  # موتور تبدیل گفتار به متن
import scipy.io.wavfile as wav      # ذخیره فایل صوتی wav
import queue                        # مدیریت صف برای پردازش صدا

# =============================
# 🚀 اجرای سرور Flask جداگانه
# =============================
def run_flask_server():
    """
    اجرای فایل server.py به‌صورت جداگانه با استفاده از پایتون نصب‌شده روی سیستم.
    این تابع معمولاً در زمان اجرا برنامه GUI صدا زده می‌شود تا سرور پرداخت یا API‌ها فعال شوند.
    """
    python_path = sys.executable  # مسیر اجرایی پایتون جاری (برای سازگاری با محیط اجرا)
    server_script = os.path.join(os.getcwd(), "server.py")  # مسیر کامل فایل server.py در دایرکتوری جاری
    subprocess.Popen([python_path, server_script])  # اجرای غیرهمزمان فایل سرور

# ========================
# 🔐 رمزنگاری پسوردها
# ========================
def hash_password(password):
    """
    هش کردن رمز عبور با استفاده از الگوریتم SHA-256 برای جلوگیری از ذخیره رمز خام در دیتابیس.
    """
    return hashlib.sha256(password.encode()).hexdigest()

# ============================
# 🧩 تولید کد امنیتی کپچا
# ============================
def generate_captcha(length=5):
    """
    تولید یک رشته تصادفی شامل حروف و ارقام برای کپچا (captcha).
    - length: تعداد کاراکترها (پیش‌فرض ۵)
    """
    letters_and_digits = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    captcha_text = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return captcha_text

# ============================
#  صفحه خوش آمد گویی
# ============================
def show_splash():
    """
    نمایش صفحه لودینگ (Splash Screen) هنگام اجرای اولیه برنامه.
    شامل انیمیشن چرخشی و پیام خوش‌آمدگویی.
    """

    # 🪟 ساخت پنجره اولیه
    splash = tk.Tk()
    splash.title("در حال بارگذاری")
    splash.overrideredirect(True)  # حذف نوار بالا (بدون minimize/maximize/close)

    # 📐 تنظیم ابعاد و مرکز‌چینی پنجره
    w, h = 400, 220
    ws = splash.winfo_screenwidth()
    hs = splash.winfo_screenheight()
    x = (ws // 2) - (w // 2)
    y = (hs // 2) - (h // 2)
    splash.geometry(f"{w}x{h}+{x}+{y}")
    splash.configure(bg="#2c3e50")  # رنگ پس‌زمینه

    # 🎯 ساخت یک دایره ثابت و انیمیشن آرک چرخان در وسط صفحه
    canvas = tk.Canvas(splash, width=80, height=80, bg="#2c3e50", highlightthickness=0)
    canvas.pack(pady=20)
    circle = canvas.create_oval(10, 10, 70, 70, outline="#ecf0f1", width=5)  # دایره خارجی

    angle = [0]  # زاویه اولیه

    def rotate():
        """انیمیشن چرخشی آرک درون دایره (حلقه بی‌نهایت با after)"""
        angle[0] = (angle[0] + 10) % 360
        canvas.delete("arc")  # حذف آرک قبلی
        canvas.create_arc(
            10, 10, 70, 70,
            start=angle[0],
            extent=90,
            style="arc",
            outline="#1abc9c",
            width=5,
            tags="arc"
        )
        splash.after(50, rotate)  # هر 50 میلی‌ثانیه تکرار شود
    rotate()

    # ✨ پیام خوش‌آمدگویی به کاربر
    label = tk.Label(
        splash,
        text="😍 به فروشگاه دانیال خوش آمدید 😍",
        font=("Arial", 13, "bold"),
        bg="#2c3e50",
        fg="white"
    )
    label.pack(pady=10)

    # ⏱️ بستن پنجره بعد از چند ثانیه (به‌عنوان تایمر اسپلش)
    def close_splash():
        splash.destroy()

    splash.after(3500, close_splash)  # بستن خودکار بعد از ۳.۵ ثانیه
    splash.mainloop()

# ================================
# 🧩 اتصال به پایگاه داده SQLite
# ================================
conn = sqlite3.connect("store.db")  # اتصال یا ساخت فایل دیتابیس
cursor = conn.cursor()              # ساخت کرسر برای اجرای دستورات SQL


cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,   
                 name TEXT NOT NULL,                   
                 category TEXT,    
                 price REAL NOT NULL,                   
                 image BLOB 
    )                                      
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,      
                username TEXT UNIQUE NOT NULL,          
                password TEXT NOT NULL,             
                role TEXT NOT NULL   
                                 
    )
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS cart (
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                username TEXT,                         
                product_name TEXT,                    
                quantity INTEGER,                       
                price INTEGER   
    )                                  
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS purchases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,   
                username TEXT,                          
                product_name TEXT,                      
                count INTEGER,                         
                unit_price INTEGER,                    
                total_price INTEGER,                    
                datetime TEXT
    )                                       
""")

conn.commit()  # ✅ اعمال تغییرات روی فایل دیتابیس

# ================================
#  ایجاد یک ادمین پیش فرض
# ================================
cursor.execute("SELECT * FROM users WHERE username='admin'")  # 👀 بررسی وجود ادمین
if not cursor.fetchone():
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                   ('admin', hash_password('admin'), 'admin'))  # ➕ افزودن ادمین
conn.commit()  # ✅ ذخیره نهایی


# ======================================
# 👥 وضعیت فعلی کاربر و نقش او در سیستم
# ======================================
current_user = None   # 👤 نام‌کاربری کاربر وارد شده (None در حالت اولیه)
current_role = None   # 🧑‍💼 نقش کاربر (کاربر عادی یا ادمین)

# ============================================
# 🛒 سبد خرید موقت در حافظه – بدون اتصال فوری به دیتابیس
# ============================================
cart = {
    # مثال ساختار:
    # 'محصول مثال': {'price': 15000, 'count': 2}
}
# ======================================
# 🛡️ مرچنت‌ کد زرین‌پال (برای محیط سندباکس تستی)
# توجه: برای محیط واقعی باید کد اصلی خودت رو جایگزین کنی
# ======================================
MERCHANT = '12345678-1234-1234-1234-123456789012'

# ======================================
# 🌐 آدرس API ارسال درخواست پرداخت (Request)
# ======================================
ZP_API_REQUEST = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"

# ======================================
# 🌐 آدرس شروع پرداخت (StartPay) برای انتقال کاربر به درگاه
# Authority در این آدرس جایگزین می‌شود
# ======================================
ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/{authority}"

# ======================================
# 🔁 آدرس برگشتی از درگاه به برنامه Flask شما
# باید با روت مربوطه در سرور Flask هماهنگ باشد
# ======================================
CALLBACK_URL = "http://localhost:5000/verify"

# ======================================
# 🙈 نمایش یا مخفی کردم رمز عبور
# ======================================
def toggle_password(entry_widget, toggle_button):
    """
    👁️‍🗨️ توگل کردن نمایش رمز عبور بین حالت مخفی (*) و قابل دیدن.
    :param entry_widget: فیلد Entry مربوط به پسورد
    :param toggle_button: دکمه‌ای که آیکن چشم رو نمایش می‌ده
    """
    if entry_widget.cget('show') == '':
        entry_widget.config(show='*')            # رمز رو مخفی کن
        toggle_button.config(text='👁')           # آیکن چشم باز
    else:
        entry_widget.config(show='')              # نمایش رمز
        toggle_button.config(text='🙈')           # آیکن چشم بسته

# ======================================
# 🛒 بارکزاری سبد خرید کاربر
# ======================================
def load_cart_from_db():
    """
    🗃️ بارگذاری سبد خرید ثبت‌شده کاربر فعلی از دیتابیس به متغیر سراسری cart.
    """
    global cart
    cart = {}  # پاک‌سازی سبد قبلی در حافظه
    cursor.execute("SELECT product_name, quantity, price FROM cart WHERE username=?", (current_user,))
    for name, qty, price in cursor.fetchall():
        cart[name] = {"price": price, "count": qty}

# ======================================
# 📐 مرکز‌چینی پنجره‌ها در وسط صفحه
# ======================================
def center_window(win, w, h):
    """
    🖼️ نمایش پنجره در مرکز صفحه نمایش.
    :param win: پنجره (Tk یا Toplevel)
    :param w: عرض پنجره
    :param h: ارتفاع پنجره
    """
    win.update_idletasks()  # بروزرسانی برای به‌دست آوردن ابعاد دقیق
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (w // 2)
    y = (screen_height // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")

# ======================================
# 🔐 بررسی قدرت رمز عبور
# ======================================
def check_strength(password):
    """
    🔐 بررسی امنیت رمز عبور بر اساس پنج معیار:
    - حداقل طول ۸ کاراکتر
    - وجود رقم
    - وجود حروف بزرگ
    - وجود حروف کوچک
    - وجود علامت‌های خاص
    خروجی عددی بین ۰ تا ۵ است.
    """
    length = len(password) >= 8
    digit = any(c.isdigit() for c in password)
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    symbol = any(c in "!@#$%^&*()_+-=~{}[]<>?/" for c in password)

    score = sum([length, digit, upper, lower, symbol])
    return score  # نمره قدرت رمز

# ======================================
# 🔐 پنجره ثبت‌نام، ورود، فراموشی رمز و پیغام‌ها
# ======================================
# 📝 پنجره ثبت‌نام کاربران
def open_register():
    win = tk.Toplevel()
    win.resizable(False, False)
    win.title("ثبت‌نام")
    center_window(win, 350, 250)
    win.configure(bg="#1e1e1e")

    # 🎨 تنظیم استایل نوار قدرت رمز عبور
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Red.Horizontal.TProgressbar", troughcolor='#2c3e50', background='red')
    style.configure("Orange.Horizontal.TProgressbar", troughcolor='#2c3e50', background='orange')
    style.configure("Green.Horizontal.TProgressbar", troughcolor='#2c3e50', background='green')

    tk.Label(win, text="ثبت‌نام کاربر جدید", fg="white", bg="#1e1e1e", font=("Vazir", 13, "bold")).pack(pady=10)

    # 🔍 بررسی قدرت رمز عبور و تغییر رنگ نوار
    def update_strength(event=None):
        pwd = password.get()
        score = check_strength(pwd)
        strength_var.set(score)

        if score <= 2:
            strength_bar.configure(style="Red.Horizontal.TProgressbar")
        elif score <= 4:
            strength_bar.configure(style="Orange.Horizontal.TProgressbar")
        else:
            strength_bar.configure(style="Green.Horizontal.TProgressbar")

    frm = tk.Frame(win, bg="#1e1e1e")
    frm.pack()

    tk.Label(frm, text="نام کاربری:", bg="#1e1e1e", fg="white").grid(row=0, column=0, sticky="e")
    username = ttk.Entry(frm)
    username.grid(row=0, column=1, pady=5)

    tk.Label(frm, text="رمز عبور:", bg="#1e1e1e", fg="white").grid(row=1, column=0, sticky="e")
    password = ttk.Entry(frm, show="*")
    password.grid(row=1, column=1, pady=5)
    password.bind("<KeyRelease>", update_strength)

    # 📊 نوار قدرت رمز
    strength_var = tk.DoubleVar()
    strength_bar = ttk.Progressbar(frm, maximum=5, length=100, variable=strength_var)
    strength_bar.grid(row=2, column=0, columnspan=2, sticky="w", padx=(70,0), pady=(0, 5))

    # 👁 دکمه نمایش رمز
    toggle_btn = ttk.Button(frm, text="👁", width=3, command=lambda: toggle_password(password, toggle_btn))
    toggle_btn.grid(row=1, column=2, padx=5)

    # ✅ تابع ثبت‌نام
    def register():
        u, p = username.get(), password.get()
        if not u or not p:
            show_custom_message("خطا", "لطفاً تمام فیلدها را کامل کنید.", "warning")
            return
        if len(p) < 8 or not p.isascii():
            show_custom_message("خطا", "رمز عبور باید حداقل ۸ کاراکتر و فقط شامل حروف لاتین باشد")
            return
        try:
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                            (u, hash_password(p), "user"))
            conn.commit()
            show_custom_message("موفق", "ثبت‌نام انجام شد")
            win.destroy()
        except Exception as e:
            show_custom_message("خطا", "نام کاربری قبلاً ثبت شده است", "error")
            print("❌ خطای ثبت‌نام:", e)

    ttk.Button(win, text="ثبت‌نام", command=register).pack(pady=10)

# ======================================
# 🔁 بازیابی رمز عبور
# ======================================
def forgot_password():
    win = tk.Toplevel()
    win.title("فراموشی رمز عبور")
    center_window(win, 350, 250)
    win.configure(bg="#1e1e1e")
    win.resizable(False, False)

    tk.Label(win, text="بازیابی رمز عبور", font=("Vazir", 13, "bold"), bg="#1e1e1e", fg="white").pack(pady=10)

    frame = tk.Frame(win, bg="#1e1e1e")
    frame.pack(pady=10)

    tk.Label(frame, text="نام کاربری:", bg="#1e1e1e", fg="white").grid(row=0, column=0)
    username = ttk.Entry(frame)
    username.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="رمز جدید:", bg="#1e1e1e", fg="white").grid(row=1, column=0)
    new_pass = ttk.Entry(frame, show="*")
    new_pass.grid(row=1, column=1, pady=5)

    toggle_btn = ttk.Button(frame, text="👁", width=3, command=lambda: toggle_password(new_pass, toggle_btn))
    toggle_btn.grid(row=1, column=2, padx=5)

    def reset_password():
        u = username.get()
        p = new_pass.get()
        if not u or not p:
            show_custom_message("خطا", "فیلدها را کامل وارد کنید")
            return
        if len(p) < 8 or not p.isascii():
            show_custom_message("خطا", "رمز باید حداقل ۸ کاراکتر و فقط حروف لاتین باشد")
            return
        cursor.execute("SELECT * FROM users WHERE username=?", (u,))
        if not cursor.fetchone():
            show_custom_message("خطا", "نام کاربری وجود ندارد")
            return
        cursor.execute("UPDATE users SET password=? WHERE username=?", (hash_password(p), u))
        conn.commit()
        show_custom_message("موفق", "رمز عبور با موفقیت تغییر کرد")
        win.destroy()

    ttk.Button(win, text="تغییر رمز", command=reset_password).pack(pady=10)

# ======================================
# 🔓 پنجره ورود کاربران و ادمین
# ======================================
def open_login(is_admin=False):
    win = tk.Toplevel()
    win.title("ورود")
    center_window(win, 400, 300)
    win.configure(bg="#1e1e1e")

    role_label = "ادمین" if is_admin else "کاربر"
    tk.Label(win, text=f"ورود {role_label}", fg="white", bg="#1e1e1e", font=("Vazir", 13, "bold")).pack(pady=10)

    frm = tk.Frame(win, bg="#1e1e1e")
    frm.pack()

    tk.Label(frm, text="نام کاربری:", bg="#1e1e1e", fg="white").grid(row=0, column=0, sticky="e", pady=5, padx=5)
    username = ttk.Entry(frm, width=20)
    username.grid(row=0, column=1, pady=5, sticky="w")

    tk.Label(frm, text="رمز عبور:", bg="#1e1e1e", fg="white").grid(row=1, column=0, sticky="e", pady=5, padx=5)
    password = ttk.Entry(frm, show="*", width=20)
    password.grid(row=1, column=1, pady=5, sticky="w")

    toggle_btn = ttk.Button(frm, text="👁", width=2, command=lambda: toggle_password(password, toggle_btn))
    toggle_btn.grid(row=1, column=2, sticky="w", padx=(3, 5))

    tk.Label(frm, text="کد امنیتی را وارد کنید:", bg="#1e1e1e", fg="white").grid(row=2, column=0, sticky="e", pady=5, padx=5)
    captcha_entry = ttk.Entry(frm, width=20)
    captcha_entry.grid(row=2, column=1, pady=5, sticky="w")

    captcha_text = tk.StringVar(value=generate_captcha())
    captcha_canvas = tk.Canvas(frm, width=120, height=40, bg="#1e1e1e", highlightthickness=0)
    captcha_canvas.grid(row=3, column=1, pady=(3, 5), sticky="w")

    def draw_captcha():
        captcha_canvas.delete("all")
        captcha_canvas.create_rectangle(2, 2, 118, 38, fill="#34495e", outline="#1abc9c", width=2)
        captcha_canvas.create_text(60, 20, text=captcha_text.get(), font=("Consolas", 14, "bold"), fill="white")

    def refresh_captcha():
        captcha_text.set(generate_captcha())
        draw_captcha()

    draw_captcha()

    refresh_btn = ttk.Button(frm, text="🔄", width=2, command=refresh_captcha)
    refresh_btn.grid(row=3, column=2, sticky="w", padx=(0, 5))

    def login():
        global current_user, current_role
        u, p = username.get(), password.get()
        c = captcha_entry.get()

        if not u or not p or not c:
            show_custom_message("خطا", "لطفاً تمام فیلدها را پر کنید")
            return
        if c != captcha_text.get():
            show_custom_message("کپچا اشتباه", "کد امنیتی وارد شده صحیح نیست", "warning")
            username.delete(0, tk.END)
            password.delete(0, tk.END)
            captcha_entry.delete(0, tk.END)
            refresh_captcha()
            return

        cursor.execute("SELECT role FROM users WHERE username=? AND password=?", (u, hash_password(p)))
        row = cursor.fetchone()
        if row:
            if is_admin and row[0] != 'admin':
                show_custom_message("خطا", "دسترسی ادمین ندارید")
                return
            current_user = u
            current_role = row[0]
            load_cart_from_db()
            win.destroy()
            main_window()
        else:
            show_custom_message("ناموفق", "رمز عبور یا نام کاربری اشتباه است!")
            username.delete(0, tk.END)
            password.delete(0, tk.END)
            captcha_entry.delete(0, tk.END)
            refresh_captcha()

    ttk.Button(frm, text="فراموشی رمز عبور", command=forgot_password).grid(row=4, column=1, sticky="w", pady=(10, 5))
    ttk.Button(frm, text="ورود", command=login).grid(row=4, column=2, sticky="e", pady=(10, 5))

# ======================================
# 📢 نمایش پیغام سفارشی با ایموجی
# ======================================
def show_custom_message(title, message, icon_type="info"):
    popup = tk.Toplevel()
    popup.title(title)
    popup.configure(bg="#1e1e1e")
    popup.resizable(False, False)

    w, h = 320, 180
    ws = popup.winfo_screenwidth()
    hs = popup.winfo_screenheight()
    x = (ws // 2) - (w // 2)
    y = (hs // 2) - (h // 2)
    popup.geometry(f"{w}x{h}+{x}+{y}")

    icon_label = tk.Label(popup, bg="#1e1e1e", font=("Arial", 24))
    if icon_type == "error":
        icon_label.config(text="❌")
    elif icon_type == "warning":
        icon_label.config(text="⚠️")
    else:
        icon_label.config(text="✅")
    icon_label.pack(pady=(15, 0))

    msg_label = tk.Label(popup, text=message, bg="#1e1e1e", fg="#ecf0f1", font=("Vazir", 11), wraplength=280, justify="center")
    msg_label.pack(pady=10, padx=20)

    ttk.Button(popup, text="باشه", command=popup.destroy).pack(pady=(5, 10))
    popup.grab_set()

# ======================================
# 🧷 صفحه انتخاب ورود و ثبت‌نام
# ======================================
def show_login():
    login_win = tk.Tk()
    login_win.title("فروشگاه دانیال")
    center_window(login_win, 500, 350)
    login_win.configure(bg="#222222")
    login_win.resizable(False, False)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Dark.TButton",
                    background="#34495e", foreground="white",
                    font=("Vazir", 11), padding=8,
                    borderwidth=0, relief="flat")
    style.map("Dark.TButton", background=[("active", "#1abc9c")])

    logo_image = tk.PhotoImage(file="logo.png")
    tk.Label(login_win, image=logo_image).pack(pady=40)

    frame = tk.Frame(login_win, bg="#1e1e1e")
    frame.pack(expand=True)

    ttk.Button(frame, text="ورود کاربر", command=lambda: open_login(False), style="Dark.TButton").pack(pady=5)
    ttk.Button(frame, text="ورود ادمین", command=lambda: open_login(True), style="Dark.TButton").pack(pady=5)
    ttk.Button(frame, text="ثبت‌نام", command=open_register, style="Dark.TButton").pack(pady=5)

    login_win.mainloop()

# ======================================
# ↩️ خروج از پنجره و بازگشت به صفحه ورود
# ======================================
def exit_to_login(window):
    window.destroy()
    show_login()

# ============================================================
# 🧾 ذخیره‌سازی فاکتور خرید به صورت فایل متنی با جزئیات کامل
# ============================================================
def save_invoice(cart):
    # بررسی اینکه آیا سبد خرید خالی است یا نه
    if not cart:
        return None

    # 🕓 گرفتن زمان و تاریخ فعلی برای نام‌گذاری فایل
    now = datetime.datetime.now().strftime("%H-%M-%S_%d-%m-%Y")

    # 📁 ساخت مسیر کامل فایل خروجی (در پوشه فعلی)
    filename = os.path.join(os.getcwd(), f"فاکتور_{now}.txt")
    
    # ✍️ نوشتن اطلاعات سبد خرید در فایل
    with open(filename, "w", encoding="utf-8") as file:
        total_price = 0
        for item in cart:
            # 🛍️ هر خط شامل نام محصول، تعداد و قیمت واحد آن است
            line = f"{item['name']} - تعداد: {item['quantity']} - قیمت واحد: {item['price']} تومان\n"
            file.write(line)
            # ➕ جمع کردن مبلغ کل
            total_price += item['quantity'] * item['price']
        
        # 💰 درج مبلغ کل در پایان فایل
        file.write(f"\nمبلغ کل: {total_price} تومان\n")

    # ✅ پیام موفقیت و مسیر فایل ذخیره شده در کنسول
    print("📄 فاکتور ذخیره شد:", filename)
    
    # 📨 بازگرداندن مسیر فایل ذخیره شده
    return filename

# =====================================
# 🖼️ پنجره اصلی فروشگاه (Main Window)
# =====================================
image_path_var = None  # 🖼️ مسیر تصویر انتخاب‌شده برای محصول جدید
def main_window():
    global main_win

    # 🧹 پاک‌سازی پنجره‌های قبلی (در صورت وجود)
    try:
        for widget in tk._default_root.winfo_children():
            widget.destroy()
        tk._default_root.destroy()
    except:
        pass

    # 🪟 ایجاد پنجره اصلی
    main_win = tk.Tk()
    main_win.resizable(True, True)
    main_win.rowconfigure(0, weight=1)
    main_win.columnconfigure(0, weight=1)
    main_win.title("فروشگاه اینترنتی دانیال")
    center_window(main_win, 1000, 700)
    main_win.configure(bg="#1e1e1e")

    # 🎨 استایل‌های سفارشی برای اجزای گرافیکی
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("TButton",
                    background="#34495e",
                    foreground="white",
                    borderwidth=0,
                    padding=8,
                    relief="flat")
    style.map("TButton", background=[('active', '#1abc9c')])

    style.configure("TEntry",
                    fieldbackground="#2c3e50",
                    foreground="white",
                    padding=5,
                    relief="flat")

    style.configure("Treeview",
                    background="#2c3e50",
                    foreground="white",
                    rowheight=28,
                    fieldbackground="#2c3e50",
                    borderwidth=0)
    style.map("Treeview", background=[('selected', '#1abc9c')])

    # -------------------------------
    # 👑 پنل ادمین (در صورت ورود ادمین)
    # -------------------------------
    if current_role == "admin":
        notebook = ttk.Notebook(main_win)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # ----------------------
        # 📦 تب مدیریت محصولات
        # ----------------------
        product_tab = tk.Frame(notebook, bg="#2c3e50")
        notebook.add(product_tab, text="مدیریت محصولات")
        product_tab.rowconfigure(1, weight=1)
        product_tab.columnconfigure(0, weight=1)

        global tree
        columns = ("id", "name", "category", "price")
        tree = ttk.Treeview(product_tab, columns=columns, show="headings", height=15)
        tree.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        # 🧾 ستون‌های جدول محصولات
        tree.heading("id", text="کد")
        tree.heading("name", text="نام محصول")
        tree.heading("category", text="دسته‌بندی")
        tree.heading("price", text="قیمت (تومان)")

        tree.column("id", width=50, anchor="center")
        tree.column("name", width=200, anchor="center")
        tree.column("category", width=150, anchor="center")
        tree.column("price", width=100, anchor="center")

        # 🔄 بارگذاری اطلاعات محصولات
        def refresh():
            for i in tree.get_children():
                tree.delete(i)
            cursor.execute("SELECT * FROM products ORDER BY category, name")
            for row in cursor.fetchall():
                tree.insert("", tk.END, values=row)
                tree.insert("", tk.END, values="")

        refresh()

        # ------------------------------
        # 📝 فرم ورود اطلاعات محصول جدید
        # ------------------------------
        frm = tk.Frame(product_tab, bg="#2c3e50")
        frm.grid(row=0, column=0, pady=10)

        tk.Label(frm, text="نام", bg="#2c3e50", fg="white").grid(row=0, column=0)
        name = ttk.Entry(frm)
        name.grid(row=0, column=1)

        tk.Label(frm, text="دسته", bg="#2c3e50", fg="white").grid(row=0, column=2)
        cat = ttk.Entry(frm)
        cat.grid(row=0, column=3)

        tk.Label(frm, text="قیمت", bg="#2c3e50", fg="white").grid(row=0, column=4)
        price = ttk.Entry(frm)
        price.grid(row=0, column=5)

        # 📤 بارگذاری تصویر محصول
        def upload_image():
            global image_path_var
            file_path = filedialog.askopenfilename(
                title="انتخاب تصویر محصول",
                filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
            )
            if file_path:
                image_path_var = file_path
                image_status_label.config(text=f"✅ {os.path.basename(file_path)} انتخاب شد", fg="lightgreen")
            else:
                image_path_var = None
                image_status_label.config(text="❌ عکسی انتخاب نشد", fg="red")

        ttk.Button(frm, text="📷 انتخاب عکس", command=upload_image).grid(row=0, column=9, padx=5)
        image_status_label = tk.Label(frm, text="📷 هیچ تصویری انتخاب نشده", bg="#1e1e1e", fg="gray")
        image_status_label.grid(row=1, column=9, columnspan=2, sticky="w")

        # ------------------------
        # ➕ افزودن محصول جدید
        # ------------------------
        def add():
            global image_path_var

            name_val = name.get().strip()
            category_val = cat.get().strip()
            price_val = price.get().strip()

            if not name_val or not category_val or not price_val:
                show_custom_message("خطا", "همه فیلدها باید پر شوند")
                return

            try:
                price_float = float(price_val)
            except:
                show_custom_message("خطا", "قیمت معتبر نیست")
                return

            if not image_path_var or not os.path.exists(image_path_var):
                show_custom_message("خطا", "لطفاً یک تصویر معتبر انتخاب کنید")
                return
            # ------------------------
            # 📦 ذخیره محصول در پایگاه داده
            # ------------------------
            cursor.execute("INSERT INTO products (name, category, price, image) VALUES (?, ?, ?, ?)",
                           (name_val, category_val, price_float, image_path_var))
            conn.commit()

            show_custom_message("موفقیت", "محصول با موفقیت اضافه شد")
            image_path_var = None
            image_status_label.config(text="📷 هیچ تصویری انتخاب نشده", fg="gray")

            name.delete(0, tk.END)
            cat.delete(0, tk.END)
            price.delete(0, tk.END)

            refresh()
        # ------------------------
        # 🗑 حذف محصول انتخاب‌شده
        # ------------------------
        def delete():
            sel = tree.selection()
            if sel:
                item = tree.item(sel[0])
                pid = item["values"][0]
                cursor.execute("DELETE FROM products WHERE id=?", (pid,))
                conn.commit()
                refresh()

        ttk.Button(frm, text="➕ افزودن", command=add).grid(row=0, column=7, padx=5)
        ttk.Button(frm, text="🗑 حذف", command=delete).grid(row=0, column=8, padx=5)

        # ------------------------
        # 🔐 تب مدیریت ادمین‌ها
        # ------------------------
        admin_tab = tk.Frame(notebook, bg="#2c3e55")
        notebook.add(admin_tab, text="مدیریت ادمین‌ها")

        frm2 = tk.Frame(admin_tab, bg="#34495e")
        frm2.pack(pady=5)

        tk.Label(frm2, text="نام کاربری:", bg="#34495e", fg="white").grid(row=0, column=0)
        admin_user = ttk.Entry(frm2)
        admin_user.grid(row=0, column=1, padx=5)

        tk.Label(frm2, text="رمز عبور:", bg="#34495e", fg="white").grid(row=0, column=2)
        admin_pass = ttk.Entry(frm2, show="*")
        admin_pass.grid(row=0, column=3, padx=5)

        toggle_btn = ttk.Button(frm2, text="👁", width=3, command=lambda: toggle_password(admin_pass, toggle_btn))
        toggle_btn.grid(row=0, column=4)

        # ➕ افزودن ادمین جدید
        def add_admin():
            username = admin_user.get().strip()
            password = admin_pass.get()

            if not username or not password:
                show_custom_message("خطا", "تمامی فیلد ها رو تکمیل کنید")
                return

            if len(password) < 8 or not password.isascii():
                show_custom_message("خطا", "رمز عبور باید حداقل ۸ کاراکتر و فقط شامل حروف لاتین باشد")
                return

            try:
                cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                               (username, hash_password(password), "admin"))
                conn.commit()
                show_custom_message("ثبت شد", "ادمین جدید افزوده شد")
                admin_user.delete(0, tk.END)
                admin_pass.delete(0, tk.END)
                refresh_admins()
            except:
                show_custom_message("خطا", "نام کاربری تکراری است")
        
        # 📃 لیست ادمین‌های ثبت‌شده
        admin_list = tk.Listbox(admin_tab, height=6, width=50, font=("Vazir", 10),
                                bg="#406386", fg="white", bd=0, highlightthickness=0,
                                selectbackground="#1abc9c", selectforeground="black")
        admin_list.pack(padx=20, pady=10)

        # 🔄 بروزرسانی لیست ادمین‌ها
        def refresh_admins():
            admin_list.delete(0, tk.END)
            cursor.execute("SELECT username FROM users WHERE role='admin'")
            for row in cursor.fetchall():
                admin_list.insert(tk.END, row[0])
                admin_list.insert(tk.END, "")

        # 🗑 حذف ادمین انتخاب‌شده
        def delete_admin():
            sel = admin_list.curselection()
            if sel:
                username = admin_list.get(sel[0])
                if username == "admin":
                    show_custom_message("مجاز نیست", "ادمین اصلی قابل حذف نیست")
                    return
                cursor.execute("DELETE FROM users WHERE username=? AND role='admin'", (username,))
                conn.commit()
                refresh_admins()

        ttk.Button(admin_tab, text="➕ افزودن ادمین", command=add_admin).pack(pady=10)
        ttk.Button(admin_tab, text="🗑 حذف ادمین", command=delete_admin).pack(pady=10)

        refresh_admins()

        # ------------------------
        # 🔙 دکمه بازگشت به صفحه ورود
        # ------------------------
        ttk.Button(main_win, text="بازگشت 🔙", command=lambda: exit_to_login(main_win)).pack(pady=10)

    # ===============================
    # 👤 پنل مشتری (کاربر غیرادمین)
    # ===============================
    else:
        # 🔲 قاب اصلی مشتری
        container = tk.Frame(main_win, bg="#1e1e1e")
        container.pack(fill='both', expand=True)

        # 🔻 دکمه بازگشت پایین صفحه
        bottom_frame = tk.Frame(container, bg="#1e1e1e")
        bottom_frame.pack(side='bottom', fill='x', pady=(0, 10))

        ttk.Button(bottom_frame, text="بازگشت 🔙", command=lambda: exit_to_login(main_win)).pack(anchor="center")

        # 👋 پیام خوش‌آمدگویی
        header = tk.Label(container, text=f"خوش آمدید {current_user}",
                        font=("Vazir", 13, "bold"), bg="#34495e", fg="white")
        header.pack(fill='x', pady=5)

        # 🔲 قاب اصلی نمایش و کنترل‌ها
        frm = tk.Frame(container, bg="#1e1e1e")
        frm.pack(fill='both', expand=True, padx=20, pady=10)

        top_controls = tk.Frame(frm, bg="#1e1e1e")
        top_controls.pack(pady=10, fill='x')

        # 🔤 متغیرهای جست‌وجو و فیلتر
        search_var = tk.StringVar()
        filter_var = tk.StringVar(value="مرتب‌سازی")

        # 🎨 استایل منوها
        style.configure("TMenubutton", background="#34495e", foreground="white",
                        font=("Vazir", 10), relief="flat")
        style.configure("Treeview", background="#2c3e50", foreground="white",
                        rowheight=28, fieldbackground="#2c3e50", borderwidth=0)
        style.map("Treeview", background=[('selected', '#1abc9c')])

        # 🔍 نوار جست‌وجو و فیلتر
        search_entry = ttk.Entry(top_controls, width=25, textvariable=search_var)
        search_entry.pack(side='right', padx=(0, 10))

        search_btn = ttk.Button(top_controls, text="🔍 جستجو", command=lambda: show_filtered())
        search_btn.pack(side='right', padx=(5, 10))

        filter_menu = ttk.OptionMenu(top_controls, filter_var, "مرتب‌سازی", "قیمت ⬆", "قیمت ⬇", "الفبا", command=lambda _: show_filtered())
        filter_menu.pack(side='right', padx=(0, 15))

        reset_btn = ttk.Button(top_controls, text="❌ حذف فیلتر", command=lambda: reset_filters())
        reset_btn.pack(side='right', padx=(10, 10))

        contact_btn = ttk.Button(top_controls, text="تماس با ما", command=lambda: toggle_contact_info())
        contact_btn.pack(side='left', padx=(10, 10))

        # 📦 جدول محصولات
        columns = ("name", "category", "price")
        tree = ttk.Treeview(frm, columns=columns, show="tree headings", height=12)
        tree.pack(expand=True, fill='both', pady=5)

        tree.heading("#0", text="تصویر")
        tree.heading("name", text="نام محصول")
        tree.heading("category", text="دسته‌بندی")
        tree.heading("price", text="قیمت (تومان)")

        tree.column("#0", width=60, anchor="center")
        tree.column("name", width=200, anchor="center")
        tree.column("category", width=150, anchor="center")
        tree.column("price", width=100, anchor="center")

        # 🎯 دکمه‌های کنترل محصول
        tree_controls = tk.Frame(frm, bg="#1e1e1e")
        tree_controls.pack(pady=5)

        ttk.Button(tree_controls, text="➕ افزودن به سبد", command=lambda: select_item_and_add()).pack(side='right', padx=5)
        ttk.Button(tree_controls, text="➖ حذف از سبد", command=lambda: select_item_and_remove()).pack(side='right', padx=5)
        ttk.Button(tree_controls, text="🧾 تکمیل خرید", command=complete_purchase).pack(side='right', padx=5)

        # 🛒 جدول سبد خرید
        global cart_tree
        cart_tree = ttk.Treeview(frm, columns=("name", "count", "price"), show="headings", height=5)
        cart_tree.pack(pady=(10, 10), fill="x")

        cart_tree.heading("name", text="نام محصول")
        cart_tree.heading("count", text="تعداد")
        cart_tree.heading("price", text="قیمت (تومان)")

        cart_tree.column("name", anchor="center")
        cart_tree.column("count", width=70, anchor="center")
        cart_tree.column("price", anchor="center")

        # 📱 اطلاعات تماس (ابتدا مخفی)
        contact_frame = tk.Frame(top_controls, bg="#ecf0f1", bd=1, relief="solid")
        tk.Label(contact_frame, text="شماره تماس: 09399236753", bg="#ecf0f1").pack(anchor="w", padx=10, pady=5)
        tk.Label(contact_frame, text="daniallsajedian@gmail.com :ایمیل", bg="#ecf0f1").pack(anchor="w", padx=10, pady=5)
        contact_frame.pack_forget()

        # =======================
        # 🧠 توابع مربوط به مشتری
        # =======================
        # تابع مخفی یا نشان دادن اطلاعات تماس با ما
        def toggle_contact_info():
            if contact_frame.winfo_ismapped():
                contact_frame.pack_forget()
            else:
                contact_frame.pack(pady=(0, 10), anchor="ne")
        # تابع برای اعمال فیلتر ها
        def show_filtered():
            tree.delete(*tree.get_children())
            global product_images
            product_images = []
            product_images.clear()

            keyword = search_var.get().strip()
            filter_type = filter_var.get()

            cursor.execute("SELECT * FROM products")
            rows = cursor.fetchall()

            # 🔍 جست‌وجوی کلمه‌کلیدی
            if keyword:
                rows = [row for row in rows if keyword in row[1]]

            # 🔃 مرتب‌سازی
            if filter_type == "قیمت ⬆":
                rows.sort(key=lambda x: x[3])
            elif filter_type == "قیمت ⬇":
                rows.sort(key=lambda x: -x[3])
            elif filter_type == "الفبا":
                rows.sort(key=lambda x: x[1])

            # 📷 درج اطلاعات به همراه تصویر
            for row in rows:
                image_path = row[4]
                img = None
                try:
                    if image_path and os.path.exists(image_path):
                        img = tk.PhotoImage(file=image_path).subsample(1, 1)
                except Exception as e:
                    print("❌ خطا در بارگذاری عکس:", e)

                product_images.append(img)
                tree.insert("", tk.END, text="", image=img, values=(row[1], row[2], f"{row[3]:,} تومان"))
        # تابع پاکسازی فیلتر ها
        def reset_filters():
            search_var.set("")
            filter_var.set("مرتب‌سازی")
            show_filtered()

        # =========================
        # 🔊 جستجوی صوتی (فارسی)
        # =========================
        audio_result_queue = queue.Queue()
        # تابع تبدیل گفتار به متن
        def start_voice_search():
            fs = 16000
            duration = 5

            print("🧠 در حال بارگذاری مدل...")
            model = Model("models/fa")
            rec = KaldiRecognizer(model, fs)

            print("🎙 شروع ضبط...")
            audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
            sd.wait()
            print("✅ ضبط تمام شد. در حال تحلیل...")

            if rec.AcceptWaveform(audio.tobytes()):
                result = json.loads(rec.Result())
            else:
                result = json.loads(rec.FinalResult())

            text = result.get("text", "")
            print("📝 نتیجه:", text)

            audio_result_queue.put(text)
            main_win.after(100, check_voice_result)
        # تابع برای دریافت نتایج و نمایش آن
        def check_voice_result():
            try:
                text = audio_result_queue.get_nowait()
                search_var.set(text)
                show_filtered()
            except queue.Empty:
                main_win.after(100, check_voice_result)

        # ==============================
        # 🎤 دکمه ضبط صدا
        # ==============================
        mic_btn = ttk.Button(top_controls, text="🎤", command=start_voice_search)
        mic_btn.pack(side='right', padx=(5, 5))    

# ======================================
# 🛒 توابع مدیریت سبد خرید
# ======================================
# 🔄 به‌روزرسانی لیست سبد خرید در UI
def update_cart_list():
    cart_tree.delete(*cart_tree.get_children())  # حذف همه آیتم‌های قبلی
    for name, info in cart.items():
        total = info["count"] * info["price"]
        cart_tree.insert("", "end", values=(name, info["count"], f"{total} تومان"))

# ➕ افزودن محصول به سبد خرید
def add_to_cart(name, price):
    if name in cart:
        cart[name]["count"] += 1
        # 🟡 به‌روزرسانی در دیتابیس در صورت وجود محصول
        cursor.execute("UPDATE cart SET quantity=? WHERE username=? AND product_name=?",
                       (cart[name]["count"], current_user, name))
    else:
        cart[name] = {"price": price, "count": 1}
        # 🟢 درج محصول جدید در دیتابیس
        cursor.execute("INSERT INTO cart (username, product_name, quantity, price) VALUES (?, ?, ?, ?)",
                       (current_user, name, 1, price))
    conn.commit()
    update_cart_list()

# ➖ حذف محصول از سبد خرید
def remove_from_cart(name):
    if name in cart:
        cart[name]["count"] -= 1
        if cart[name]["count"] <= 0:
            del cart[name]
            # 🔴 حذف از دیتابیس در صورت صفر شدن تعداد
            cursor.execute("DELETE FROM cart WHERE username=? AND product_name=?", (current_user, name))
        else:
            # 🟡 به‌روزرسانی تعداد در دیتابیس
            cursor.execute("UPDATE cart SET quantity=? WHERE username=? AND product_name=?",
                           (cart[name]["count"], current_user, name))
        conn.commit()
    update_cart_list()

# 🖱️ انتخاب آیتم از جدول و افزودن به سبد خرید
def select_item_and_add():
    sel = tree.selection()
    if sel:
        item = tree.item(sel[0])["values"]
        name = item[0]
        try:
            # 🧮 استخراج قیمت به‌صورت عددی
            price_str = str(item[2]).replace("تومان", "").replace(",", "").strip()
            price = float(price_str)
            add_to_cart(name, price)
        except:
            show_custom_message("خطا", f"قیمت نامعتبر است: {item[2]}", "error")

# 🖱️ انتخاب آیتم از جدول و حذف از سبد خرید
def select_item_and_remove():
    sel = tree.selection()
    if sel:
        item = tree.item(sel[0])["values"]
        name = item[0]
        remove_from_cart(name)

# ========================================
# 💳 تابع ارسال درخواست پرداخت به زرین‌پال
# ========================================
# تابع ارسال اطلاعات پرداخت به سمت سرور
def send_payment_request(amount):
    print("📤 درخواست پرداخت فراخوانی شد")

    # 🔧 داده‌های مورد نیاز برای ارسال درخواست به زرین‌پال
    data = {
        "merchant_id": MERCHANT,  # آیدی پذیرنده
        "amount": amount * 10,    # مبلغ به ریال (تبدیل از تومان)
        "callback_url": CALLBACK_URL,  # آدرس بازگشت پس از پرداخت
        "description": "خرید از فروشگاه دانیال",
        "metadata": {
            "mobile": "09120000000",
            "email": "test@example.com"
        }
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        # 📡 ارسال درخواست POST به زرین‌پال
        response = requests.post(ZP_API_REQUEST, data=json.dumps(data), headers=headers)
        result = response.json()
        print("✅ پاسخ دریافتی از زرین‌پال:", result)

        # 🚫 بررسی وجود خطا در پاسخ دریافتی
        if 'errors' in result:
            errors = result['errors']
            if isinstance(errors, list) and len(errors) > 0:
                message = errors[0].get("message", "خطای نامشخص")
                show_custom_message("❌ خطا در پرداخت", message)
                return
            elif isinstance(errors, dict) and errors.get("message"):
                message = errors.get("message", "خطای نامشخص")
                show_custom_message("❌ خطا در پرداخت", message)
                return

        # 🆔 استخراج authority برای پرداخت
        authority = result['data']['authority']
        pay_url = ZP_API_STARTPAY.format(authority=authority)
        print("🆔 authority دریافتی:", authority)

        # 📝 ساخت فایل HTML موقت برای ذخیره authority در سرور محلی

        def generate_session_saver(authority, amount):
            html = f"""
            <html>
            <body onload="document.forms[0].submit()">
                <form method="post" action="http://127.0.0.1:5000/save-session">
                    <input type="hidden" name="authority" value="{authority}">
                    <input type="hidden" name="amount" value="{int(amount)}">
                </form>
                <p>در حال ذخیره سشن پرداخت...</p>
            </body>
            </html>
            """
            with tempfile.NamedTemporaryFile("w", delete=False, suffix=".html", encoding="utf-8") as f:
                f.write(html)
                return f.name

        # 📄 ایجاد فایل HTML و باز کردن آن در مرورگر برای ذخیره authority
        html_file = generate_session_saver(authority, amount * 10)
        webbrowser.open(f"file://{html_file}")

        # 🌐 باز کردن درگاه پرداخت در مرورگر
        webbrowser.open(pay_url)

    except Exception as e:
        # ⚠️ خطا در ارتباط با سرور زرین‌پال
        show_custom_message("❌ خطا در ارتباط با درگاه", str(e))

# ========================================================
# 🧾 تابع نمایش صفحه تکمیل خرید و نمایش فاکتور نهایی
# ========================================================
def complete_purchase():
    # ⛔️ بررسی خالی بودن سبد خرید
    if not cart:
        show_custom_message("خالی", "سبد خرید شما خالی است", "warning")
        return

    # ==============================
    # 🪟 تنظیمات اولیه پنجره جدید
    # ==============================
    win = tk.Toplevel(main_win)
    win.title("🧾 تکمیل فرایند خرید")
    center_window(win, 550, 450)
    win.configure(bg="#1e1e1e")

    container = tk.Frame(win, bg="#1e1e1e")
    container.pack(fill="both", expand=True)

    tk.Label(container, text="🛍 لیست خرید نهایی", font=("Vazir", 13, "bold"),
             bg="#1e1e1e", fg="white").pack(pady=10)

    # ====================================
    # 📊 جدول نمایش اقلام داخل سبد خرید
    # ====================================
    columns = ("name", "count", "unit_price", "total_price")
    tree = ttk.Treeview(container, columns=columns, show="headings", height=10)
    tree.pack(padx=10, fill="both", expand=True)

    # 🧾 عنوان ستون‌ها
    tree.heading("name", text="نام محصول")
    tree.heading("count", text="تعداد")
    tree.heading("unit_price", text="قیمت واحد")
    tree.heading("total_price", text="قیمت کل")

    # 📐 تنظیمات عرض ستون‌ها
    tree.column("name", width=150, anchor="center")
    tree.column("count", width=80, anchor="center")
    tree.column("unit_price", width=100, anchor="center")
    tree.column("total_price", width=120, anchor="center")

    # 🔢 پر کردن جدول و محاسبه مبلغ کل
    total_price = 0
    for name, info in cart.items():
        count = info["count"]
        unit_price = info["price"]
        total = count * unit_price
        total_price += total
        tree.insert("", tk.END, values=(name, count, f"{unit_price} تومان", f"{total} تومان"))

    # 💵 نمایش مجموع مبلغ
    tk.Label(container, text=f"💵 مجموع مبلغ: {total_price:,} تومان", font=("Vazir", 12, "bold"),
             bg="#1e1e1e", fg="#1abc9c").pack(pady=(10, 5))

    # ======================================================
    # ✅ تابع نهایی‌سازی خرید و ذخیره فاکتور و پرداخت
    # ======================================================
    def finalize():
        pay_btn.config(state="disabled")  # جلوگیری از کلیک مجدد

        try:
            # 💾 ذخیره‌سازی فاکتور به صورت فایل txt
            filename = f"فاکتور خرید_{current_user}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write("🧾 فاکتور خرید\n")
                f.write("="*40 + "\n")
                for name, info in cart.items():
                    total = info["count"] * info["price"]
                    f.write(f"{name} - تعداد: {info['count']} - قیمت: {info['price']} تومان - جمع: {total} تومان\n")
                f.write("="*40 + f"\nمبلغ نهایی: {total_price:,} تومان\n")

        except Exception as e:
            show_custom_message("❌ خطا در ذخیره فاکتور", str(e), "error")
            return

        try:
            # 🧹 پاک‌سازی سبد خرید از حافظه و پایگاه داده
            cart.clear()
            cursor.execute("DELETE FROM cart WHERE username=?", (current_user,))
            conn.commit()
            update_cart_list()
        except Exception as e:
            show_custom_message("❌ خطا در پاکسازی سبد خرید", str(e), "error")

        try:
            # 🌐 باز کردن درگاه پرداخت زرین‌پال
            send_payment_request(total_price)
        except Exception as e:
            show_custom_message("❌ خطا در باز کردن درگاه پرداخت", str(e), "error")

        show_custom_message("پرداخت ثبت شد", "✅ فاکتور ذخیره و سبد خرید پاک شد")
        win.destroy()

    # ==========================
    # 🔘 دکمه پرداخت و نهایی‌سازی
    # ==========================
    pay_btn = tk.Button(container, text="💳 پرداخت", command=finalize,
                        bg="#2e2e2e", fg="white", font=("B Nazanin", 12, "bold"))
    pay_btn.pack(pady=10)

# ==========================
# 🪟 پنجره نمایش سبد خرید
# ==========================
def show_cart_window():
    if not cart:
        show_custom_message("خالی", "سبد خرید خالی است", "warning")
        return
    # ساخت پنجره جدید
    win = tk.Toplevel(main_win)
    win.title("🛒 سبد خرید")
    center_window(win, 550, 400)
    win.configure(bg="#1e1e1e")

    # نمایش سبد خرید شما
    tk.Label(win, text="📦 سبد خرید شما", font=("Vazir", 13, "bold"), bg="#1e1e1e", fg="white").pack(pady=10)

    # تعریف متغیر tree
    columns = ("name", "count", "unit_price", "total_price")
    tree = ttk.Treeview(win, columns=columns, show="headings", height=10)
    tree.pack(padx=10, pady=10, fill="both", expand=True)

    # وارد کردن نام ستون ها
    tree.heading("name", text="نام محصول")
    tree.heading("count", text="تعداد")
    tree.heading("unit_price", text="قیمت واحد")
    tree.heading("total_price", text="قیمت کل")

    # تعیین موقعیت ستون ها
    tree.column("name", width=150, anchor="center")
    tree.column("count", width=80, anchor="center")
    tree.column("unit_price", width=100, anchor="center")
    tree.column("total_price", width=120, anchor="center")

    # استایل دهی به ستون ها
    style = ttk.Style()
    style.configure("Treeview",
        background="#2c3e50",
        foreground="white",
        rowheight=28,
        fieldbackground="#2c3e50",
        borderwidth=0)
    style.map("Treeview", background=[('selected', '#1abc9c')])

    # انجام محاسبات برای بدست آوردن جمع کل مبلغ
    total_all = 0
    for name, info in cart.items():
        count = info["count"]
        unit = info["price"]
        total = count * unit
        total_all += total
        tree.insert("", tk.END, values=(name, count, f"{unit:,} تومان", f"{total:,} تومان"))

    # ==========================
    # 🔘 نمایش مجموع کل مبلغ
    # ==========================
    tk.Label(win, text=f"💰 مجموع کل: {total_all:,} تومان", font=("Vazir", 12, "bold"),
            bg="#1e1e1e", fg="#1abc9c").pack(pady=(5, 15))
    
    main_win.mainloop()
# ---------------- اجرای اولیه ----------------
run_flask_server()  # اجرای سرور فلاسک برای مدیریت session پرداخت

# اجرای splash screen در نخ جداگانه
splash_thread = threading.Thread(target=show_splash)
splash_thread.start()
splash_thread.join()  # منتظر ماندن تا اسپلش تمام شود

# نمایش صفحه ورود
show_login()

# بستن اتصال دیتابیس هنگام خروج
conn.close()