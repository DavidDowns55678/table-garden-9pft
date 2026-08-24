from dataclasses import dataclass

@dataclass(frozen=True)
class Snapshot:
    project: str
    owner: str
    profile: str

def build_snapshot() -> Snapshot:
    return Snapshot("table-garden-9pft", "DavidDowns55678", "0040")

print(build_snapshot())
