from unreliable_car import UnreliableCar

reliable_car = UnreliableCar("Lada", 120, 95)
unreliable_car = UnreliableCar("Camry", 120, 35.6)

print(unreliable_car)
unreliable_car.drive(45)
print(unreliable_car)
unreliable_car.drive(30)
print(unreliable_car)

print(reliable_car)
reliable_car.drive(45)
print(reliable_car)
reliable_car.drive(30)
print(reliable_car)
