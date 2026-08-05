import platform
import socket
import time
import psutil


def get_metrics():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    uptime = (time.time() - psutil.boot_time()) / 3600

    return {
        "cpu": {
            "usage_percent": psutil.cpu_percent(interval=1),
            "cores": psutil.cpu_count(),
        },
        "memory": {
            "used_gb": round(memory.used / (1024**3), 2),
            "total_gb": round(memory.total / (1024**3), 2),
            "percent": memory.percent,
        },
        "disk": {
            "used_gb": round(disk.used / (1024**3), 2),
            "total_gb": round(disk.total / (1024**3), 2),
            "percent": disk.percent,
        },
        "system": {
            "hostname": socket.gethostname(),
            "platform": platform.system(),
            "platform_version": platform.release(),
            "uptime_hours": round(uptime, 2),
        },
    }


def get_health():
    return {"status": "healthy"}


def get_service_info():
    return {
        "service": "Infrastructure Monitoring Service",
        "status": "running",
        "version": "1.0.0",
    }
