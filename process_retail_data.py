import pandas as pd
import os


def load_and_clean_sales(file_path):
    """بارگذاری و پاکسازی داده‌های فروش پوشاک"""
    try:
        # فرض بر این است که فایل‌ها اکسل هستند
        df = pd.read_excel(file_path)

        # ۱. حذف ردیف‌های کاملاً خالی
        df = df.dropna(how='all')

        # ۲. پر کردن مقادیر خالی در ستون‌های عددی با صفر
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].fillna(0)

        # ۳. اطمینان از فرمت صحیح تاریخ (اگر ستون تاریخ وجود داشته باشد)
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])

        return df
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None


def generate_summary(df):
    """ایجاد گزارش ساده از عملکرد فروش"""
    summary = {
        "Total_Transactions": len(df),
        "Total_Revenue": df['Amount'].sum() if 'Amount' in df.columns else 0,
        "Unique_Products": df['Product_ID'].nunique() if 'Product_ID' in df.columns else 0
    }
    return summary


if __name__ == "__main__":
    # مسیر داده‌ها
    data_file = 'data/Sales_1.xlsx'  # فایل نمونه شما

    if os.path.exists(data_file):
        print("Starting Data Transformation Pipeline...")
        df_final = load_and_clean_sales(data_file)

        if df_final is not None:
            stats = generate_summary(df_final)
            print("-" * 30)
            print("PIPELINE COMPLETE: Retail Data Insights")
            print(f"Total Transactions: {stats['Total_Transactions']}")
            print(f"Total Revenue: {stats['Total_Revenue']}")
            print("-" * 30)

            # ذخیره خروجی
            df_final.to_csv('data/cleaned_sales_report.csv', index=False)
            print("Cleaned data saved to 'data/cleaned_sales_report.csv'")
    else:
        print(f"File {data_file} not found. Please check your data directory.")
