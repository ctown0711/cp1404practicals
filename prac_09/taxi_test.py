from taxi import Taxi

my_taxi = Taxi("Prius 1", 100)
my_taxi.drive(40)
print(f"{my_taxi}, Total: ${my_taxi.get_fare()}")
my_taxi.start_fare()
my_taxi.drive(100)
print(f"{my_taxi}, Total: ${my_taxi.get_fare()}")
