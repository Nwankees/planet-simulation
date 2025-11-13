import pygame
import math

DEFAULT_SCALE = 250
DEFAULT_TIMESTEP = 0.5


scale_input = input("Enter the scale you want to use(type \"Default\" to use the default scale value): ")
timestep_input = input("Enter the number of days you want to simulate(type \"Default\" to use the default timestep value): ")

settings = {
    "Scale" : DEFAULT_SCALE if scale_input.lower() == "default" else scale_input,
    "Timestep" : DEFAULT_TIMESTEP if timestep_input.lower() == "default" else timestep_input
}

pygame.init()

zoom_factor = 1.0
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
ORANGE = (255, 165, 0)
GOLD = (218, 165, 32)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (72, 61, 139)

class Planet:
    AU = 149.6E6 * 1000 # km -> m
    G = 6.67428e-11
    SCALE = settings["Scale"] / AU
    TIMESTEP = settings["Timestep"] * 24 * 60 * 60

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        scale = self.SCALE * zoom_factor
        x = self.x * scale + WIDTH / 2
        y = self.y * scale + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * scale + WIDTH / 2
                y = y * scale + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)
        pygame.draw.circle(win, self.color, (x,y), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

class Moon(Planet):
    def update_position(self, planets):
        total_fx = total_fy = 0

        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

def main():
    global zoom_factor
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    # Inner planets
    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 0.30 * 10**24)
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    # Outer planets
    jupiter = Planet(5.203 * Planet.AU, 0, 30, ORANGE, 1.898 * 10 ** 27)
    jupiter.y_vel = -13.07 * 1000

    saturn = Planet(9.537 * Planet.AU, 0, 26, GOLD, 5.683 * 10 ** 26)
    saturn.y_vel = -9.68 * 1000

    uranus = Planet(19.191 * Planet.AU, 0, 22, LIGHT_BLUE, 8.681 * 10 ** 25)
    uranus.y_vel = -6.80 * 1000

    neptune = Planet(30.07 * Planet.AU, 0, 20, DARK_BLUE, 1.024 * 10 ** 26)
    neptune.y_vel = -5.43 * 1000

    moon = Moon(earth.x + 384_400_000, earth.y, 6, WHITE, 7.34767309e22)
    moon.y_vel = earth.y_vel - 1_022
    moon.x_vel = earth.x_vel

    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, moon]

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_q:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:  # zoom in
                    zoom_factor *= 1.1
                elif event.key == pygame.K_MINUS or event.key == pygame.K_UNDERSCORE:  # zoom out
                    zoom_factor /= 1.1

        for planet in planets:
            if planet == moon:
                moon.update_position(planets)
            else:
                planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()

main()