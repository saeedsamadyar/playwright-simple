from playwright.sync_api import sync_playwright

def check_setup():
    print("در حال تست ارتباط پایتون و پلی‌رایت...")
    
    with sync_playwright() as p:
        # ۱. باز کردن مرورگر کرومیوم
        # اگر این مرحله خطا ندهد، یعنی نصب مرورگرها درست بوده است
        browser = p.chromium.launch(headless=False) 
        
        page = browser.new_page()

        try:
            # ۲. تلاش برای باز کردن سایت
            page.goto("https://www.google.com", timeout=30000)
            
            # ۳. خواندن عنوان صفحه
            title = page.title()
            
            # چاپ نتیجه با رنگ سبز
            print("\033[92m" + "✅ ارتباط با موفقیت برقرار شد!" + "\033[0m")
            print(f"عنوان صفحه باز شده: {title}")
            
        except Exception as e:
            print("\033[91m" + "❌ خطا در برقراری ارتباط:" + "\033[0m")
            print(e)
            
        finally:
            browser.close()

if __name__ == "__main__":
    check_setup()