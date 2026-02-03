from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional


class FailureMode(str, Enum):
    """
    In custody terms, failure is not 'a bug' — it is loss of control.
    """
    NONE = "none"
    LEAKAGE = "leakage"   # secret copied / control compromised
    LOSS = "loss"         # secret unavailable to rightful owner


@dataclass
class CustodyState:
    """
    Models custody of a private digital secret WITHOUT storing the secret.

    Key idea:
    - the secret is an atomic control point
    - control is a living state that can degrade silently over time
    """

    # High-level control (0.0 = no control, 1.0 = full control)
    control: float = 1.0

    # Exposure risk (0.0 = no exposure, 1.0 = fully exposed)
    exposure: float = 0.0

    # Can the owner still recover control *by design* (not by luck)?
    recoverable: bool = True

    # When was custody last explicitly verified by the owner/system?
    last_verified_day: int = 0

    # A narrative label for what failed (useful for reporting)
    failure_mode: FailureMode = FailureMode.NONE

    # Track key assumptions that often break in real life
    assumptions: Dict[str, bool] = field(default_factory=lambda: {
        "owner_has_full_memory": True,
        "owner_has_device_access": True,
        "owner_behaves_consistently": True,
        "succession_exists": False,
    })

    def clamp(self) -> None:
        self.control = max(0.0, min(1.0, self.control))
        self.exposure = max(0.0, min(1.0, self.exposure))

    def mark_verified(self, day: int) -> None:
        self.last_verified_day = day

    def set_failure(self, mode: FailureMode) -> None:
        # failure is terminal once control collapses
        if self.failure_mode == FailureMode.NONE:
            self.failure_mode = mode

    def is_catastrophic(self) -> bool:
        """
        Catastrophic = control lost OR secret effectively unusable.
        """
        return self.control <= 0.0 or self.failure_mode != FailureMode.NONE
