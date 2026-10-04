import unittest

from backend.passforge.app import create_app


class TestPasswordAPI(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_health(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "ok")

    def test_generates_password(self):
        response = self.client.post("/api/passwords", json={"length": 24})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["length"], 24)
        self.assertEqual(len(response.json["password"]), 24)
        self.assertIn("estimated_exhaustive_years", response.json)
        self.assertEqual(response.json["guesses_per_second"], 100_000_000_000)

    def test_entropy_estimate_for_minimum_length(self):
        response = self.client.post("/api/passwords", json={"length": 12})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["entropy"], 78.7)
        self.assertGreater(response.json["estimated_exhaustive_years"], 100_000)

    def test_rejects_invalid_options(self):
        response = self.client.post(
            "/api/passwords",
            json={"length": 20, "symbols": "yes"},
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
