import os
from datetime import datetime


# Stateless utility class; callers can capture screenshots without creating an instance.
class Screenshot:

    @staticmethod
    def capture(driver, name):

        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_path = os.path.join(folder, f"{name}_{timestamp}.png")

        driver.save_screenshot(file_path)

        print(f"Screenshot saved at: {file_path}")

        return file_path