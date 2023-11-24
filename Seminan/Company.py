# Если все компании прибыльные веруть истину, а если хотябы одна убыточная вернуть ложь

def company(name_company: dict[str, float | int]) -> bool:
    for key, value in name_company.items():
        if sum(value) < 0:
            return False
        return True
    #return all(map(lambda  x : sum(x) > 0, name_company.values()))
    
data = {
    "Roga": [42, 73, 12, 85, -15, 2],
    "Kopieta": [45, -25, 100, 22, 1],
    "Hvostie": [500, -123, 52, 45, 93]
}

print(company(data))
