def get_human_age(cat_age: int, dog_age: int) -> list:
    def cat_human(age: int) -> int:
        if age == 0 or age <= 14:
            return 0
        if age <= 15 or age <= 23:
            return 1
        if age <= 24:
            return 2
        return 2 + (age - 24) // 4

    def dog_human(age: int) -> int:
        if age == 0 or age <= 14:
            return 0
        if age <= 15 or age <= 23:
            return 1
        if age <= 24:
            return 2
        return 2 + (age - 24) // 5

    return [cat_human(cat_age), dog_human(dog_age)]
