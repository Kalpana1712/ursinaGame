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

        # Create plots
        self.create_plots()

        # Player controller
        self.player = FirstPersonController()

        # Instructions text
        self.instructions = Text(text="Walk around and click on a plot to plant!", scale=2, position=(-0.4, 0.4), parent=camera.ui)

    def setup_environment(self):
        # Set up a sky for the environment
        self.sky = Sky(color=color.rgb(135, 206, 235))  # Light blue sky color (sky blue)

    def create_plots(self):
        # Define the grid size and spacing
        rows = 4
        cols = 4
        plot_size = 1.5
        spacing = 0.5

        for row in range(rows):
            for col in range(cols):
                # Create a plot
                plot = Entity(
                    model='cube',  # Use a cube for the plot
                    color=color.brown,
                    position=(col * (plot_size + spacing) - (cols - 1) * (plot_size + spacing) / 2, 0.01, 
                              row * (plot_size + spacing) - (rows - 1) * (plot_size + spacing) / 2),
                    scale=(plot_size, 0.1, plot_size),  # Size of the plot
                    collider='box'  # Add a collider for interaction
                )
                plot.on_click = self.on_plot_click  # Assign the click event

    def on_plot_click(self):
        # Logic for when a plot is clicked
        print("Plot clicked!")

    def update(self):
        pass

if __name__ == '__main__':
    game = PlantationGame()
    game.run()
