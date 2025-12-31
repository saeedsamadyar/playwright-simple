from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        # تنظیمات مخصوص مک High Sierra
        browser = p.chromium.launch(
            headless=False,
            channel="chrome",
            args=["--disable-gpu", "--no-sandbox"]
        )
        context = browser.new_context()
        page = context.new_page()

        try:
            # ۱. رفتن به گوگل
            print("Trying to open google")
            page.goto("https://www.google.com")

            # ۲. پیدا کردن باکس جستجو و تایپ کلمه (Selector: name='q')
            print("🔍 در حال جستجوی کلمه 'Python Playwright'...")
            page.fill('input[name="q"]', "Python Playwright")
            
            # ۳. فشردن دکمه اینتر
            page.press('input[name="q"]', "Enter")

            # ۴. صبر کردن برای لود شدن نتایج
            page.wait_for_selector('h3') 

            # ۵. کلیک روی اولین تیتر (h3) که در نتایج ظاهر می‌شود
            print("🖱 کلیک روی اولین نتیجه جستجو...")
            page.click('h3')

            # ۶. صبر برای لود شدن سایت مقصد و گرفتن اسکرین‌شات
            time.sleep(5) 
            page.screenshot(path="first_result.png")
            print(f"✅ با موفقیت وارد سایت شدیم. اسکرین‌شات ذخیره شد.")

        except Exception as e:
            print(f"❌ خطا در سناریو: {e}")
            
        finally:
            print("⏳ ۶۰ ثانیه فرصت برای بررسی دستی...")
            time.sleep(60)
            browser.close()

if __name__ == "__main__":
    run()