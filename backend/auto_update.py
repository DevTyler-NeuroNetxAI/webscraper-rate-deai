import subprocess
import sys
import os
from datetime import datetime

def update_python_packages():
    print(f"[{datetime.now()}] Updating Python packages...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "-r", "requirements.txt"], check=True)
    with open("requirements.txt", "w") as f:
        freeze = subprocess.check_output([sys.executable, "-m", "pip", "freeze"]).decode()
        f.write(freeze)

def update_node_packages(frontend_path):
    print(f"[{datetime.now()}] Updating Node packages in {frontend_path}...")
    subprocess.run(["npm", "install", "-g", "npm"], check=True)
    subprocess.run(["npm", "update"], cwd=frontend_path, check=True)

def run_python_tests():
    print(f"[{datetime.now()}] Running Python tests...")
    result = subprocess.run(["pytest"], cwd="backend")
    return result.returncode == 0

def run_node_tests(frontend_path):
    print(f"[{datetime.now()}] Running Node tests...")
    result = subprocess.run(["npm", "test"], cwd=frontend_path)
    return result.returncode == 0

def main():
    try:
        backend_path = os.path.dirname(os.path.abspath(__file__))
        frontend_path = os.path.join(os.path.dirname(backend_path), "frontend")
        
        update_python_packages()
        update_node_packages(frontend_path)
        
        py_tests = run_python_tests()
        node_tests = run_node_tests(frontend_path)
        
        if not py_tests or not node_tests:
            print("[ERROR] Some tests failed after update. Please review manually.")
        
        print(f"[{datetime.now()}] Auto-update completed.")
    except Exception as e:
        print(f"[ERROR] Auto-update failed: {e}")

if __name__ == "__main__":
    main()