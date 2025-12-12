# ======================================
# 🌐 Flask Server برای مدیریت پرداخت زرین‌پال
# ======================================

from flask import Flask, request, jsonify
import json, requests

# ================================
# 🧾 اطلاعات شناسایی زرین‌پال (Sandbox)
# ================================
app = Flask(__name__)
MERCHANT = '12345678-1234-1234-1234-123456789012'  # شناسه تستی زرین‌پال
ZP_API_VERIFY = "https://sandbox.zarinpal.com/pg/v4/payment/verify.json"

# ======================================================
# 🧠 حافظه موقتی برای نگهداری authority و مبلغ پرداختی
# ======================================================
payment_sessions = {}

# =====================================================
# 💾 مسیر ذخیره سشن پرداخت
# آدرس: /save-session
# متد: POST
# ورودی‌ها: authority و amount
# عملکرد: ذخیره مقدار پرداختی بر اساس شناسه پرداخت
# =====================================================
@app.route("/save-session", methods=["POST"])
def save_session():
    authority = request.form.get("authority") or request.json.get("authority")
    amount = request.form.get("amount") or request.json.get("amount")

    try:
        amount = int(amount)
    except:
        return jsonify({"error": "amount is not valid int"}), 400

    if authority and amount > 0:
        payment_sessions[authority] = amount
        print(f"📌 سشن ذخیره شد: {authority} = {amount}")
        return jsonify({"status": "saved"}), 200
    else:
        return jsonify({"error": "invalid data"}), 400

# =====================================================
# ✅ مسیر تأیید پرداخت از سمت زرین‌پال
# آدرس: /verify
# متد: GET
# ورودی‌ها: Authority و Status
# عملکرد: ارسال درخواست تأیید به زرین‌پال و نمایش نتیجه
# =====================================================
@app.route("/verify")
def verify_payment():
    authority = request.args.get("Authority")
    status = request.args.get("Status")

    if not authority or not status:
        return "❌ پارامتر ناقص"

    if status != "OK":
        return "❌ پرداخت توسط کاربر لغو شد"

    amount = payment_sessions.get(authority)
    if not amount:
        return f"❌ مبلغ برای authority {authority} یافت نشد"

    print(f"📥 تایید پرداخت برای {authority} با مبلغ {amount}")

    payload = {
        "merchant_id": MERCHANT,
        "amount": amount,
        "authority": authority
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        res = requests.post(ZP_API_VERIFY, data=json.dumps(payload), headers=headers)
        print("📩 وضعیت HTTP:", res.status_code)
        print("📩 پاسخ متنی:", res.text)
        data = res.json()

        if data.get("data", {}).get("code") == 100:
            return f"✅ پرداخت موفق - کد پیگیری: {data['data']['ref_id']}"
        else:
            return f"❌ پرداخت ناموفق - کد: {data['data'].get('code')}"

    except Exception as e:
        return f"❌ خطا در ارتباط: {str(e)}"

# =======================
# ▶️ اجرای سرور
# =======================
if __name__ == "__main__":
    app.run(port=5000)