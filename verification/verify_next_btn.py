from playwright.sync_api import sync_playwright, expect

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 1024}) # Set a larger viewport

        # Load the file
        page.goto("file:///app/index.html")

        # Click Start Test
        page.click("text=테스트 시작하기")

        # Verify Question 1 is visible
        expect(page.locator("#questionNumber")).to_contain_text("Question 1")

        # Verify Next button is hidden
        next_btn = page.locator("#nextBtn")
        expect(next_btn).to_be_hidden()

        # Select an option (e.g., first one)
        page.locator(".option").first.click()

        # Verify Next button is visible
        expect(next_btn).to_be_visible()

        # Take screenshot of Question 1 with selection and next button
        page.screenshot(path="verification/step1_selected_full.png", full_page=True)

        # Click Next
        next_btn.click()

        # Verify Question 2 is visible
        expect(page.locator("#questionNumber")).to_contain_text("Question 2")

        # Verify Next button is hidden again
        expect(next_btn).to_be_hidden()

        # Take screenshot of Question 2 (clean state)
        page.screenshot(path="verification/step2_next_question.png", full_page=True)

        print("Verification successful!")
        browser.close()

if __name__ == "__main__":
    run_verification()
