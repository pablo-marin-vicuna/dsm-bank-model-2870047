import subprocess

def install_packages(requirements_file, error_log_file):
    with open(requirements_file, 'r') as file:
        packages = file.readlines()
    
    with open(error_log_file, 'w') as error_log:
        for package in packages:
            package = package.strip()
            if package:
                print(f"Installing {package}...")
                result = subprocess.run(['pip', 'install', package], capture_output=True, text=True)
                if result.returncode != 0:
                    error_log.write(f"Failed to install {package}. Error:\n{result.stderr}\n")
                    print(f"Failed to install {package}. See {error_log_file} for details.")

if __name__ == "__main__":
    install_packages("requirements.txt", "install_errors.log")
