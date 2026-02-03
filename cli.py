from simulator.engine import CustodySimulator, TimelineEvent
from simulator.events import FailureEvent

def main() -> None:
    sim = CustodySimulator()
    sim.state.mark_verified(day=0)

    timeline = [
        TimelineEvent(day=7, event=FailureEvent.SCREENSHOT_SEED),
        TimelineEvent(day=45, event=FailureEvent.INFOSTEALER),
        TimelineEvent(day=120, event=FailureEvent.STRESS_ERROR),
    ]

    final_state = sim.run(timeline)

    print("=== FINAL STATE ===")
    print(final_state)
    print("\n=== LOG ===")
    for line in sim.log:
        print("-", line)

if __name__ == "__main__":
    main()
PY


