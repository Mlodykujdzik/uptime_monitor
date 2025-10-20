import platform
import subprocess
import sys

def ping(host: str, count: int = 1):
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
    host = "kujdzik.pl" if len(sys.argv) == 1 else sys.argv[1]
    code, out = ping(host)
    print("Kod wyjścia:", code)
    print(out)