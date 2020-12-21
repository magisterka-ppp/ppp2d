import pygame
from pygame.math import Vector2
from pygame.rect import Rect


class Player(object):
    def __init__(self):
        self.grounded = False
        self.max_y_vel = 20
        self.drag = 0.85
        self.gravity = 6
        self.collision_box = Rect(20, 0, 80, 120)
        self.color = (155, 155, 0)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.collision_box)
        #pygame.draw.rect(screen, (155, 0, 0), self.get_feet())
        #pygame.draw.rect(screen, (155, 0, 0), self.get_head())
        #pygame.draw.rect(screen, (155, 0, 0), self.get_right())
        #pygame.draw.rect(screen, (155, 0, 0), self.get_left())

    def add_force(self, force):
        self.acc = force

    def logic(self, game):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d]:
            self.add_force(Vector2(3, 0))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-3, 0))
        if pressed[pygame.K_w] and self.grounded:
            self.add_force(Vector2(0, -60))

        self.vel += self.acc
        self.acc *= 0

        self.collisions(game.ground.platforms)
        self.limit_fall_speed()

        self.vel.x *= self.drag
        self.collision_box.x += round(self.vel.x, 0)





    def limit_fall_speed(self):
        if self.vel.y < self.max_y_vel:
            self.collision_box.y += self.vel.y
        else:
            self.collision_box.y += self.max_y_vel

    def collisions(self, colliders):
        self.collisions_head(colliders)
        self.collisions_feet(colliders)

    def collisions_head(self, colliders):
        head = self.get_head()
        right = self.get_right()
        left = self.get_left()
        for collider in colliders:
            if head.colliderect(collider):
                self.vel.y = 0
            if right.colliderect(collider) or left.colliderect(collider):
                self.vel.x = 0

    def collisions_feet(self, colliders):
        feet = self.get_feet()
        self.grounded = False
        self.vel.y += self.gravity
        for collider in colliders:
            if feet.colliderect(collider) and self.vel.y > 0.0:
                self.grounded = True
                self.vel.y = 0
                self.collision_box.y = collider.y - self.collision_box.height

    def get_feet(self):
        return Rect(self.collision_box.x,
                    self.collision_box.y + self.collision_box.height,
                    self.collision_box.width,
                    self.max_y_vel)

    def get_head(self):
        velocity = 0
        if self.vel.y < 0:
            velocity = self.vel.y/2
        return Rect(self.collision_box.x,
                    self.collision_box.y + velocity,
                    self.collision_box.width,
                    -velocity)

    def get_right(self):
        velocity = 0
        if self.vel.x > 0:
            velocity = self.vel.x

        return Rect(self.collision_box.x + self.collision_box.width,
                    self.collision_box.y,
                    velocity,
                    self.collision_box.height)

    def get_left(self):
        velocity = 0
        if self.vel.x < 0:
            velocity = self.vel.x

        return Rect(self.collision_box.x + velocity,
                    self.collision_box.y,
                    -velocity,
                    self.collision_box.height)
