## 🔄 Batch Processing & Merging Module

This module is engineered to automate the handling of a large volume of financial reports stored in separate Excel files. Instead of processing each file individually, this script automatically detects, cleans, and merges all files within a specified input directory into a unified Master Dataset.

### 💡 Key Features
*   **Auto-Discovery:** Automatically detects all `.xlsx` and `.xls` files in the designated input path.
*   **Intelligent Sheet Integration:** Capable of intelligently processing files 
## 🔄 ماژول ادغام و پردازش دسته‌ای (Batch Processing & Merging)

این ماژول برای مدیریت خودکار حجم انبوهی از گزارش‌های مالی که در فایل‌های اکسل مجزا ذخیره شده‌اند، طراحی شده است. به جای پردازش تک‌به‌تک، این اسکریپت به صورت خودکار تمام فایل‌های موجود در پوشه ورودی را شناسایی، پاکسازی و در یک پایگاه داده یکپارچه (Master Dataset) ادغام می‌کند.

### 💡 ویژگی‌های کلیدی
*   **تشخیص خودکار (Auto-Discovery):** شناسایی تمام فایل‌های `.xlsx` و `.xls` موجود در مسیر تعیین شده.
*   **یکپارچه‌سازی شیت‌ها:** قابلیت پردازش هوشمند فایل‌هایی که دارای چندین شیت هستند (مانند `Sales_Sheets.xlsx`).
*   **ردیابی منبع (Lineage Tracking):** افزودن ستون‌های `source_file` و `source_sheet` به هر ردیف برای اطمینان از قابلیت ردیابی داده (Data Lineage).
*   **پاکسازی هوشمند در سطح کلان:** اجرای توابع استانداردسازی برای تمام فایل‌ها پیش از ادغام، به منظور جلوگیری از بروز خطا در فرمت داده‌ها (مانند تفاوت در نام‌گذاری ستون‌ها).
*   **مانیتورینگ حرفه‌ای:** ثبت تمام وقایع، هشدارها و خطاهای احتمالی در فایل `merging.log` جهت عیب‌یابی سریع.

### 🛠 نحوه استفاده

1.  **آماده‌سازی فایل‌ها:**
    تمام فایل‌های گزارش بانکی خود را در مسیر زیر قرار دهید:
    `data/raw_banking_files/`

2.  **اجرای عملیات ادغام:**
    اسکریپت `merge_banking_data.py` را از پوشه `scripts/` اجرا کنید:
```bash
python scripts/merge_banking_data.py

