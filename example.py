import codesters
stage = codesters.Environment()
stage.set_background("summer")
sprite = codesters.Sprite("Alien1")
sprite.set_speed(0.5)
#sprite.move_up(100)
sprite.turn_left(90)
sprite.wait(2)
print sprite.get_wait_time(), "CHECKER 1"
sprite.glide_to(0,0)
sprite.wait(3)
print sprite.get_total_wait_time(), "checker 2"
sprite.right(70)
sprite.forward(100)

sprite2 = codesters.Sprite("")
sprite2.set_speed(0.5)

sprite2.glide_to(0,0)
sprite2.wait(1)
sprite2.set_direction(10,-10)
sprite2.forward(200)
sprite2.glide_to(0,0)
