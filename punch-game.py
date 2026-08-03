import turtle, time

t = turtle.Turtle()
t.color("blue")
t.speed(0)
t.penup()
dt = 0
bullets = []
last_time = 0

screen = turtle.Screen()
screen.tracer(0)
screen.listen()

def move_forward():
    t.forward(20)

def move_backward():
    t.backward(20)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

def shoot():
    b=bullet()
    bullets.append(b)
running = True
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(shoot,"e")
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

class bullet:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.shape("circle")
        self.t.shapesize(0.5, 0.5)
        self.t.color("red")
        self.t.penup()
        self.t.speed(0)
        self.t.goto(t.xcor(), t.ycor())
        self.t.setheading(t.heading())
        self.time = time.time()

        
    def move(self):
        self.t.fd(dt*100)
        if self.time + 5 <= time.time():
            self.t.hideturtle()
            bullets.remove(self)
            return
            
while running:
    curtime = time.time()
    dt = curtime - last_time
    using UnityEngine;

public class EnemyChase : MonoBehaviour
{
    public Transform player;           // assign in inspector or find at runtime
    public float speed = 3f;
    public float stoppingDistance = 1.2f;
    public int health = 3;

    void Update()
    {
        if (player == null) return;
        float dist = Vector2.Distance(transform.position, player.position);
        if (dist > stoppingDistance)
        {
            transform.position = Vector2.MoveTowards(transform.position, player.position, speed * Time.deltaTime);
        }
        // TODO: play walk/idle animations here based on distance
    }

    public void TakeDamage(int dmg)
    {
        health -= dmg;
        if (health <= 0) Die();
        // TODO: spawn hit VFX, play sound
    }

    void Die()
    {
        // TODO: drop loot, play death animation, then:
        Destroy(gameObject);
    }
}
    last_time = curtime
    for i in bullets:
        i.move()
    screen.update()
