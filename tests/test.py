import os
import subprocess
import sys
import unittest


class TestStudentApp(unittest.TestCase):

    def test_student_information(self):
        env = os.environ.copy()
        env.update({
            "STUDENT_NAME": "Adilet",
            "STUDENT_SURNAME": "Toktarbay",
            "STUDENT_GROUP": "IT2-2306",
            "STUDENT_ID": "37629",
        })

        process = subprocess.Popen(
            [sys.executable, "-u", "app/main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )

        try:
            output = ""
            for _ in range(8):
                output += process.stdout.readline()

            self.assertIn("Name: Adilet", output)
            self.assertIn("Surname: Toktarbay", output)
            self.assertIn("Group: IT2-2306", output)
            self.assertIn("Student ID: 37629", output)
            self.assertIn("Application is running successfully!", output)
        finally:
            process.terminate()
            try:
                process.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.communicate()


if __name__ == "__main__":
    unittest.main()
