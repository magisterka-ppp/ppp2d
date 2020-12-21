import pygame
from pygame.math import Vector2
from pygame.rect import Rect


class Player(object):
    def __init__(self):
        self.grounded = False
        self.max_y_vel = 20
        self.drag = 0.8
        self.gravity = 6
        self.bounds = Rect(20, 0, 80, 120)
        self.color = (155, 155, 0)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         Rect(self.bounds.x,
                              self.bounds.y,
                              self.bounds.width,
                              self.bounds.height))

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
        self.bounds.x += round(self.vel.x, 0)

    def limit_fall_speed(self):
        if self.vel.y < self.max_y_vel:
            self.bounds.y += self.vel.y
        else:
            self.bounds.y += self.max_y_vel

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
                self.bounds.y = self.bounds.y - (self.bounds.y - (collider.y + collider.height))

            if right.colliderect(collider):
                self.vel.x = 0
                self.bounds.x = self.bounds.x - self.bounds.width - (self.bounds.x - collider.x)

            if left.colliderect(collider):
                self.vel.x = 0
                self.bounds.x = self.bounds.x - (self.bounds.x - (collider.x + collider.width))


    def collisions_feet(self, colliders):
        feet = self.get_feet()
        self.grounded = False
        self.vel.y += self.gravity
        for collider in colliders:
            if feet.colliderect(collider) and self.vel.y > 0.0:
                self.grounded = True
                self.vel.y = 0
                self.bounds.y = collider.y - self.bounds.height

    def get_feet(self):
        return Rect(self.bounds.x,
                    self.bounds.y + self.bounds.height,
                    self.bounds.width,
                    self.max_y_vel)

    def get_head(self):
        velocity = 0
        if self.vel.y < 0:
            velocity = self.vel.y
        return Rect(self.bounds.x,
                    self.bounds.y + velocity,
                    self.bounds.width,
                    -velocity)

    def get_right(self):
        velocity = 0
        if self.vel.x > 0:
            velocity = self.vel.x
        return Rect(self.bounds.x + self.bounds.width,
                    self.bounds.y,
                    velocity,
                    self.bounds.height)

    def get_left(self):
        velocity = 0
        if self.vel.x < 0:
            velocity = self.vel.x
        return Rect(self.bounds.x + velocity,
                    self.bounds.y,
                    -velocity,
                    self.bounds.height)
