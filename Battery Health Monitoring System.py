# Battery Health Monitoring System
# EEE Mini Project - Python

class BatteryHealthMonitor:

    def __init__(self, rated_capacity):
        self.rated_capacity = rated_capacity

    def calculate_soh(self, actual_capacity):
        soh = (actual_capacity / self.rated_capacity) * 100

        # Limit SOH between 0 and 100
        if soh > 100:
            soh = 100
        elif soh < 0:
            soh = 0

        return soh

    def check_voltage(self, voltage):
        if voltage < 3.0:
            return "LOW VOLTAGE"
        elif voltage > 4.2:
            return "OVER VOLTAGE"
        else:
            return "NORMAL"

    def check_temperature(self, temperature):
        if temperature < 0:
            return "LOW TEMPERATURE"
        elif temperature > 45:
            return "HIGH TEMPERATURE"
        else:
            return "NORMAL"

    def get_health_status(self, soh):
        if soh >= 80:
            return "GOOD"
        elif soh >= 60:
            return "FAIR"
        elif soh >= 40:
            return "WEAK"
        else:
            return "CRITICAL"

    def display(self, voltage, temperature, cycles,
                actual_capacity, soh):

        voltage_status = self.check_voltage(voltage)
        temperature_status = self.check_temperature(temperature)
        health_status = self.get_health_status(soh)

        print("\n====================================")
        print("     BATTERY HEALTH MONITORING")
        print("====================================")

        print(f"Voltage          : {voltage:.2f} V")
        print(f"Temperature      : {temperature:.2f} °C")
        print(f"Charge Cycles    : {cycles}")
        print(f"Rated Capacity   : {self.rated_capacity:.2f} Ah")
        print(f"Actual Capacity  : {actual_capacity:.2f} Ah")
        print(f"Battery SOH      : {soh:.2f}%")

        print("------------------------------------")
        print(f"Voltage Status   : {voltage_status}")
        print(f"Temperature      : {temperature_status}")
        print(f"Battery Health   : {health_status}")

        if soh < 40:
            print("WARNING: Battery replacement recommended.")
        elif temperature > 45:
            print("WARNING: Battery temperature is high.")
        elif voltage < 3.0:
            print("WARNING: Battery voltage is low.")
        else:
            print("System Status    : NORMAL")

        print("====================================")


# Main Program
print("BATTERY HEALTH MONITORING SYSTEM")

rated_capacity = float(input("Enter rated battery capacity (Ah): "))
actual_capacity = float(input("Enter actual battery capacity (Ah): "))
voltage = float(input("Enter battery voltage (V): "))
temperature = float(input("Enter battery temperature (°C): "))
cycles = int(input("Enter number of charge cycles: "))

# Input validation
if rated_capacity <= 0:
    print("Invalid rated capacity.")

elif actual_capacity < 0:
    print("Invalid actual capacity.")

elif actual_capacity > rated_capacity:
    print("Actual capacity cannot be greater than rated capacity.")

elif voltage < 0:
    print("Invalid voltage.")

elif cycles < 0:
    print("Invalid number of cycles.")

else:
    monitor = BatteryHealthMonitor(rated_capacity)

    soh = monitor.calculate_soh(actual_capacity)

    monitor.display(
        voltage,
        temperature,
        cycles,
        actual_capacity,
        soh
    )
