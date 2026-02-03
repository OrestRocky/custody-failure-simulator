from enum import Enum


class FailureEvent(str, Enum):
    """
    Real-world recurring patterns.
    """
    PHISHING = "phishing"
    INFOSTEALER = "infostealer"
    DEVICE_THEFT = "device_theft"
    DEVICE_FAILURE = "device_failure"
    BAD_BACKUP = "bad_backup"
    SCREENSHOT_SEED = "screenshot_seed"
    CLOUD_SYNC_LEAK = "cloud_sync_leak"
    MEMORY_DECAY = "memory_decay"
    DEATH_NO_SUCCESSION = "death_no_succession"
    STRESS_ERROR = "stress_error"
