import platform
import subprocess
import sys
import argparse

def ping(host: str, count: int):
    system = platform.system().lower()
    if system == "windows":
        cmd = ["ping", "-n", str(count), host]
    else:
        cmd = ["ping", "-c", str(count), host]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return res.returncode, res.stdout
    except Exception as e:
        return 2, str(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prosty ping w Pythonie.")
    parser.add_argument("--url", "-u", nargs="?", default="kujdzik.pl", help="Adres hosta do spingowania.")
    parser.add_argument("--count", "-c", nargs="?", type=int, default=1, help="Ilość pakietów do wysłania.")
    args = parser.parse_args()

    code, out = ping(args.url, args.count)
    print("Kod wyjścia:", code)
    print(out)