import csv
import os
from colorama import init, Fore
from datetime import date

init(autoreset=True)

FILENAME = "returns.csv"
FIELDS = ["date", "tracking", "reason", "action"]

def save_returns(returns):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(returns)

def load_returns():
    returns = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                returns.append(row)
    return returns

def log_return(returns):
    print(Fore.YELLOW + "\n-- Log a Return --")
    tracking = input("Tracking number: ").strip()
    if not tracking:
        print(Fore.RED + "Tracking number cannot be empty.")
        return
    reason = input("Reason for return: ").strip()
    if not reason:
        print(Fore.RED + "Reason cannot be empty.")
        return
    action = input("Action taken (e.g. contact supplier, re-ship): ").strip()
    today = date.today().strftime("%Y-%m-%d")
    returns.append({"date": today, "tracking": tracking, "reason": reason, "action": action})
    save_returns(returns)
    print(Fore.GREEN + "Return logged!")

def view_returns(returns):
    if not returns:
        print(Fore.RED + "\nNo returns logged yet.")
        return
    print(Fore.YELLOW + "\n--- Return Tracker ---")
    print(f"{'DATE':<12}{'TRACKING':<20}{'REASON':<30}ACTION")
    print("-" * 75)
    for r in returns:
        print(f"{Fore.WHITE}{r['date']:<12}{r['tracking']:<20}{r['reason']:<30}{r['action']}")

if __name__ == "__main__":
    returns = load_returns()
    view_returns(returns)