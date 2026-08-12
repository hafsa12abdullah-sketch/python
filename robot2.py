class SimpleRobot:

    def __init__(self, name):
        self.name = name
        self.battery = 80  # Isko change karke 30 karke dekhein!

    def check_status(self):
        if self.battery > 50:
            return "Full Energy ⚡"
        else:
            return "Needs Charging 🔌"


# Object create karein
bot = SimpleRobot("PyBot")

# Values print karein
print("Robot Name:", bot.name)
print("Status:", bot.check_status())