import random
import time
import csv
from datetime import datetime

LOG_FILE = "detections_log.csv"


class SensorSimulator:
    """
    Simulates a metal detection sensor.
    In real life, this could be replaced with serial input from Arduino.
    """

    def read_value(self) -> int:
        """
        Returns a fake sensor reading between 0 and 1023.
        Metal-like spikes are simulated with higher probability sometimes.
        """
        base = random.randint(50, 300)

        # Occasionally simulate a "metal" spike
        if random.random() < 0.2:  # 20% chance
            base += random.randint(300, 700)

        return min(base, 1023)


class MetalDetector:
    def __init__(self, threshold: int = 500, delay: float = 0.5):
        self.threshold = threshold
        self.delay = delay
        self.sensor = SensorSimulator()

    def is_metal_detected(self, value: int) -> bool:
        return value >= self.threshold

    def log_detection(self, value: int):
        """
        Logs detection time and sensor value into a CSV file.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # If file doesn't exist, write header
        try:
            file_exists = False
            with open(LOG_FILE, "r"):
                file_exists = True
        except FileNotFoundError:
            file_exists = False

        with open(LOG_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Timestamp", "Sensor Value"])
            writer.writerow([timestamp, value])

    def start_monitoring(self):
        print("\n--- Starting Metal Detection ---")
        print("Press Ctrl + C to stop.\n")

        try:
            while True:
                value = self.sensor.read_value()
                metal = self.is_metal_detected(value)

                if metal:
                    status = "METAL DETECTED ⚠"
                else:
                    status = "Safe"

                print(f"Sensor Value: {value:4d} | Status: {status}")

                if metal:
                    self.log_detection(value)

                time.sleep(self.delay)

        except KeyboardInterrupt:
            print("\nStopped monitoring. Returning to menu...\n")


def print_menu():
    print("======== METAL ITEM DETECTOR ========")
    print("1. Start monitoring")
    print("2. Change detection threshold")
    print("3. View recent detection logs")
    print("4. Exit")
    print("=====================================")


def change_threshold(detector: MetalDetector):
    print(f"\nCurrent threshold: {detector.threshold}")
    try:
        new_th = int(input("Enter new threshold (0 - 1023): "))
        if 0 <= new_th <= 1023:
            detector.threshold = new_th
            print(f"Threshold updated to {detector.threshold}\n")
        else:
            print("Invalid value. Threshold not changed.\n")
    except ValueError:
        print("Invalid input. Threshold not changed.\n")


def view_logs(limit: int = 10):
    print("\n--- Recent Metal Detections ---")
    try:
        with open(LOG_FILE, mode="r") as file:
            reader = list(csv.reader(file))
            if len(reader) <= 1:
                print("No detections logged yet.\n")
                return

            header = reader[0]
            rows = reader[1:]

            # Show last `limit` detections
            for row in rows[-limit:]:
                print(f"Time: {row[0]} | Sensor Value: {row[1]}")
            print()
    except FileNotFoundError:
        print("No log file found. No detections recorded yet.\n")


def main():
    detector = MetalDetector(threshold=500, delay=0.5)

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            detector.start_monitoring()
        elif choice == "2":
            change_threshold(detector)
        elif choice == "3":
            view_logs()
        elif choice == "4":
            print("Exiting Metal Item Detector. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
