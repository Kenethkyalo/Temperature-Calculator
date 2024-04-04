class Temperature:
    def __init__(self, value, scale='Celsius'):
        self.value = value
        self.scale = scale
    
    def convertCelsius(self):
        if self.scale == 'Celsius':
            return self.value
        elif self.scale == 'Fahrenheit':
            return (self.value - 32) * 5/9
        elif self.scale == 'Kelvin':
            return self.value - 273.15
        else:
            raise ValueError("Invalid scale. Accepted scales are Celsius, Fahrenheit, and Kelvin.")

    def convertFahrenheit(self):
        if self.scale == 'Celsius':
            return (self.value * 9/5) + 32
        elif self.scale == 'Fahrenheit':
            return self.value
        elif self.scale == 'Kelvin':
            return (self.value - 273.15) * 9/5 + 32
        else:
            raise ValueError("Invalid scale. Accepted scales are Celsius, Fahrenheit, and Kelvin.")



    def convert_fahrenheit(self):
        if self.scale == 'Celsius':
            return (self.value * 9/5) + 32
        elif self.scale == 'Fahrenheit':
            print("Temperature is already in Fahrenheit.")
            return self.value
        elif self.scale == 'Kelvin':
            return (self.value - 273.15) * 9/5 + 32
        else:
            raise ValueError("Invalid scale. Accepted scales are Celsius, Fahrenheit, and Kelvin.")
            
    def convert_celsius(self):
        if self.scale == 'Fahrenheit':
            return (self.value - 32) * 5/9
        elif self.scale == 'Celsius':
            print("Temperature is already in Celsius.")
            return self.value
        elif self.scale == 'Kelvin':
            return self.value - 273.15
        else:
            raise ValueError("Invalid scale. Accepted scales are Celsius, Fahrenheit, and Kelvin.")

    def __str__(self):
        return f"{self.value} {self.scale}"

# Example usage:
temp_celsius = Temperature(100, 'Celsius')
print(temp_celsius.convert_fahrenheit())  # This will print the equivalent temperature in Fahrenheit

temp_fahrenheit = Temperature(212, 'Fahrenheit')
print(temp_fahrenheit.convert_celsius())  # This will print the equivalent temperature in Celsius

