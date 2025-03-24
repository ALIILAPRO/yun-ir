<div dir="rtl">

# کلاینت پایتون برای Yun.ir

یک کلاینت پایتون برای API سرویس کوتاه‌کننده لینک [Yun.ir](https://yun.ir/)

---

## نصب

نصب با استفاده از `pip`:

```sh
pip install yun-ir
```

---

## نحوه استفاده

```python
from yun import Yun

login = Yun.Api('YOUR tOKEN')  # توکن API خود را وارد کنید
result = login.short('title', 'url')  # به جای 'title' و 'url' مقادیر دلخواه را وارد کنید

print(result)  # نتیجه را چاپ می‌کند
```

---

## مستندات API

### `yun_ir.Yun(token: str)`

ساخت یک نمونه از کلاینت Yun.ir

**پارامترها:**
- `token`: توکن API شما در Yun.ir

---

### `yun_ir.Yun.short(title: str, url: str) -> dict`

کوتاه‌کردن یک لینک با استفاده از API یون

**پارامترها:**
- `title`: عنوان لینک
- `url`: لینکی که می‌خواهید کوتاه شود

**خروجی:**
- یک دیکشنری شامل لینک کوتاه‌شده یا پیام خطا (در صورت بروز خطا)

---

> حتماً باید یک توکن معتبر از [Yun.ir](https://yun.ir/) دریافت کرده باشید.

</div>

---

# Yun.ir Python Client

A Python client for the [Yun.ir](https://yun.ir/) URL shortener API.

---

## Installation

Install with `pip`:

```sh
pip install yun-ir
```

---

## Usage

```python
from yun import Yun

login = Yun.Api('YOUR tOKEN')
result = login.short('title', 'url')

print(result)
```

---

## API

### `yun_ir.Yun(token: str)`

Create a new Yun.ir client instance.

**Parameters:**
- `token`: Your Yun.ir API token

---

### `yun_ir.Yun.short(title: str, url: str) -> dict`

Shorten a URL using Yun.ir API.

**Parameters:**
- `title`: Title for the URL
- `url`: URL to shorten

**Returns:**
- A dictionary containing the shortened URL, or an error message if the request fails.

---

> Make sure you have a valid API token from [Yun.ir](https://yun.ir/)
