import json
import os
from cryptography.fernet import Fernet
from pathlib import Path

# Constants for configuration
CONFIG_DIR = Path(__file__).parent.parent  # Points to the project root directory
CONFIG_FILE = CONFIG_DIR / "config.json"
BACKUP_CONFIG_FILE = CONFIG_DIR / "config_backup.json"
ENCRYPTION_KEY = os.environ.get("CONFIG_ENCRYPTION_KEY", Fernet.generate_key())  # Ideally, this key should be stored securely
cipher_suite = Fernet(ENCRYPTION_KEY)

def load_config():
    """
    Load and decrypt configuration from a JSON file.
    
    Returns:
    - dict: Contains configuration settings. If no configuration file found, returns default settings.
    """
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r') as file:
                encrypted_data = file.read()
                decrypted_data = cipher_suite.decrypt(encrypted_data.encode()).decode()
                config = json.loads(decrypted_data)
                
                # Validation
                if not validate_config(config):
                    return default_config()
                return config
        except (json.JSONDecodeError, ValueError):
            return default_config()
    else:
        return default_config()

def save_config(config):
    """
    Backup the old configuration, then encrypt and save the new configuration to a JSON file.
    
    Args:
    - config (dict): Contains configuration settings.
    """
    # Backup old configuration
    if CONFIG_FILE.exists():
        os.rename(CONFIG_FILE, BACKUP_CONFIG_FILE)
        
    encrypted_data = cipher_suite.encrypt(json.dumps(config).encode()).decode()
    with open(CONFIG_FILE, 'w') as file:
        file.write(encrypted_data)

def validate_config(config):
    """
    Validate the configuration dictionary to ensure all necessary keys are present.
    
    Args:
    - config (dict): Configuration to validate.
    
    Returns:
    - bool: True if valid, else False.
    """
    required_keys = ["database", "email", "smtp_server", "scan_frequency"]
    return all(key in config for key in required_keys)

def default_config():
    """
    Default configuration settings for the IDS-Lite system.
    
    Returns:
    - dict: Contains default configuration settings.
    """
    return {
        "database": os.environ.get("DEFAULT_DB_PATH", "default_db_path"),
        "email": os.environ.get("DEFAULT_ALERT_EMAIL", "alert@example.com"),
        "smtp_server": os.environ.get("DEFAULT_SMTP_SERVER", "smtp.example.com"),
        "scan_frequency": 10
    }

# For testing purposes
if __name__ == "__main__":
    config = load_config()
    print(config)
    config["database"] = "new_db_path"
    save_config(config)