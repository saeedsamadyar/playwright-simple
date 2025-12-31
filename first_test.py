from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        print("در حال تلاش برای باز کردن گوگل کروم...")
        
        # تنظیمات مخصوص برای اجرای پایدار در مک قدیمی
        browser = p.chromium.launch(
            headless=False,
            channel="chrome", 
            args=[
                "--disable-gpu", 
                "--disable-software-rasterizer",
                "--no-sandbox"
            ]
        )
        
        # ایجاد Context برای قابلیت ضبط Trace
        context = browser.new_context()
        
        # شروع ضبط تراک
        context.tracing.start(screenshots=True, snapshots=True)
        
        page = context.new_page()

        try:
            # رفتن به گوگل (عدد تایم اوت اصلاح شد)
            page.goto("https://www.google.com", timeout=60000)
            
            # انجام یک جستجو برای اینکه تراک جذاب‌تر شود
            page.fill('input[name="q"]', "Playwright Python Trace")
            page.press('input[name="q"]', "Enter")
            
            print(f"✅ سایت باز شد. عنوان صفحه: {page.title()}")
            
        except Exception as e:
            print(f"❌ خطا رخ داد: {e}")
            
        finally:
            # پایان ضبط و ذخیره فایل برای trace.playwright.dev
            context.tracing.stop(path="trace.zip")
            print("✅ فایل trace.zip با موفقیت ذخیره شد.")
            
            # ۶۰ ثانیه انتظار قبل از بسته شدن
            print("⏳ ۶۰ ثانیه صبر می‌کنم تا صفحه را بررسی کنید...")
            time.sleep(60)
            
            browser.close()

if __name__ == "__main__":
    run()