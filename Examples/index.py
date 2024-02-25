class Div:
    def __hash__(self) -> int:
        return id(self)

    def __repr__(self) -> str:
        return f"<div></div>"


print({Div(): 1, Div(): 2})
