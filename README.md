# projekt-VehicleShop
This code appears to be implementing a VehicleShop class that reads vehicles from a CSV file, displays them, allows a user to select a vehicle for sale, and then updates the vehicle list accordingly.
# Vehicle Shop Application

Ky është një aplikacion Python që simulon një dyqan makinash, ku përdoruesit mund të shohin makinat në dispozicion, të zgjedhin një makinë për ta shitur, dhe të përditësojnë listën e makinave.

## Teknologjitë e përdorura:
- Python
- CSV për ruajtjen dhe përpunimin e të dhënave

## Struktura e Projektit:
```plaintext
VehicleShop/
│
├── vehicle-list.csv            # Skedari hyrës që përmban listën e makinave.
├── vehicle_shop.py             # Skedari kryesor ku implementohet klasa VehicleShop.
├── VehicleFileManager.py        # Klasa për menaxhimin e operacioneve të skedarëve CSV.
├── VehicleShopPrinter.py        # Klasa për shfaqjen e informacionit në konsolë.
├── VehicleShopProcessor.py      # Klasa për përpunimin e logjikës së shitjes së makinave.
├── VehicleTransformer.py        # Klasa për transformimin e të dhënave nga string në objekte Python.
├── README.md                    # Skedari i dokumentacionit (ky skedar).
