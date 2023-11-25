from silver_service_taxi import SilverServiceTaxi

silver_taxi = SilverServiceTaxi("Hummer", 200, 4)
lindsay_taxi = SilverServiceTaxi("A silver service taxi", 100, 2)
print(silver_taxi)
silver_taxi.drive(40)
print(f"{silver_taxi} Total: ${silver_taxi.get_fare():.2f}")

print(lindsay_taxi)
lindsay_taxi.drive(18)
print(f"{lindsay_taxi} Total: ${lindsay_taxi.get_fare():.2f}")  # the fare should be $48.78 (yikes!)
