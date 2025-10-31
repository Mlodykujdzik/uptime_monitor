import platform
import subprocess
import sys
import argparse
import re

def ping(host: str, count: int):
    system = platform.system().lower()
    if system == "windows":
        cmd = ["ping", "-n", str(count), host]
    else:
        cmd = ["ping", "-c", str(count), host]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=False)
        output = res.stdout
        if system == "windows":
            match = re.search(r"Average = (\d+)ms", output)
        else:
            match = re.search(r" = [\d\.]+/([\d\.]+)", output)
        avg_time = match.group(1) if match else "?"
        ok = res.returncode == 0
        return {
            "host": host,
            "ok": ok,
            "avg_time_ms": avg_time,
            "code": res.returncode,
        }
    except Exception as e:
        return {"host": host, "ok": False, "error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prosty ping w Pythonie.")
    parser.add_argument("--url", "-u", nargs="?", default="kujdzik.pl", help="Adres hosta do spingowania.")
    parser.add_argument("--count", "-c", nargs="?", type=int, default=1, help="Ilość pakietów do wysłania.")
    args = parser.parse_args()

    result = ping(args.url, args.count)

    if result["ok"]:
        print(f" {result['host']} działa (średni czas: {result['avg_time_ms']} ms)")
    else:
        print(f" {result['host']} niedostępny")
        if "error" in result:
            print("Błąd:", result["error"])