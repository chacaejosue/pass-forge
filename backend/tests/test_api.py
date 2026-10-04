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

    def test_rejects_invalid_options(self):
        response = self.client.post(
            "/api/passwords",
            json={"length": 20, "symbols": "yes"},
        )
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
