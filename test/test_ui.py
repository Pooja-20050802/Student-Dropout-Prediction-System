from playwright.sync_api import sync_playwright

def test_student_prediction_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(
            "http://localhost:5500/index.html",
            wait_until="networkidle"
        )

        page.fill("#age", "20")
        page.fill("#admission_grade", "127.3")
        page.fill("#sem1_enrolled", "6")
        page.fill("#sem1_approved", "6")
        page.fill("#sem1_grade", "13.5")
        page.fill("#sem2_enrolled", "6")
        page.fill("#sem2_approved", "5")
        page.fill("#sem2_grade", "12.5")

        page.click("#predictButton")

        page.wait_for_function(
            """() => document.querySelector('#result')
            .textContent.includes('Prediction:')"""
        )

        result = page.locator("#result").text_content()

        print("UI Result:", result)

        assert any(
            prediction in result
            for prediction in ["Dropout", "Enrolled", "Graduate"]
        )

        browser.close()