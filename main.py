from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class PlantationGame(Ursina):
    def __init__(self):
        super().__init__()
        window.fullscreen = False
        window.borderless = False
        window.title = "3D Plantation Game for Kids"
        
        # Set up the environment
        self.ground = Entity(model='plane', texture='white_cube', color=color.brown, scale=(20, 1, 20), collider='box')
        self.sky = Sky()  # Add a skybox

        # Tools (Buttons for interaction)
        self.shovel = Button(text='Shovel', scale=0.1, position=(-0.5, -0.4), parent=camera.ui)
        self.seeds = Button(text='Seeds', scale=0.1, position=(0, -0.4), parent=camera.ui)
        self.water = Button(text='Water', scale=0.1, position=(0.5, -0.4), parent=camera.ui)
        
        # Custom progress bar (to show plant growth progress)
        self.progress_bg = Entity(model='quad', color=color.gray, scale=(0.4, 0.05), position=(0, 0.45), parent=camera.ui)
        self.progress_bar = Entity(model='quad', color=color.green, scale=(0.0, 0.05), position=(-0.2, 0.45), origin=(-0.5, 0), parent=camera.ui)
        
        # Instructions text to guide the player
        self.instructions = Text(text="Click on the shovel to start!", scale=2, y=0.4, parent=camera.ui)
        
        # Plant (initially invisible)
        self.plant = Entity(model='cube', scale=(0.5, 0.5, 0.5), color=color.green, position=(0, 0.25, 0), visible=False)
        
        # Player controller
        self.player = FirstPersonController()

        # Game state
        self.stage = 0
        self.stages = ["dig", "plant", "water", "grow"]
        
        # Set up tool click events
        self.shovel.on_click = self.use_shovel
        self.seeds.on_click = self.use_seeds
        self.water.on_click = self.use_water

    def use_shovel(self):
        if self.stage == 0:
            self.ground.color = color.rgb(139, 69, 19)  # Change ground color to represent dug soil
            self.instructions.text = "Great! Now plant the seeds."
            self.stage += 1

    def use_seeds(self):
        if self.stage == 1:
            self.plant.visible = True
            self.plant.color = color.yellow  # Change plant color to represent seeds
            self.instructions.text = "Seeds planted! Time to water them."
            self.stage += 1

    def use_water(self):
        if self.stage == 2:
            self.plant.color = color.lime  # Change plant color to represent sprouting
            self.instructions.text = "Wonderful! Watch your plant grow."
            self.stage += 1
            self.grow_plant()

    def grow_plant(self):
        # Simulate plant growth by scaling and updating the progress bar
        self.plant.animate_scale((1.5, 3, 1.5), duration=2)
        self.progress_bar.scale_x = 0.25  # Indicating 25% progress
        invoke(self.final_growth, delay=2)

    def final_growth(self):
        self.plant.color = color.orange  # Change plant color to represent full growth
        self.progress_bar.scale_x = 1  # Indicating 100% progress
        self.instructions.text = "Congratulations! You grew a plant!"

    def update(self):
        pass

if __name__ == '__main__':
    game = PlantationGame()
    game.run()
