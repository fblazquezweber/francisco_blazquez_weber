import shutil
from pathlib import Path

def classify_logs(log_dir: Path, extensions: dict):
    log_dir.mkdir(parents=True, exist_ok=True)  # Crea la carpeta base si no existe
    for ext, folder_name in extensions.items():
        (log_dir / folder_name).mkdir(exist_ok=True)  # Crea subcarpetas App1, App2, etc.
        for log_file in log_dir.glob(f"*{ext}"):
            shutil.move(str(log_file), str(log_dir / folder_name / log_file.name))

# Uso
extensions = {
    ".log_app_1": "App1",
    ".log_app_2": "App2",
    ".log_app_3": "App3"
}

# IMPORTANTE: Usa r"" para evitar problemas con los backslash
ruta_logs = Path(r"D:\IACC\ACTIVIDADES POR CICLO\CICLO VIII\PROIF1301-6-PROCESOS INFORMÁTICOS\Semana 3\logs")
classify_logs(ruta_logs, extensions)
