from dataclasses import dataclass, field


@dataclass
class Category:
    id: int
    name: str
    description: str = field(default="")

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.name:
            raise ValueError("Name cannot be empty.")
