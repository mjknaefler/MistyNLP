import requests
import json

class MistyAPI:
    def __init__(self, ip):
        self.base_url = f"http://{ip}/api"

    def speak(self, text):
        url = f"{self.base_url}/tts/speak"
        data = {"text": text}
        response = requests.post(url, json=data)
        return self._handle_response(response)

    def listen(self, capture_duration=5000):
        url = f"{self.base_url}/audio/capture"
        data = {"CaptureDuration": capture_duration}  # Time in milliseconds
        response = requests.post(url, json=data)
        return self._handle_response(response)

    def get_audio_file(self, filename):
        url = f"{self.base_url}/audio?FileName={filename}"
        response = requests.get(url)
        return self._handle_response(response, is_binary=True)

    def _handle_response(self, response, is_binary=False):
        if response.status_code == 200:
            return response.content if is_binary else response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None


if __name__ == "__main__":
    misty = MistyAPI("192.168.1.125")  # Replace with Misty's actual IP

    response = misty.speak("Hello! I am Misty!")
    print(response)

    response = misty.listen()
    print(response)
