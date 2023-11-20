class ExampleClass:
    # Class parameter
    class_parameter = "Class Parameter"

    def __init__(self, instance_parameter):
        # Instance parameter
        self.instance_parameter = instance_parameter

    def display_parameters(self):
        # Display both class and instance parameters
        print("Class Parameter:", self.class_parameter)
        print("Instance Parameter:", self.instance_parameter)

# Create instances of the class with different instance parameters
instance1 = ExampleClass("Instance 1")
instance2 = ExampleClass("Instance 2")

# Display parameters for each instance
print("Instance 1:")
instance1.display_parameters()

print("\nInstance 2:")
instance2.display_parameters()
