from dataclasses import asdict, dataclass, replace

@dataclass(frozen = True)
class Config:
    lr: float = 0.01
    epochs: int = 100
    layers: tuple[int, ...] = (64,32)

    def __post_init__(self):
        if self.lr <= 0:
            raise ValueError("lr phải lớn hơn 0!")

c1 = Config();
c2 = replace(c1, lr = 0.001)

print("c1:", c2);
print("c2:", c2)
print("c1 == c2:", c1 == c2)
print("Dạng dict để lưu JSON:", asdict(c2))