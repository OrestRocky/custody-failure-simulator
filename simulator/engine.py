from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

from simulator.state import CustodyState, FailureMode
from simulator.events import FailureEvent


@dataclass
class TimelineEvent:
    day: int
    event: FailureEvent


class CustodySimulator:
    """
    Applies events to a custody state.

    Principle:
    - leakage can be silent and delayed
    - loss can be accidental but equally terminal
    """

    def __init__(self, state: CustodyState | None = None) -> None:
        self.state = state or CustodyState()
        self.log: List[str] = []

    def apply(self, day: int, event: FailureEvent) -> None:
        s = self.state

        # Baseline drift: if not verified for long time, exposure becomes more dangerous.
        days_since_verify = max(0, day - s.last_verified_day)
        if days_since_verify > 30:
            s.exposure += 0.01 * (days_since_verify / 30)

        # Event impacts (kept simple but truthful)
        if event in {FailureEvent.PHISHING, FailureEvent.INFOSTEALER, FailureEvent.CLOUD_SYNC_LEAK, FailureEvent.SCREENSHOT_SEED}:
            # Silent compromise increases exposure immediately,
            # but control may not drop until attacker acts.
            s.exposure += 0.35
            self.log.append(f"Day {day}: leakage vector introduced ({event}). Exposure ↑.")

        elif event in {FailureEvent.DEVICE_THEFT, FailureEvent.DEVICE_FAILURE}:
            # If custody was device-dependent, control collapses.
            s.assumptions["owner_has_device_access"] = False
            s.control -= 0.45
            self.log.append(f"Day {day}: device disruption ({event}). Control ↓.")

        elif event == FailureEvent.MEMORY_DECAY:
            s.assumptions["owner_has_full_memory"] = False
            s.control -= 0.25
            self.log.append(f"Day {day}: memory reliability degraded. Control ↓.")

        elif event == FailureEvent.STRESS_ERROR:
            s.assumptions["owner_behaves_consistently"] = False
            s.control -= 0.20
            s.exposure += 0.10
            self.log.append(f"Day {day}: stress-driven operational error. Control ↓, Exposure ↑.")

        elif event == FailureEvent.DEATH_NO_SUCCESSION:
            # Human discontinuity without succession is terminal loss.
            if not s.assumptions.get("succession_exists", False):
                s.control = 0.0
                s.recoverable = False
                s.set_failure(FailureMode.LOSS)
                self.log.append(f"Day {day}: human discontinuity without succession. Terminal LOSS.")

        # Catastrophic conversion rule:
        # if exposure is high enough, assume attacker eventually acts -> control collapses (leakage becomes loss-of-control).
        if s.failure_mode == FailureMode.NONE and s.exposure >= 0.85:
            s.control = 0.0
            s.recoverable = False
            s.set_failure(FailureMode.LEAKAGE)
            self.log.append(f"Day {day}: exposure threshold crossed. LEAKAGE becomes terminal loss-of-control.")

        s.clamp()

    def run(self, timeline: List[TimelineEvent]) -> CustodyState:
        for t in sorted(timeline, key=lambda x: x.day):
            if self.state.is_catastrophic():
                break
            self.apply(t.day, t.event)
        return self.state
