kor_01 = {
    "kozeppont" : (2, 5),
    "sugar" : 10
}

def terulet(kor):
    return kor["sugar"] * pow(3.14, 2)

def kerulet(kor):
    return kor["sugar"] * 2 * 3.14

print("A kör kerülete:", kerulet(kor_01), "egység.")
print("A kör területe:", terulet(kor_01), "egység.")
# print(f"A kör kerülete: {kerulet(kor_01)} egység.")
# print(f"A kör területe: {terulet(kor_01)} egység.")