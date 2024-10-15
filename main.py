from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class PlantationGame(Ursina):
    def __init__(self):
        super().__init__()
        window.title = "3D Plantation Game for Kids"
        
        # Set up the ground
        self.ground = Entity(model='plane', texture='grass', scale=(20, 1, 20), collider='box')
        
        # Set up the environment (sky)
        self.setup_environment()
        
        # Create a single plot
        self.create_single_plot()
        
        # Player controller with no jump
        self.player = FirstPersonController(y=1, jump_height=0)
        
        # Instructions text
        self.instructions = Text(text="Walk around and click on the plot to plant!", scale=2, position=(-0.4, 0.4), parent=camera.ui)

    def setup_environment(self):
        # Set up a sky for the environment
        self.sky = Sky(color=color.rgb(135, 206, 235))  # Light blue sky color (sky blue)

    def create_single_plot(self):
        # Create a single plot
        self.plot = Entity(
            model='cube',  # Use a cube for the plot
            color=color.brown,
            position=(0, 0.01, 0),  # Position the plot at the center
            scale=(1.5, 0.1, 1.5),  # Size of the plot
            collider='box'  # Add a collider for interaction
        )
        self.plot.on_click = self.on_plot_click  # Assign the click event

    def on_plot_click(self):
        # Logic for when the plot is clicked
        print("Plot clicked!")

    def update(self):
        pass

if __name__ == '__main__':
    game = PlantationGame()
    game.run()
