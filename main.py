import drawing
import enemy
import vector
import inputs
app = drawing.PygameApp()
enemy_handler = enemy.EnemyHandler(app)
vector_handler = vector.VectorHandler(app, enemy_handler)
input_handler = inputs.InputHandler(app)

while app.loop():
    if app.game_state == drawing.GameStates.start:
        app.draw_start()
    else:
        app.draw_coordinates()
        enemy_handler.update_enemys()
        vector_handler.update_vectors()
        vect = input_handler.update()
        if vect != None:
            vector_handler.add_vector(vect)