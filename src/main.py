# === imports ===
from src.punto import punto

def main():
    print(("===prueba de la clase punto==="))
    punto1 = punto(3,2)
    print("punto: ", punto1.opuesto())
    pass

if __name__ == "__main__":
    main()
