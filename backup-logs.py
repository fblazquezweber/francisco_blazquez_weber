import zipfile
from datetime import datetime
import os
from pathlib import Path

RUTA_LOGS = Path(r"D:\IACC\ACTIVIDADES POR CICLO\CICLO VIII\PROIF1301-6-PROCESOS INFORMÁTICOS\Semana 3\logs")
RUTA_BACKUPS = Path(r"D:\IACC\ACTIVIDADES POR CICLO\CICLO VIII\PROIF1301-6-PROCESOS INFORMÁTICOS\Semana 3\backups")
DIAS_RETENCION = 30

# Verifica si existe la carpeta de backups
RUTA_BACKUPS.mkdir(parents=True, exist_ok=True)

#Crear backup (incluyendo subcarpetas App1, App2, App3)
fecha = datetime.now().strftime('%Y%m%d')
nombre_backup = f"backup_logs_{fecha}.zip"
ruta_backup_completa = RUTA_BACKUPS / nombre_backup

with zipfile.ZipFile(ruta_backup_completa, 'w') as zipf:
    for app_dir in RUTA_LOGS.iterdir():
        if app_dir.is_dir() and app_dir.name.startswith('App'):
            for archivo in app_dir.glob('*.log_*'):
                # Guardar en el zip
                zipf.write(archivo, arcname=f"{app_dir.name}/{archivo.name}")
    print(f"✅ Backup creado: {nombre_backup}")

#Limpiar backups antiguos
for backup in RUTA_BACKUPS.glob('backup_logs_*.zip'):
    dias = (datetime.now() - datetime.fromtimestamp(backup.stat().st_mtime)).days
    if dias > DIAS_RETENCION:
        backup.unlink()
        print(f"🗑️ Eliminado backup antiguo: {backup.name}")

print("✔️ Proceso completado")